import json

from dfa import Dfa

if __name__ == "__main__":
    with open("dfa.json", "r") as f:
        data = json.load(f)

        con = Dfa(data)
        print(con)
        print(con.minimize())
        print((con.read("")))
