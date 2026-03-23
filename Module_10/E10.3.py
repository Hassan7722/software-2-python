from E10 import Building

b = Building(1, 10, 3)

b.run_elevator(1, 5)
b.run_elevator(2, 4)
b.run_elevator(3, 3)

print("FIRE ALARM")
b.fire_alarm()