from typing import Dict, Any, Tuple, List, Union

from AF.State_fa import State_fa
from AF.dfa import Dfa


class Nfa:
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

    def determine(self) -> Dfa:
        start = self.__start_state().state
        table = {tuple([start]): self.__diction[start]}  # initial dictionary
        next_key = self.__next_key(table, self.__get_values(start, self.__diction))
        return self.__to_dfa(self.__determine(next_key, table))

    def __determine(self, key: Tuple, table: Dict) -> Dict:
        if self.__is_none_next_key(key):
            return table
        table[key] = self.__morphs_key(key)  # set directed to morphism
        next_key = self.__next_key(table, self.__get_values(key, table))
        return self.__determine(next_key, table)

    def __morphs_key(self, key: tuple) -> dict:
        dictionary_morphs: Dict[Any, Tuple[Any, ...]] = {}
        for symbol in self.alphabet:
            _set = set()
            for elem in key:
                morph = self.__diction[elem][symbol]
                _set.update(morph)
            dictionary_morphs[symbol] = tuple(_set)
        return dictionary_morphs

    def __to_dfa(self, dictionary_convert: dict) -> Dfa:
        return Dfa({'deterministic': True,
                    'alphabet': self.alphabet,
                    'states': self.__generate_list_states_dfa(dictionary_convert)})

    def __generate_list_states_dfa(self, dic: dict) -> List[dict]:
        _list_keys = list(dic.keys())
        return [{'state': _list_keys.index(key),
                 'final': self.__is_final_state(key),
                 'start': self.__is_start_state(key),
                 'morphs': {s: _list_keys.index(dic[key][s])
                            for s in self.alphabet}} for key in _list_keys]

    def __is_start_state(self, args: tuple) -> bool:
        if len(args) == 1:
            return self.states[args[0]].is_start()
        return False

    def __is_final_state(self, args: Tuple) -> bool:
        for i in args:
            if self.states[i].is_final():
                return True
        return False

    def __start_state(self) -> State_fa:
        start_state = (x for x in self.states if x.is_start())
        return next(start_state)

    def __get_states(self) -> list:
        return [State_fa(i["state"]
                         , i["final"]
                         , i["start"]
                         , i["morphs"]) for i in self.automaton["states"]]

    def dictionary(self) -> Dict:
        return {h.state: {j: tuple(h.morphs[j])
                          # uso de una tupla para key : las tuplas al ser inmutables pueden usarse como key
                          for j in self.alphabet}
                for h in self.states
                }

    @staticmethod
    def __is_none_next_key(next_key: Tuple) -> bool:
        return True if next_key is None else False

    @staticmethod
    def __get_values(next_key: Tuple, table: Dict) -> Tuple:
        return table[next_key].values()

    @staticmethod
    def __next_key(table: Dict, args: tuple) -> Union[None, Tuple]:
        for value in args:
            if value not in table:
                return value
        return None
