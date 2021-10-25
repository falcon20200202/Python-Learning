#if
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#相等运算符
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

#与或
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))

#检查特定值是否包含在列表中
print("检查特定值是否包含在列表中:")
requested_toppings = ['mushrooms','onions','pineapple']
print(f"\n{'mushrooms' in requested_toppings}")
print('pepperoni' in requested_toppings)

print("检查特定值是否不包含在列表中:")
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

#if语句
print("\nif:")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("\nif-else:")
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print("\nif-elif-else:")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

#case5-3
alien_color = 'green'
if alien_color == 'green':
    print("5 points!")
alien_color = 'red'
if alien_color == 'green':
    print("5 points!")

#case5-4
alien_color = 'green'
if alien_color == 'green':
    print("5 points!")
else:
    print("10 points!")

alien_color = 'red'
if alien_color == 'green':
    print("5 points!")
else:
    print("10 points!")

#case5-5
alien_color = 'green'
if alien_color == 'green':
    print("5 points!")
elif alien_color == 'yellow':
    print("10 points!")
else:
    print("15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("5 points!")
elif alien_color == 'yellow':
    print("10 points!")
else:
    print("15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("5 points!")
elif alien_color == 'yellow':
    print("10 points!")
else:
    print("15 points!")

#case5-6
age = 22
if age < 2:
    print("This is a baby.")
elif (age >=2 and age <4):
    print("This is a child.")
elif (age >=4 and age <13):
    print("This is a children.")
elif (age >=13 and age <20):
    print("This is a teenager.")
elif (age >=20 and age <65):
    print("This is a adult.")
else:
    print("This is a aged.")

#case5-7
favorite_fruits = ['fruit1','furit2','fruit3']
fruit = 'fruit3'
if fruit in favorite_fruits:
    print("You really like fruit3!")

#if语句处理列表
print("\n检查特殊元素:")
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding{requested_topping}.")
print("\nFinished making your pizza!")

print("\n确定列表不是空的:")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\n使用多个列表:")
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','fresh fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#case5-8
names = ['admin','name2','name3','name4','name5']
for name in names:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

#case5-9
names = []
if names:
    for name in names:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")

#case5-10
current_users = ['user1','user2','user3','user4','user5']
new_users = ['user1','user6','user7','user8','user9']
current_users_2 = []
for current_user in current_users:
    current_users_2.append(current_user.lower())
for user in new_users:
    if user.lower() in current_users_2:  #已占用
        print("Please use a new name.")
    else:                                #未占用，可用
        print(f"{user} is available!")

#case5-11
nums = list(range(1,10))
print(nums)
for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num ==2:
        print(f"{num}nd")
    else:
        print(f"{num}th")