import abc
from AF.dfa import Dfa
from AF.Nfa import Nfa


class Interface_Fa(abc.ABC):
    @abc.abstractmethod
    def dictionary(self):
        pass

    @abc.abstractmethod
    def read(self, world: str):
        pass

    @abc.abstractmethod
    def automaton(self):
        pass

    @abc.abstractmethod
    def states(self):
        pass

    @abc.abstractmethod
    def alphabet(self):
        pass


class Fa(Interface_Fa):
    def __init__(self, automaton):
        self.__automaton = automaton
        if self.automaton["deterministic"]:
            self.heritage = Dfa(automaton)
        elif not self.automaton["deterministic"]:
            self.heritage = Nfa(automaton)
        else:
            raise TypeError

    def read(self, word):
        return self.heritage.read(word)

    @property
    def automaton(self):
        return self.__automaton

    @property
    def states(self):
        return self.heritage.states

    @property
    def alphabet(self):
        return self.heritage.alphabet

    @property
    def dictionary(self):
        return self.heritage.dictionary

    def __repr__(self):
        return self.heritage.dictionary

    def __str__(self):
        return self.heritage.__str__()
