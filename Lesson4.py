# 1
from sys import argv
from functools import reduce

prod_in_hours, rate, bonus = map(int, argv[1:])
salary = (prod_in_hours * rate) + bonus

print(f'Salary is: {salary}')

# 2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list[i] for i in range(1, len(list)) if list[i] > list[i - 1]]
print(new_list)

# 3
list3 = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(list3)

# 4
list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list4 if list4.count(el) == 1]
print(new_list)

# 5
list5 = [el for el in range(100, 1001) if el % 2 == 0]
def func_5(a,b):
    return a*b

result = reduce(func_5,list5)
print(result)