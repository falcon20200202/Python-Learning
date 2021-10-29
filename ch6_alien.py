# 字典示例
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2使用字典
print("6.2.1 访问字典中的值:")
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print("\n6.2.2 添加键值对:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n6.2.3 创建空字典:")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("\n6.2.4 修改字典中的值:")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")
# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3
# 新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")

print("\n6.2.5 删除键值对:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print("\n6.2.6 由类似对象组成的字典:")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("\n6.2.7 访问值:")
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('point', 'No point value assigned.')
print(point_value)

# case6-1
person = {'first_name': 'first_name', 'last_name': 'last_name', 'age': 21, 'city': 'city'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# case6-2
nums = {
    'name1': 1,
    'name2': 2,
    'name3': 3,
    'name4': 4,
    'name5': 5,
}

print(f"Name1's favorite num is {nums['name1']}.")

# case6-3
vocabulary = {
    '列表': '用方括号[]表示列表，并用逗号分隔其中的元素',
    '元组': '不可变的列表称为元组',
    '字典': '字典是一系列键值对',
}
print(f"列表 : {vocabulary['列表']}.")
print(f"元组 : {vocabulary['元组']}")
print(f"字典 : {vocabulary['字典']}")

# 6.3遍历字典
print("\n6.3.1 遍历所有键值对:")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n6.3.2 遍历字典中的所有键:")
# exp1
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# exp2
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n6.3.3 按特定顺序遍历字典中的所有键:")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n6.3.4 遍历字典中的所有值:")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

# case6-4
vocabulary = {
    '列表': '用方括号[]表示列表，并用逗号分隔其中的元素',
    '元组': '不可变的列表称为元组',
    '字典': '字典是一系列键值对',
}
vocabulary['set'] = '不重复'
for key, value in vocabulary.items():
    print(f"{key}:{value}.")


# case6-5
rivers = {
    'Yangtze River': 'China',
    'Yellow River': 'China',
    'nile': 'egypt',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# case6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

old_name = favorite_languages.keys()
names = ['jen', 'sarah', 'edward', 'phil', 'name5', 'name6']
for name in names:
    if name in old_name:
        print(f"{name.title()}, thank you!")
    else:
        print(f"{name.title()}, Welcome to the survey.")

# 6.4嵌套
print("\n6.4.1 字典列表:")
# exp1
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# exp2
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 对列表中部分字典进行修改
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
# 显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")

print("\n6.4.2 在字典中存储列表:")
# exp1
# 存储所点披萨的信息。
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点披萨
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    # print(f"\t{topping}")

# exp2
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

print("\n6.4.3 在字典中存储字典:")
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# case6-7
person1 = {'first_name': 'first_name1', 'last_name': 'last_name1', 'age': 21, 'city': 'city1'}
person2 = {'first_name': 'first_name2', 'last_name': 'last_name2', 'age': 21, 'city': 'city2'}
person3 = {'first_name': 'first_name3', 'last_name': 'last_name3', 'age': 21, 'city': 'city3'}
people = [person1, person2, person3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}'s informations are:"
    print(full_name)
    print(person['age'])
    print(person['city'])

# case6-8
pet1 = {
    'pet_name': 'pet1',
    'owner_name': 'owner1',
}
pet2 = {
    'pet_name': 'pet2',
    'owner_name': 'owner2',
}
pets = [pet1, pet2]
for pet in pets:
    print(f"{pet['pet_name']} is own to {pet['owner_name']}")

# case6-9
favorite_places = {
    'A': ['d', 'e'],
    'B': ['f'],
    'C': ['g', 'h']
}
for key, values in favorite_places.items():
    print(f"{key}'s favorite places are:")
    for value in values:
        print("\t" + value)

# case6-10
nums = {
    'name1': [1,3],
    'name2': [2,5,7,8],
    'name3': [3,2,5,6],
    'name4': [46,4,6,8],
    'name5': [5,3,1,7],
}
for key, values in nums.items():
    print(f"{key}'s favorite numbers are:")
    for value in values:
        print(f"\t{value}")

# case6-11
cities = {
    'city1':{
        'country': 'country1',
        'population': 30,
        'fact': 'fact1',
    },
    'city2':{
        'country': 'country2',
        'population': 50,
        'fact': 'fact2',
    },
    'city3':{
        'country': 'country3',
        'population': 100,
        'fact': 'fact3',
    },
}
for city, city_info in cities.items():
    print(f"{city.title()}'s information are:")
    for key, info in city_info.items():
        print(f"\t{key.title()}: {info}")