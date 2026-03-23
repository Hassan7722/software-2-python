from E10 import Building

b = Building(bottom_floor=1, top_floor=10, number_of_elevators=5)
b.run_elevator(new_elevator=4, target_floor=9)
b.run_elevator(new_elevator=1, target_floor=8)
