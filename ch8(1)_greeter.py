# 函数
# 8.1定义函数
    # 无信息
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()
    # 传递信息
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")
greet_user('jesse')

# case8-1
def display_message():
    """本章学习内容"""
    print("In this chapter, we study functions. ")
display_message()

# case8-2
def favorite_book(title):
    """最喜欢的一本书"""
    print(f"One of my favorite books is {title}.")
favorite_book('Alice in Wonderland')

# 8.2传递实参
print("\n8.2.1 位置实参:")
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

print("\n8.2.2 关键字实参:")
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

print("\n8.2.3 默认值:")
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='whillie')
describe_pet(pet_name='whillie', animal_type='hamster')
describe_pet('whillie', 'hamster')

print("\n8.2.3 默认值.测试:")
# 经以下测试，得出结论：要把含有默认值的参数放在不含默认值的参数的后面，其余不含默认值的参数可为位置实参也可为关键字实参
def describe_pet(pet, pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}{pet}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet='1', pet_name='whillie')
describe_pet(pet_name='whillie', pet='1')
describe_pet('1', 'whillie')
describe_pet('whillie', '1')

def describe_pet(pet, pet_name, animal_type='dog', two = '2'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}{pet}{two}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('1', 'whillie', '3', '4')
describe_pet('1', 'whillie', '4', '3')

# case8-3
def make_shirt(size, words):
    """T恤"""
    print(f"This shirt is {size} size with {words} on it.")

make_shirt("m", "hello!")
make_shirt(size='l', words='hello!')

# case8-4
def make_shirt(size='l', words='"I love Python"'):
    """T恤"""
    print(f"This shirt is {size} size with {words} on it.")

make_shirt()
make_shirt(size='m')
make_shirt(words='"hello"')

# case8-5
def describe_city(city, country='Iceland'):
    """城市"""
    print(f"{city} is in {country}.")

describe_city('Reykjavik')
describe_city('Akureri')
describe_city('Harbin','China')

# 8.3返回值
print("\n8.3.1 返回简单值:")
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print("\n8.3.2 让实参变成可选的:")
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print("\n8.3.3 返回字典:")
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("\n8.3.4 结合使用函数和while循环:")
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# case8-6
def city_country(city, country):
    """城市所属国家"""
    sentence = f"{city}, {country}"
    return sentence

print(city_country('Santiago', 'Chile'))

# case8-7、case8-8
def make_album(name, Album_name, num=None):
    """歌手与专辑"""
    if num:
        album = {'name':name, 'Album_name':Album_name, 'num': num}
    else:
        album = {'name': name, 'Album_name': Album_name}
    return album

while True:
    print("\nPlease tell me a name and a album")
    print("(enter 'q' at any time to quit)")
    prompt_num = "How many songs in it: "
    prompt_num += "\n(enter 'n' if you do not want to enter.)"
    name = input("name: ")
    if name == 'q':
        break
    album = input("album: ")
    if album == 'q':
        break
    num = input(prompt_num)
    if num == 'q':
        break
    elif num == 'n':
        num = None
    else:
        num = int(num)
    print(make_album(name, album, num))
