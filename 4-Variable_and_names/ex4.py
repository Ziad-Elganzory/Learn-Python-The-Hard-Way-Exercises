# Number of cars
cars = 100
# Space in a car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Number of cars not driven
cars_not_driven = cars - drivers
# Number of cars driven
cars_driven = drivers
# Carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
# Study Drills
# The error message because there's no variable named car_pool_capacity, it should be carpool_capacity.
#1. It's not necessary , both are the same.
#2. Done
#3. Done
#4. Done

