bicycles = ['trek', 'cannondale', 'redline','specialized']
print(bicycles)
print(bicycles[0])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#case3-1
names = ['first','second','third','forth','fifth']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
#case3-2
print(f'{names[0]}, good moring!')
#case3-3
ways = ['walk','run','bicycle']
print(f"I would like to own a {ways[0]}.")

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'
motorcycles.remove('ducati')

#case3-4
dinner = ['first','second','third']
print(f"{dinner[0].title()}, would you like to have dinner with me? ")
#case3-5
print(f"{dinner[0].title()} can not attend")
dinner_cannot = dinner.pop(0)
dinner.insert(0,'forth')
print(f"{dinner[0].title()}, would you like to have dinner with me? ")
#case3-6
print(f"I found a bigger table! ")
dinner.insert(0,'fifth')
dinner.insert(2,'sixth')
dinner.append('seventh')
print(f"{dinner[0].title()}, would you like to have dinner with me? ")
#case3-7
print(f"I'm sorry to inform you that we can only invite two people to dinner because the new table didn't arrive in time. ")
dinner_cannot = dinner.pop(0)
print(f"{dinner_cannot.title()}, sorry, we can not have dinner together")
dinner_cannot = dinner.pop(0)
print(f"{dinner_cannot.title()}, sorry, we can not have dinner together")
dinner_cannot = dinner.pop(0)
print(f"{dinner_cannot.title()}, sorry, we can not have dinner together")
dinner_cannot = dinner.pop()
print(f"{dinner_cannot.title()}, sorry, we can not have dinner together")
print(f"{dinner[0].title()}, welcome!")
print(f"{dinner[1].title()}, welcome!")
del dinner[0]
del dinner[0]
print(dinner)

#3.3排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print(sorted(cars,reverse=True))

cars.reverse()
print(cars)

print("列表长度为：")
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
