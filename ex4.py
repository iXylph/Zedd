cars = 100 #assigns the value 100 to cars
space_in_a_car = 4 #assigns the value 4 to space_in_a_car
drivers = 30 #assigns the value 30 to drivers
passengers = 90 #assigns the value 90 to passengers
cars_not_driven = cars - drivers #subtracts the value assigned to drivers from the value assigned from cars.
carpool_capacity = drivers * space_in_a_car
average_passengers_per_car = passengers / drivers

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." 