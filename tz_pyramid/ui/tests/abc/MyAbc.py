from abc import ABC, abstractmethod

class AbstractAdder(ABC):
    @abstractmethod
    def add(self, value1, valu2):
        print("111111111")
        pass

class ConcreteAdder(AbstractAdder):
    def add(self, value1, value2):
        print("2222222222")
        return value1 + value2

def AddExecuter(AbstractAdder):
    return AbstractAdder.add(1, 2)