# 1
list = [123, 'd', 'ball', 5.5, None, [1, 2, 5], True, 5]

for item in list:
    print(type(item))

# 2
list2 = []

for i in range(5):
    item = input('Enter item: ')
    list2.append(item)

print(list2)

for i in range(len(list2)):
    if i % 2 != 0:
        list2[i - 1], list2[i] = list2[i], list2[i - 1]
print(list2)

# 3
# via dict:

seasons = {'winter': ['1', '2', '12'], 'spring': ['3', '4', '5'], 'summer': ['6', '7', '8'], 'fall': ['9', '10', '11']}

month = input('Enter month: ')

for el in seasons:
    if month in seasons[el]:
        print(el)

# via list:
seasons = ['winter', 'spring', 'summer', 'fall']
months = [['1', '2', '12'], ['3', '4', '5'], ['6', '7', '8'], ['9', '10', '11']]

month = input('Enter month: ')

for i in range(len(months)):
    if month in months[i]:
        print(seasons[i])

# 4
line = input('Enter the line')

result = line.split()

for ind, el in enumerate(result):
    print(ind, el[:10])

# 5
my_list = [7, 5, 3, 3, 2]
number = int(input('Enter the number: '))

for i in range(len(my_list)):
    if number == my_list[i]:
        my_list.insert(i + 1, number)
        break
    elif number > max(my_list):
        my_list.insert(0, number)
    elif number < min(my_list):
        my_list.insert(len(my_list) + 1, number)
        break
print(my_list)

#6*
old_list = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
new_list = []

# отрезаем элементы с нумерацией:
for i in range(len(old_list)):
    new_list.append(old_list[i][1])

#print(list(new_list))  # печать для проверки

result = {}

for i in range(len(new_list)):
    el = new_list[i]  # присваиваем в переменную словарь (каждый эл-т списка в цикле)
    #print(el, type(el)) - проверяем вывод каждого словаря и его тип
    for key, val in el.items():
        if key not in result.keys():
            result.update(el)

for key in result.keys():
    val_list = []
    for i in range(len(new_list)):
        el = new_list[i]
        for key1, val1 in el.items():
            if key1 == key and val1 not in val_list:
                val_list.append(val1)
    result[key] = val_list

print('*' * 30)
print(dict(result))

