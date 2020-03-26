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
        b = self.__next_key(table, self.__diction[a].values())
        c = self.__morphs_key(b)
        table[b] = c
        i = 0
        while i < 6:
            b = self.__next_key(table, table[b].values())
            c = self.__morphs_key(b)
            table[b] = c
            i = i + 1

        return table

    def __morphs_key(self, key):
        hola = {}
        for x in self.alphabet:
            for i in key:
                a = self.__diction[i][x]
                if len(a) > 0:
                    if x in hola:
                        hola[x] = hola[x] + a if a not in hola[x] else None
                    else:
                        hola[x] = a
        return hola

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
