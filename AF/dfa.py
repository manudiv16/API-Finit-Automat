"""Este es el docstring de mi_paquete"""

from typing import Tuple, Generator, Any, List, Union, Dict
from AF.State_fa import State_fa


class Dfa:
    """
        Create deterministic finite automaton
    """

    def __init__(self, automaton):
        """
        Initialize a attributes of automaton
        :param automaton dictionary :
        """
        self.automaton = automaton
        self.states: list = self.__get_states()
        self.alphabet: dict = self.automaton["alphabet"]
        self.__diction: dict = self.dictionary()
        if not self.automaton["deterministic"]:
            raise TypeError

    def minimize(self) -> Dict[Any, Union[dict, Any]]:
        """
        Initialize sets with final states and the others , generate dictionary with the minimized automaton
        :return dictionary:
        """
        automaton_minimized = self.__minimize(self.__final_or_not())
        return self.__put_the_morphs(automaton_minimized)

    def dictionary(self) -> dict:
        """
        format a dictionary
        :return dictionary of states :
        """
        return {h.state: {j: h.morphs[j]
                          for j in self.alphabet}
                for h in self.states
                }

    def read(self, word: str) -> Union[bool, str]:
        """
        the firsts states determines the start of the automaton
        read set of symbols and determine this automaton accept this symbols
        :param word:
        :return boolean value :
        """
        for i in self.__sets_start():
            try:
                if not self.__read(word, i.state):
                    return False
            except ValueError:
                return "No Has intraducido una cadena valida"
        return True

    def __read(self, word: str, state: int) -> bool:
        if len(word) != 0:
            char: str = word[0]
            if char not in self.alphabet:
                raise ValueError
            next_state: int = self.__diction[state][char]
            return self.__read(word[1:], next_state)
        return self.states[state].is_final()

    def __final_or_not(self) -> Tuple[set, set]:
        finals_states = set(x for x in self.states if x.is_final())
        non_final_states = finals_states ^ set(self.states)
        finals_states = {x.state for x in finals_states}
        non_final_states = {x.state for x in non_final_states}
        return finals_states, non_final_states

    def __sets_start(self) -> Generator[Any, Any, None]:
        return (x for x in self.states if x.is_start())

    def __minimize(self, sets) -> list:
        category = []
        for i in sets:
            var = self.__sets_generator(i)
            category = category + var  # union of sets in set1
        if sets != category:  # verify the changes of sets,
            return self.__minimize(category)  # when the set is equal stop recursive call
        return category

    def __sets_generator(self, set_of_states: tuple) -> List[set]:
        out, in_ = self.__divide_sets(set_of_states)
        if len(set_of_states) == 2 and len(out) == 2:
            return [{out.pop()}, out]
        if len(in_) == 0:
            return [out]
        if len(out) == 0:
            return [in_]
        return [in_, out]

    def __divide_sets(self, set_of_states: tuple) -> Tuple[set, set]:
        in_, out = set(), set()
        for i in set_of_states:
            for j in self.__diction[i]:
                if self.__diction[i][j] in set_of_states:
                    in_.add(i)
                else:
                    out.add(i)
                    in_.discard(i)
                    break
        return out, in_

    def __get_states(self) -> list:
        return [State_fa(i["state"]
                         , i["final"]
                         , i["start"]
                         , i["morphs"]) for i in self.automaton["states"]]

    def __put_the_morphs(self, lists):
        def exist(s):
            for i, j in enumerate(lists):
                if s in j:
                    return i

        minimized_dict = {}
        for key, elem in enumerate(lists):
            if len(elem) == 1:
                minimized_dict[key]= {s: exist(self.states[list(elem)[0]].morphs[s]) for s in self.alphabet}
            else:
                minimized_dict[key] = {x: key for x in self.alphabet}
        return minimized_dict

    def __repr__(self):
        return self.__diction

    def __str__(self):
        return str(self.__repr__())
