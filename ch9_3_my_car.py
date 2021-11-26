from ch9_2_car import Car
from ch9_1_dog import Car,ElectricCar
import ch9_1_dog
from ch9_1_dog import ElectricCar as EC

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

my_beetle = ch9_1_dog.Car('volkswagen', 'beetle', 2019)
print(my_tesla.get_descriptive_name())
my_tesla = ch9_1_dog.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)