from T9 import Car
import random
from tabulate import tabulate

# Exercise 4
cars = []

for i in range(1,11):
    reg = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(reg, max_speed)
    cars.append(car)

race = True

while race:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.distance >= 10000:
            race = False

printable_cars = []
for car in cars:
    printable_cars.append(car.get_info())

table = tabulate(printable_cars, headers = "keys", tablefmt="fancy_grid")
print(table)