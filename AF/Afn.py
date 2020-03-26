from typing import Dict, Any

from AF.State_fa import State_fa


class Afn:
    def __init__(self, automaton):
        """
        Init a attributes of automaton
        :param automaton :
        """
        self.automaton = automaton
        self.states: list = self.__get_states()
        self.alphabet: dict = self.automaton["alphabet"]
        self.__diction: dict = self.dictionary()
        if self.automaton["deterministic"]:
            raise TypeError

    def determine(self):
        a = self.__start_state().state
        table = {tuple([a]): self.__diction[a]}
        while True:
            b = self.__next_key(table, self.__diction[a].values())
            b = self.__morphs_key(b)
            break
        return b

    def __morphs_key(self, key):

        d = {x: tuple(self.__diction[j][x] for j in key if len(self.__diction[j][x]) > 0) for x in self.alphabet}
        return d

    def __next_key(self, table, args):
        for x in args:
            if x not in table:
                return x

    def __start_state(self):
        start_state = (x for x in self.states if x.is_start())
        return next(start_state)

    def __get_states(self) -> list:
        return [State_fa(i["state"]
                         , i["final"]
                         , i["start"]
                         , i["morphs"]) for i in self.automaton["states"]]

    def dictionary(self):
        return {h.state: {j: tuple(h.morphs[j])
                          # uso de una tupla para key : las tuplas al ser inmutables pueden usarse como key
                          for j in self.alphabet}
                for h in self.states
                }
