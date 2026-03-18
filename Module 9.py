import random


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


# Exercise 1
car1 = Car("ABC-123", 142)

print(car1.reg_num)
print(car1.max_speed)
print(car1.current_speed)
print(car1.distance)

# Exercise 2
car2 = Car("ABC-123", 142)

car2.accelerate(30)
car2.accelerate(70)
car2.accelerate(50)

print(car2.current_speed)

car2.accelerate(-200)
print(car2.current_speed)

# Exercise 3
ford = Car("ABC-123", 142, 60, 2000)
ford.drive(1.5)

print(ford.distance)

# Exercise 4
cars = []

for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(reg, max_speed)
    cars.append(car)

while True:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

    for car in cars:
        if car.distance >= 10000:
            break
    else:
        continue
    break

for car in cars:
    print(car.reg_num, car.max_speed, car.current_speed, int(car.distance))
