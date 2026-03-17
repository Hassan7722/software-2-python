class Car:
    def __init__(self, new_reg_num, new_max_speed):
        self.reg_num = new_reg_num
        self.max_speed = new_max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.current_speed = self.current_speed + change

        # Current sped
        if self.current_speed < 0:
            self.current_speed = 0

        # Max_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed







"""ford = Car("ABC-123", 142)
ford.accelerate(30)
ford.accelerate(70)
ford.accelerate(50)

print(ford.current_speed)

ford.accelerate(-200)
print(ford.current_speed)"""

"""ford = Car("ABC-123", 142)
print(ford.reg_num)
print(ford.max_speed)
print(ford.current_speed)
print(ford.distance)"""

1