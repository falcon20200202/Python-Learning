# while循环
print("\n7.2.1 使用while循环:")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n7.2.2 让用户选择何时退出:")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

print("\n7.2.3 使用标志:")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

print("\n7.2.4 使用break退出循环:")
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

print("\n7.2.5 循环中使用continue:")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# case7-4
prompt = "\nPlease enter the name of topping:"
prompt += "\n(Enter 'quit' when you are finished.)"
flag = True
while flag:
    topping = input(prompt)
    if topping == 'quit':
        flag = False
    else:
        print(f"We will attend the {topping}!")

# case7-5
prompt = "\nPlease enter your age:"
prompt += "\n(Enter '0' when you are finished.)"
while True:
    age = input(prompt)
    age = int(age)
    if age == 0:
        break
    elif age < 3:
        price = 0
    elif (age >= 3) and (age <= 12):
        price = 10
    elif age > 12:
        price = 15
    print(f"The price is {price}.")

# case7-6
prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.)"
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age <= 0:
            print("Please enter a right age:")
            continue
        elif age < 3:
            price = 0
        elif (age >= 3) and (age <= 12):
            price = 10
        elif age > 12:
            price = 15
        print(f"The price is {price}.")

# 7.3使用while循环处理列表和字典
print("\n7.3.1 在列表之间移动元素:")
# 首先，创建一个待验证用户列表
#    和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users =[]
# 验证每个用户，直到没有未验证用户为止。
#    将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)
# 显示所以已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("\n7.3.2 删除为特定值的所有列表元素:")
pets = ['dog', 'cat', 'dog', 'goldfish ', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

print("\n7.3.3 使用用户输入来填充字典:")
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答。
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # 将回答存储在字典中。
    responses[name] = response
    # 看看是否还有人要参与调查。
    repeat = input("Woule you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# case7-8
sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3']
finished_sandwichs = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwichs.append(sandwich)
print(finished_sandwichs)

# case7-9
sandwich_orders = ['sandwich1', 'pastrami', 'sandwich2', 'pastrami','sandwich3', 'pastrami']
finished_sandwichs = []
print("Pastrami has been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwichs.append(sandwich)
print(finished_sandwichs)

# case7-10
places = []
flag = True
while flag:
    places = input("If you could visit one place in the world, where would you go? ")
    print(places)
    repeat = input("Woule you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        break