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

    # def determine(self):
    #     l = []
    #     # {self.__start_state()}
    #
    #     return
    #
    # def register(self, state):
    #     for x in state:
    #         self.where_go(x,)
    #     return

    def __start_state(self):
        start_state = (x for x in self.states if x.is_start())
        return next(start_state)

    def __get_states(self) -> list:
        return [State_fa(i["state"]
                         , i["final"]
                         , i["start"]
                         , i["morphs"]) for i in self.automaton["states"]]

    def dictionary(self):
        return {h.state: {j: h.morphs[j]
                          for j in self.alphabet}
                for h in self.states
                }
