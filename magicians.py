#for循环
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print(f"Thank you, everyone. That was a great magic show!")

#case4-1
pizzas = ['pizza1','pizza2','pizza3']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print(f"I like {pizzas[0]}, {pizzas[1]}, {pizzas[2]}, I really love pizza!")
#case4-2
pets = ['dog','cat','bird']
for pet in pets:
    print(pet)
for pet in pets:
    print(f"A {pet} would make a great pet.")
print(f"Any of these animals would make a great pet!")

#创建数值列表
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

#case4-3
for num in range(1,21):
    print(num)
#case4-4
nums = list(range(1,1_000_001))
#for num in nums:
#    print(num)
#case4-5
nums = list(range(1,1_000_001))
print(min(nums))
print(max(nums))
print(sum(nums))
#case4-6
nums = list(range(1,20,2))
for odd in nums:
    print(odd)
#case4-7
nums = []
for num in range(3,31):
    if num%3==0:
        nums.append(num)
print(nums)
for num in nums:
    print(num)
#case4-8
cube_numbers = [value**3 for value in range(1,11)]
for cube_number in cube_numbers:
    print(cube_number)
#case4-9
cube_numbers = [value**3 for value in range(1,11)]

#切片
players = ['ceharls','martina','michael','florence','eli']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[0:5:2])

#历遍切片
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#case4-10
players = ['charles','martina','michael','florence','eli']
print("The first three items in the list are:")
print(players[:3])
print("Three items from the middle of the list are:")
print(players[1:4])
print("The last three items in the list are:")
print(players[-3:])
#case4-11
pizzas = ['pizza1','pizza2','pizza3']
friend_pizzas = pizzas[:]
friend_pizzas.append('pizza4')
print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza)
print("My friends's favorite pizzas are:")
for pizza in friend_pizzas[:]:
    print(pizza)
#case4-12
print("My favorite foods are:")
for food in my_foods[:]:
    print(food)
print("My friend's favorite foods are:")
for food in friend_pizzas[:]:
    print(food)