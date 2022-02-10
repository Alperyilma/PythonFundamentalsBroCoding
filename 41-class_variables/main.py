from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2021,"red")

car_1.wheels = 2
Car.wheels = 4


print(car_1.wheels) #2
print(car_2.wheels) #4

print(Car.wheels) #4








