import abc


class Algorithm(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def target_function(self, **kwargs):
        pass

    @abc.abstractmethod
    def initial_position(self):
        pass

    @abc.abstractmethod
    def algorithm(self):
        pass
