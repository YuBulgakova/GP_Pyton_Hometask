# 1
# with open('lesson5-1.txt', 'w', encoding='utf-8') as f:
#     while True:
#         line = input('Enter some words#1')
#         if line == '':
#             break
#         f.write(line+'\n')

# 2

# with open(r'lesson5-2_man.txt', 'a', encoding='utf-8') as f:
#     try:
#         while True:
#             line = input('Enter some words#2')
#             if line == '':
#                 break
#             f.write(line+'\n')
#     except IOError:
#         print('The file is not founded')

with open(r'lesson5-2_man.txt', 'r', encoding='utf-8') as f:
    n = 0
    for line in f:
        n += 1
        print(f'It is {len(line.split())} words in line # {n} ')

# 3
sum = 0
try:
    with open(r'Employees.txt', encoding='utf-8') as f:
        for line in f:
            l = line.split()
            surname = l[0]
            salary = float(l[1])
            sum += salary
            n += 1
            if salary < 20000:
                print('Получает менее 20 тыс.: ',surname)
        med_sal = round(sum / n, 2)
        print(f'Medium salary = {med_sal}')
except IOError:
    print(r'File doesnt exist. Check the file name')

# 4
numbers_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
with open(r'lesson5-4_man.txt', encoding='utf-8') as f:
    with open('lesson5-4.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            l = line.split()
            for key, val in numbers_dict.items():
                if key == l[0].lower():
                    new_line = ' '.join([val, l[1], l[2], '\n'])
                    # print(new_line)
                    f2.write(new_line)

# 5
from random import randint

with open('lesson5-5.txt', 'w+', encoding='utf-8') as f:
    for i in range(10):
        f.write(f'{randint(1, 100)} ')

    f.seek(0)
    list1 = f.read().split()
    print( list1)
    summa = 0
    for el in list1:
        summa += int(el)
    print(summa)

#6
subj_dict = {}

with open('lesson5-6_Subjects.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list6=line.split()
        print(list6)
        new_list = []
        summa = 0
        for el in list6:
             for symb in el:
                 if ord(symb) not in range(48,57):
                     el=el.replace(symb,'')
             if len(el) > 0:
                new_list.append(el) # в new_list хранятся только числа по каждой строке
        for el in new_list:
            summa +=int(el)

        subj_dict[list6[0]]=summa

    for item in subj_dict.items():
        print('Название предмета и количество занятий: ',item)

#7
sum_profit = 0
n=0
firms={}
average_profit = {}
new_list = []

with open('lesson5-7_firms.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list7=line.split()
        print(list7)
        profit = int(list7[2])- int(list7[3])
        if profit >0:
            sum_profit +=profit
            n +=1
        firms[list7[0]]=profit

average_profit['average_profit'] = round(sum_profit/n)
new_list.append(firms)
new_list.append(average_profit)
print('Firms list: ', list(new_list))
