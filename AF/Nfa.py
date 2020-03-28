from typing import Dict, Any, Tuple, List, Union

from AF.State_fa import State_fa
from AF.dfa import Dfa


class Nfa:
    def __init__(self, automaton):
        """
        Init a attributes of automaton
        :param automaton :
        """
        self.__automaton = automaton
        self.__states: list = self._get_states()
        self.__alphabet: dict = self.__automaton["alphabet"]
        self.__dictionary: dict = self._dictionary()
        if self.__automaton["deterministic"]:
            raise TypeError

    @property
    def automaton(self):
        return self.__automaton

    @property
    def states(self):
        return self.__states

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def dictionary(self):
        return self.__dictionary

    def determine(self) -> Dfa:
        start = self._start_state().state
        table = {tuple([start]): self.__dictionary[start]}  # initial _dictionary
        next_key = self._next_key(table, self._get_values(start, self.__dictionary))
        return self._to_dfa(self._determine(next_key, table))

    def _determine(self, key: Tuple, table: Dict) -> Dict:
        if self._is_none_next_key(key):
            return table
        table[key] = self._morphs_key(key)  # set directed to morphism
        next_key = self._next_key(table, self._get_values(key, table))
        return self._determine(next_key, table)

    def _morphs_key(self, key: tuple) -> dict:
        dictionary_morphs: Dict[Any, Tuple[Any, ...]] = {}
        for symbol in self.__alphabet:
            _set = set()
            for elem in key:
                morph = self.__dictionary[elem][symbol]
                _set.update(morph)
            dictionary_morphs[symbol] = tuple(_set)
        return dictionary_morphs

    def _to_dfa(self, dictionary_convert: dict) -> Dfa:
        return Dfa({'deterministic': True,
                    'alphabet': self.__alphabet,
                    'states': self._generate_list_states_dfa(dictionary_convert)})

    def _generate_list_states_dfa(self, dic: dict) -> List[dict]:
        _list_keys = list(dic.keys())
        return [{'state': _list_keys.index(key),
                 'final': self._is_final_state(key),
                 'start': self._is_start_state(key),
                 'morphs': {s: _list_keys.index(dic[key][s])
                            for s in self.__alphabet}} for key in _list_keys]

    def _is_start_state(self, args: tuple) -> bool:
        if len(args) == 1:
            return self.__states[args[0]].is_start()
        return False

    def _is_final_state(self, args: Tuple) -> bool:
        for i in args:
            if self.__states[i].is_final():
                return True
        return False

    def _start_state(self) -> State_fa:
        start_state = (x for x in self.__states if x.is_start())
        return next(start_state)

    def _get_states(self) -> list:
        return [State_fa(i["state"]
                         , i["final"]
                         , i["start"]
                         , i["morphs"]) for i in self.__automaton["states"]]

    def _dictionary(self) -> Dict:
        return {h.state: {j: tuple(h.morphs[j])
                          # uso de una tupla para key : las tuplas al ser inmutables pueden usarse como key
                          for j in self.__alphabet}
                for h in self.__states
                }

    @staticmethod
    def _is_none_next_key(next_key: Tuple) -> bool:
        return True if next_key is None else False

    @staticmethod
    def _get_values(next_key: Tuple, table: Dict) -> Tuple:
        return table[next_key].values()

    @staticmethod
    def _next_key(table: Dict, args: tuple) -> Union[None, Tuple]:
        for value in args:
            if value not in table:
                return value
        return None
