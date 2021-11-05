# 8.4传递列表
def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print("\n8.4.1 在函数中修改列表:")
def print_models(unprinted_designs, completed_models):
    """
    模型打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)

# case8-9
def show_messages(texts):
    """文本消息"""
    for text in texts:
        print(text)

texts = ['this is the first message', 'this is the second message', 'this is the third message']
show_messages(texts)

# case8-10
def send_messages(texts,sent_messages):
    """文本转移"""
    while texts:
        current_text = texts.pop()
        print(current_text)
        sent_messages.append(current_text)
    return sent_messages

texts = ['this is the first message', 'this is the second message', 'this is the third message']
sent_messages = []
print(send_messages(texts, sent_messages))
print(texts)

# case8-11
def send_messages(texts,sent_messages):
    """文本转移"""
    while texts:
        current_text = texts.pop()
        print(current_text)
        sent_messages.append(current_text)
    return sent_messages

texts = ['this is the first message', 'this is the second message', 'this is the third message']
sent_messages = []
print(send_messages(texts[:], sent_messages))
print(texts)

# 8.5传递任意数量的实参
def make_pizza(*toppings):
    """概述要制作的比萨。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("\n8.5.1 结合使用位置实参和任意数量实参:")
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n8.5.2 使用任意数量的关键字实参:")
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# case8-12
def sandwiches(*sandwich):
    """sandwiches"""
    print(f"You ordered the following sandwiches:"
          f"\n\t{sandwich}")

sandwiches('sandwich1')
sandwiches('sandwich1', 'sandwich2')
sandwiches('sandwich1', 'sandwich2', 'sandwich3')

# case8-13
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('first_name', 'last_name', location='Country', field='field')
print(user_profile)

# case8-14
def make_car(manufacturer, model, **kwargs):
    """car"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)