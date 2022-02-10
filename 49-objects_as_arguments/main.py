class Car:

    color = None

class Motorcyle:

    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcyle()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")

change_color(bike_1, "black")

print(car_1.color) #red
print(car_2.color) #white
print(car_3.color) #blue

print(bike_1.color) #black
