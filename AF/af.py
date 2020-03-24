from AF.dfa import Dfa


class Af:
    def __init__(self, automaton):
        self.automaton = automaton
        if self.automaton["deterministic"]:
            self.heritage = Dfa(automaton)
        elif not self.automaton["deterministic"]:
            self.heritage = None
        else:
            raise TypeError

    def read(self, word):
        return self.heritage.read(word)

    def __str__(self):
        return self.heritage.__str__()
