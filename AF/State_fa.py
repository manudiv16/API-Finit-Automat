
class State_fa:
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