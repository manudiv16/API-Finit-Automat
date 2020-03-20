"""Este es el docstring de mi_paquete"""

from typing import Tuple, Generator, Any, List


class Fa:
    """
        Create state of finite automaton
    """

    def __init__(self, state, final, start, morphs):
        self.state = state
        self.__final = final
        self.__start = start
        self.morphs = morphs

    def is_final(self) -> bool:
        """
        :return true when state is a starter state and false when no:
        """
        return self.__final

    def is_start(self) -> bool:
        """
        :return true when state is a starter state and false when no:
        """
        return self.__start

    def __repr__(self):
        return str(self.state)


class Dfa:
    """
        Create deterministic finite automaton
    """

    def __init__(self, automaton):
        """
        Init a attributes of automaton
        :param automaton :
        """
        self.automaton = automaton
        self.states: list = self.__get_states()
        self.alphabet: dict = self.automaton["alphabet"]
        self.__diction: dict = self.dictionary()

    def minimize(self) -> list:
        """
        initialize sets with final sets and the others
        :return list of sets minimized:
        """
        return self.__minimize(self.__initial_sets())

    def dictionary(self) -> dict:
        """
        format a dictionary
        :return dictionary of states :
        """
        return {h.state: {j: h.morphs[j]
                          for j in self.alphabet}
                for h in self.states
                }

    def read(self, word: str) -> bool:
        """
        read set of symbols and determine this automaton accept this symbols
        :param word:
        :return boolean value :
        """
        for i in self.__sets_start():
            if not self.__read(word, i.state):
                return False
        return True

    def __read(self, word, state):
        if len(word) != 0:
            char = word[0]
            if char not in self.alphabet:
                return Exception
            next_state = self.__diction[state][char]
            return self.__read(word[1:], next_state)
        return self.states[state].is_final()

    def __initial_sets(self) -> Tuple[set, set]:
        finals_states = set(x for x in self.states if x.is_final())
        non_final_states = finals_states ^ set(self.states)
        finals_states = {x.state for x in finals_states}
        non_final_states = {x.state for x in non_final_states}
        return finals_states, non_final_states

    def __sets_start(self) -> Generator[Any, Any, None]:
        return (x for x in self.states if x.is_start())

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
        return [Fa(i["state"]
                   , i["final"]
                   , i["start"]
                   , i["morphs"]) for i in self.automaton["states"]]

    def __minimize(self, sets) -> list:
        category = []
        for i in sets:
            var = self.__sets_generator(i)
            category = category + var  # union of sets in set1
        if sets != category:  # verify the changes of sets,
            return self.__minimize(category)  # when the set is equal stop recursive call
        return category

    def __repr__(self):
        return self.__diction

    def __str__(self):
        return str(self.__repr__())
