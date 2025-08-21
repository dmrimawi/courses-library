from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    @abstractmethod
    def introduce(self):
        pass
