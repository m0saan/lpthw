cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("there are cars availible.")
print ("There are only ", drivers , "drivers avalible.")
print ("There will be ", cars_not_driven, "empty cars to day.")
print ("We can transport", carpool_capacity, "people to day.")
print ("We have", passengers, "to carpool today.")
print ("We have to put about ", average_passengers_per_car, "in each car")