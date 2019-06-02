from abc import ABCMeta, abstractclassmethod

class Base(metaclass=ABCMeta):

    @abstractclassmethod
    def read(self):
        pass

    @abstractclassmethod
    def write(self):
        pass
