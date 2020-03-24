import json

from AF.af import Af
from AF.Afn import Afn

if __name__ == "__main__":
    with open("dfa.json", "r") as f:
        data = json.load(f)

        con = Af(data)
        print(con)
        # print(con.minimize())
        print((con.read("aab")))
    with open("nfa.json", "r") as f:
        data = json.load(f)
        con = Afn(data)
        print(con.dictionary())
        print(con.determine())
