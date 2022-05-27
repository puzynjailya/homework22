from part1.practice.abstract_classes.transport import Transport


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