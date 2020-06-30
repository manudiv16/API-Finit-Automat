import os

from flask import Flask, request, send_file, after_this_request

from AF.dfa import Dfa

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/afn', methods=['POST'])
def afn():
    data = request.json
    non_final_automaton = Dfa(data)
    name_file = "hola"
    filename = non_final_automaton.dot_dictionary(name_file)

    @after_this_request
    def remove_file(response):
        try:
            os.remove(filename)
            os.remove(f"{name_file}.dot")
            return response
        except Exception as error:
            app.logger.error("error removing file", error)

    try:
        return send_file(filename)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
