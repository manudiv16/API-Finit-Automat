import json

from AF.af import Af
from AF.Nfa import Nfa
from AF.dfa import Dfa

if __name__ == "__main__":
    with open("dfa.json", "r") as f:
        data = json.load(f)

        con = Dfa(data)
        print(con)
        print(con.minimize())
        print((con.read("aab")))
    with open("nfa.json", "r") as f:
        data = json.load(f)
        con = Nfa(data)
        print(con.dictionary)
        b = con.determine()
        print(b)
        print(b.minimize())
