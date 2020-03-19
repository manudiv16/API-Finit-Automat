import typing


class FA:

    def __init__(self, state, final, start, morphs):
        self.state = state
        self.__final = final
        self.__start = start
        self.morphs = morphs

    def is_final(self):
        return self.__final

    def is_star(self):
        return self.__start

    def state_in_morph(self, morph):
        return self.morphs[morph]

    def __repr__(self):
        return str(self.state)


class DFA:
    def __init__(self, automat):
        self.automat = automat
        self.states: list = self.__get_states()
        self.alphabet: dict = self.automat["alphabet"]
        self.__diction: dict = self.dictionary()

    def __get_states(self) -> list:
        return [FA(i["state"]
                   , i["final"]
                   , i["start"]
                   , i["morphs"]) for i in self.automat["states"]]

    def __initial_sets(self) -> typing.Tuple[set, set]:
        conant_de_tots_eds_estate = set(self.states)
        con1 = set(x for x in self.states if x.is_final())
        con2 = con1 ^ conant_de_tots_eds_estate
        con1 = {x.state for x in con1}
        con2 = {x.state for x in con2}
        return con1, con2

    def __sets_generator(self, set_of_states: tuple) -> list:
        no, yes = self.__divide_sets(set_of_states)
        if len(set_of_states) == 2 and len(no) == 2:
            return [{no.pop()}, no]
        if len(yes) == 0:
            return [no]
        if len(no) == 0:
            return [yes]
        return [yes, no]

    def minimize(self) -> list:
        """
        initialize sets with final sets and the others
        :return:
        """
        return self.__minimize(self.__initial_sets())

    def __minimize(self, con) -> list:
        set1 = []
        for i in con:
            a: list = self.__sets_generator(i)
            set1 = set1 + a
        if con != set1:
            return self.__minimize(set1)
        return set1

    def dictionary(self) -> dict:
        return {h.state: {j: h.morphs[j]
                          for j in self.alphabet}
                for h in self.states
                }

    def read(self, palabra):
        start_states = [x for x in self.states if x.is_start()]

    def readles(self, simbolo):
        pass

    def __divide_sets(self, set_of_states: tuple) -> typing.Tuple[set, set]:
        yes, no = set(), set()
        for i in set_of_states:
            for j in self.__diction[i]:
                if self.__diction[i][j] in set_of_states:
                    yes.add(i)
                else:
                    no.add(i)
                    yes.discard(i)
                    break
        return no, yes

    def __repr__(self):
        return self.__diction

    def __str__(self):
        return str(self.__repr__())
