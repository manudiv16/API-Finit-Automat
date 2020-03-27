from typing import Dict, Any, Tuple

from AF.State_fa import State_fa
from AF.dfa import Dfa


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

    def determine(self) -> dict:
        a = self.__start_state().state
        table = {tuple([a]): self.__diction[a]}
        next_key = self.__next_key(table, self.__diction[a].values())
        all_in_table = False if next_key is None else True
        while all_in_table:
            table[next_key] = self.__morphs_key(next_key)
            next_key = self.__next_key(table, table[next_key].values())
            all_in_table = False if next_key is None else True
        return self.procesado_de_determinacion(table)

    @staticmethod
    def __next_key(table, args):
        for value in args:
            if value not in table:
                return value
        return None

    def __morphs_key(self, key: tuple) -> dict:
        dictionary_morphs: Dict[Any, Tuple[Any, ...]] = {}
        for symbol in self.alphabet:
            _set = set()
            for elem in key:
                morph = self.__diction[elem][symbol]
                _set.update(morph)
            dictionary_morphs[symbol] = tuple(_set)
        return dictionary_morphs

    def to_dfa(self, dictionary_convert):
        x = {'deterministic': True,
             'alphabet': self.alphabet,
             'states': []}
        return Dfa(x)

    def procesado_de_determinacion(self, dic):
        print(dic)
        l = list(dic.keys())
        h = {l.index(key): {s: l.index(dic[key][s])
                            for s in self.alphabet}
             for key in l}

        return

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
