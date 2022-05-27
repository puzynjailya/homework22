# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop
from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass
