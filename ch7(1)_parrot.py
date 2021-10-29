# 7.1 函数input()
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

print("\n7.1.1 编写清晰的程序:")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}")

print("\n7.1.2 使用int()来获取数值输入:")
age = input("How old are you? ")
age = int(age)
print(age >= 18)

print("\n7.1.3 求模运算符:")
print(4 % 3)
print(5 % 3)
print(6 % 3)
# 判断奇偶
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# case7-1
car = input("Whitch car do you want? ")
print(f"Let me see if I can find you a {car}.")

# case7-2
num = input("How many people? ")
num = int(num)
if num > 8:
    print("There are no empty seats.")
else:
    print("Available seats.")

# case7-3
num = input("Enter a number, and I'll tell you if it's a number is an integral multiple of ten: ")
num = int(num)
if num % 10 == 0:
    print(f"{num} is an integral multiple of ten.")
else:
    print(f"{num} is not an integral multiple of ten.")