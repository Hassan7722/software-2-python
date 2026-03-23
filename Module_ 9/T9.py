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