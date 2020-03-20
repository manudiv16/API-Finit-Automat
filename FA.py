import json

from DFA import DFA

if __name__ == "__main__":
    with open("dfa.json", "r") as f:
        data = json.load(f)

        con = DFA(data)
        print(con)
        print(con.dictionary())
        print(con.minimize())
        print((con.read("")))
