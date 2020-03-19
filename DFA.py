class DFA:
    def __init__(self, automat):
        self.automat = automat
        self.states = self.get_states()
        self.alphabet = self.get_alphabet()
        self.__diction = self.dictionary()

    def get_states(self):
        return [self.FA(i["state"]
                        , i["final"]
                        , i["start"]
                        , i["morphs"]) for i in self.automat["states"]]

    def get_alphabet(self):
        return self.automat["alphabet"]

    class FA:

        def __init__(self, state, final, start, morphs):
            self.state = state
            self.final = final
            self.start = start
            self.morphs = morphs

        def is_final(self):
            return self.final

        def is_star(self):
            return self.start

        def state_in_morph(self, morph):
            return self.morphs[morph]

        def __repr__(self):
            return str(self.state)

    def __initial_sets(self):
        conant_de_tots_eds_estate = set(self.states)
        con1 = set(filter(lambda x: x.is_final(), self.states))
        con2 = con1 ^ conant_de_tots_eds_estate
        con1 = {x.state for x in con1}
        con2 = {x.state for x in con2}
        return con1, con2

    def __sets_generator(self, set_of_states):
        yes = set()
        no = set()
        for i in set_of_states:
            for j in self.__diction[i]:
                if j not in set_of_states:
                    no.add(i)
                    yes.discard(i)
                    break
                else:
                    yes.add(i)
        if len(set_of_states) == 2 and len(no) == 2:
            return [{no.pop()}, no]
        return [yes, no]

    def minimize(self):
        return self.__minimize(self.__initial_sets())

    def __minimize(self, con):
        set1 = []
        for i in con:
            a = self.__sets_generator(i)
            set1 = set1 + a
        set2 = [x for x in set1 if len(x) > 0]
        if con != set2:
            return self.__minimize(set2)
        return set2

    def dictionary(self):
        return {h.state: [h.morphs[j]
                          for j in self.alphabet]
                for h in self.states
                }

    def __repr__(self):
        return self.__diction

    def __str__(self):
        return str(self.__repr__())
