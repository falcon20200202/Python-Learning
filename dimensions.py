#定义元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#以下会报错
#dimensions[0] = 250

my_t = (3,)

#遍历元组
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#修改元组变量
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,50)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#case4-13
foods = ('food1','food2','food3','food4','food5')
for food in foods:
    print(food)
#foods[0]='food6'
foods=('food6','food7','food3','food4','food5')
for food in foods:
    print(food)