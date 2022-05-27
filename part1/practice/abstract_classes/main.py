# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть унаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport

# экземпляр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключений
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


class Boat(Transport):

    def start_engine(self):
        print('Пых-пых-пых')

    def stop_engine(self):
        print('Бум! Бах! Пошёл черный дым')

    def move(self):
        print('Ветер в лицо, брызги на штанах, лодка летит на волнах')

    def stop(self):
        print('Упс! Что-то пошло не так и отвалился винт')


class Car(Transport):

    def start_engine(self):
        print('Тра-та-та')

    def stop_engine(self):
        print('Клац. Двигатель заглох')

    def move(self):
        print('Лето, жара, море... где-то, а ты едешь на работу по пробкам')

    def stop(self):
        print('Ой! Красный свет!')


class Electroscooter(Transport):

    def start_engine(self):
        print('        *никаких звуков нет*        ')

    def stop_engine(self):
        print('        *опять таки никаких звуков нет*        ')

    def move(self):
        print('Вжжжжууууух')

    def stop(self):
        print('Хуууууужжжжжв')


class Person:

    def use_transport(self, transport_obj):
        transport_obj.start_engine()
        transport_obj.move()
        transport_obj.stop()
        transport_obj.stop_engine()


# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
