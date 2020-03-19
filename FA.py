import json


class FA:

    def __init__(self, state, final, start, morphs):
        self.state = state
        self.final = final
        self.start = start
        self.morphs = morphs

    def is_final(self):
        return self.final

    def state_in_morph(self, morph):
        return self.morphs[morph]

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)


class Automate:
    def __init__(self, states):
        self.states = states
        self.__diction = self.dictionary()

    def dictionary(self):
        return {h.state: [h.morphs[j]
                          for j in range(len(h.morphs))]
                for h in self.states
                }

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


if __name__ == "__main__":
    with open("dfa.json", "r") as f:
        data = json.load(f)
        list_of_states = []
        for state in data["states"]:
            state_actual = state["state"]
            final = state["final"]
            start = state["start"]
            morphs = state["morphs"]
            list_of_states.append(FA(state_actual
                                     , final
                                     , start
                                     , morphs))

        print(list_of_states)
        con = Automate(list_of_states)
