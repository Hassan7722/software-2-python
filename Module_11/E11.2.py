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

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, tank_volume):
        super().__init__(reg_num, max_speed)
        self.tank_volume = tank_volume

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.accelerate(100)
gasoline.accelerate(120)

electric.drive(3)
gasoline.drive(3)

print(electric.reg_num, electric.distance ,"Km" , electric.battery_capacity, "kWh")
print(gasoline.reg_num, gasoline.distance, "Km", gasoline.tank_volume, "liters")
