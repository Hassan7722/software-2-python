import random
from tabulate import tabulate

class Car:
    def __init__(self, new_reg_num, new_max_speed, new_current_speed=0, new_distance=0):
        self.reg_num = new_reg_num
        self.max_speed = new_max_speed
        self.current_speed = new_current_speed
        self.distance = new_distance

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.current_speed * hours

    def get_info(self):
        return {
            "reg_num": self.reg_num,
            "max_speed": self.max_speed,
            "current_speed": self.current_speed,
            "distance": self.distance
        }

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for each_car in self.cars:
            random_change = random.randint(-10, 15)
            each_car.accelerate(random_change)
            each_car.drive(1)

    def print_status(self):
        data = []
        for each_car in self.cars:
            data.append(each_car.get_info())

        print(tabulate(data, headers = "keys", tablefmt = "fancy_grid"))

    def race_finished(self):
        for each_car in self.cars:
            if each_car.distance >= self.distance:
                return True

        return False

cars = []

for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(reg, max_speed)
    cars.append(car)

race = Race("Grand_Demolition_Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()

race.print_status()