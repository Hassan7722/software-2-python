from T9 import Car

# Exercise 2
car2 = Car("ABC-123", 142)

car2.accelerate(30)
car2.accelerate(70)
car2.accelerate(50)

print(car2.current_speed)

car2.accelerate(-200)
print(car2.current_speed)