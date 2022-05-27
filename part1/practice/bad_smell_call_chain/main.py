# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов
class Person:
    def __init__(self, room_number):
        self.room = room_number

    def get_person_room(self):
        return self.room

    def __repr__(self):
        return f'Номер комнаты: {self.get_person_room()}'


class Planet:
    def __init__(self, city_population: int):
        self.city_population = city_population

    def get_country(self):
        return self.get_city()

    def get_city(self):
        return self.get_street()

    def get_street(self, person):
        return person.get_person_room()

    def get_city_population(self):
        return self.city_population


if __name__ == '__main__':
    person = Person(room_number=55)
    print(person)
    planet = Planet(city_population=100200300)
    planet.get_city_population()
    print(planet.get_street(person))
