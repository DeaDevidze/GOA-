# Creating a list of friends
friends = ["mari", "ano", "dachi", "nini", "luka"]

print(friends[0]) 
print(friends)

# Changing the name at index 3 to a new name
friends[3] = "Irakli"
print(friends)
print(len(friends))

# Creating a list of cars
cars = ["Honda", "Toyota", "BMW", "Mercedes"]
def add_car(car):
    cars.append(car)
# a new car
add_car("Tesla")
print(cars)


numbers = [10, 20, 30, 40, 50]
numbers[0] = 50
total = numbers[0] + numbers[-1]
print(total)
