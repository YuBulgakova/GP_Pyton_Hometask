# 1
name = 'Julia'
number = 10
tempriture = 36.6

print(f'name: {name}, number: {number}, tempriture: {tempriture}')

name = input('name: ')
number = input('number: ')
tempriture = input('tempriture: ')

print(f'name: {name}, number: {number}, tempriture: {tempriture}')

# 2
time = int(input('Enter time in seconds: '))

sec = time % 60
time = time // 60

min = time % 60
time = time // 60

print(f'{time}:{min}:{sec}')

# 3
number = int(input('Enter number (0-9): '))
result = number * 111 + number * 11 + number
print(result)

# 4
number = int(input('Enter number (integer, >0): '))
result = 0

while number:
    n = number % 10
    number = number // 10
    if n > result:
        result = n

print(result)

# 5
proceeds = float(input('enter proceeds: '))
costs = float(input('enter costs: '))
fin_result = proceeds - costs

if fin_result > 0:
    print(f'year profit is: {fin_result} rub')
else:
    print(f'year loss is: {fin_result} rub')

# 6
if fin_result > 0:
    rent = proceeds / costs
    employee_number = int(input('enter employee number: '))
    rent_per_employee = rent / employee_number
print(f'Rent is: {rent},  Rent per employee: {rent_per_employee}')

# 7
import math

day_1_distance = float(input('1st day distance: '))
day_N_distance = float(input('N day distance: '))
day_N = 1

while day_1_distance < day_N_distance:
    day_1_distance = round(day_1_distance * 1.1, 2)
    day_N += 1

print(f'На {day_N}й день спортсмен достиг результата — {day_1_distance} км')
