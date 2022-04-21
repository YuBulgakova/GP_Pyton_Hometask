# 1
from time import sleep


class Trafficlight:
    __color = ('red', 'yellow', 'green')

    def running(self):
        print(f'traffic light on')
        mode = Trafficlight.__color[0]
        print(mode)
    #    sleep(7)
        mode = Trafficlight.__color[1]
        print(mode)
     #   sleep(2)
        mode = Trafficlight.__color[2]
        print(mode)
     #   sleep(5)


trafficlite1 = Trafficlight()
trafficlite1.running()


# 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_cover_calc(self, k, dep):
        mass = self._length * self._length * k * dep
        print(f'Road cover mass = {mass} t')


r1 = Road(10, 10)
r1.road_cover_calc(1, 1)


# 3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + self.surname
        print(f'Worker full name: {full_name}')

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f'Total income = {total_income}')


p_1 = Position('Ivan', 'Jacobs', 'manager', 1000, 500)
print(p_1.name)
print(p_1.surname)
print(p_1.position)
print(p_1._income)
p_1.get_full_name()
p_1.get_total_income()

# 4
print('*' * 20)


class Car:
    def __init__(self, color, speed, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.color} {self.name} goes')

    def stop(self):
        print(f'{self.color} {self.name} stops')

    def turn(self, direction):
        if direction == 'r':
            print('The car turns right')
        if direction == 'l':
            print('The car turns left')

    def show_speed(self):
        print(f'Current speed is: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed is exceeded!')
        else:
            print(f'Current speed is: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed is exceeded!')
        else:
            print(f'Current speed is: {self.speed}')


class SportCar(Car):
    def __init__(self, color, name, turbo, speed=220):
        super().__init__(color, speed, name)
        self.turbo = turbo


class PoliceCar(Car):
    def __init__(self, speed, name, color='blue'):
        super().__init__(color, speed, name)
     #   self.color = 'blue'
        self.is_police = True


sc2 = SportCar('red', 'MacLaren', True)
sc2.go()
sc2.show_speed()
sc2.turn('r')
sc2.stop()
print(sc2.is_police)
print(sc2.color, sc2.name)

pc1 = PoliceCar(40, 'UAZ')
pc1.go()
print(pc1.is_police)
pc1.show_speed()

c1 = Car('yellow', 100, 'Mersedes', )
c1.go()
c1.turn('l')

tc1 = TownCar('white', 100, 'Hundai')
tc1.go()
tc1.show_speed()

# 5
print('*' * 20)


class Stationery():
    title = ['pen', 'pensil', 'handle']

    def draw(self):
        print('start rendering')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title[0]} is drawing')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title[1]} is drawing')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title[2]} is drawing')


s1 = Stationery()
s1.draw()
p_1 = Pen()
p_1.draw()
pl_1 = Pencil()
pl_1.draw()
h_1 = Handle()
h_1.draw()
