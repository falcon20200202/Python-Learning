# 9.1创建和使用类
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age。"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下。"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# case9-1
class Restaurant:
    """餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """餐馆信息"""
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        """正在营业"""
        print(f"The reataurant {self.restaurant_name} is opening.")

restaurant = Restaurant('name', 'type')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# case9-2
restaurant1 = Restaurant('name1', 'type1')
restaurant2 = Restaurant('name2', 'type2')
restaurant3 = Restaurant('name3', 'type3')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# case9-3
class User:
    """用户"""
    def __init__(self, first_name, last_name):
        """初始化属性first_name和last_name。"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """用户摘要"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Full name: {full_name}")

    def greet_user(self):
        """用户问候"""
        print(f"Hello, {self.first_name} {self.last_name}")

user1 = User('first1', 'last1')
user1.describe_user()
user1.greet_user()

user2 = User('first2', 'last2')
user2.describe_user()
user2.greet_user()

# 9.2使用类和实例
print("\n9.2 使用类和实例:")
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model =model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_time = f"{self.year} {self.make} {self.model}"
        return long_time.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# case9-4
class Restaurant:
    """餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆信息"""
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        """正在营业"""
        print(f"The reataurant {self.restaurant_name} is opening.")

    def set_number_served(self, value):
        """设置值"""
        self.number_served = value

    def increment_number_served(self, increment_value):
        """增加值"""
        self.number_served += increment_value

restaurant = Restaurant('name', 'type')
print(restaurant.number_served)
restaurant.set_number_served(23)
print(restaurant.number_served)
restaurant.increment_number_served(100)
print(restaurant.number_served)

# case9-5
class User:
    """用户"""
    def __init__(self, first_name, last_name):
        """初始化属性first_name和last_name。"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """用户摘要"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Full name: {full_name}")

    def greet_user(self):
        """用户问候"""
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """属性值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """属性值重置0"""
        self.login_attempts = 0

user = User('first', 'last')
i = 0
while i < 3:
    user.increment_login_attempts()
    i += 1
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

# 9.3继承
class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有邮箱。"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print("\n9.3.4 将实例用作属性:")
class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size ==75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# case9-6
class IceCreamStand(Restaurant):
    """冰激凌小店。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Mango', 'Apple']

    def describe_icecreamstand(self):
        """各种口味。"""
        print(self.flavors)

icecream = IceCreamStand('name', 'type')
icecream.describe_icecreamstand()

# case9-7
class Admin(User):
    """管理员。"""

    def __init__(self, first_name, last_name):
        """初始化父类"""
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """显示"""
        for privilege in self.privileges:
            print(privilege)

admin = Admin('first', 'last')
admin.show_privileges()

# case9-8
class Privileges:
    """小类"""
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        """初始化属性privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """显示"""
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """管理员。"""

    def __init__(self, first_name, last_name):
        """初始化父类"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

admin = Admin('first', 'last')
admin.privileges.show_privileges()

# case9-9
class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size ==75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """检查电瓶容量。"""
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# 9.5Python标准库
from random import randint
print(randint(1,6))
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# case9-13
from random import randint
class Die:
    """骰子"""
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        x = 1
        while x <= 10:
            print(randint(1, self.sides))
            x += 1

six = Die(6)
six.roll_die()

ten = Die(10)
ten.roll_die()

twenty = Die(20)
twenty.roll_die()

# case9-14
from random import choice
choices = ['0','1','2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
selected = []
x = 1
while x <= 4:
    selected.append(choice(choices))
    x += 1
print(selected)
print(f"If numbers are {selected[0]}{selected[1]}{selected[2]}{selected[3]}, you won the prize! ")

# case9-15
choices = ['0','1','2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
selected = []
my_ticket = ['0', '3', '2', '7']
i = 0
while my_ticket != selected:
    selected = []
    x = 1
    while x <= 4:
        selected.append(choice(choices))
        x += 1
    i += 1
print(i)
