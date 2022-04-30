# # 1
# class Date():
#     def __init__(self, day, month, year):
#         self.d = int(day)
#         self.m = int(month)
#         self.y = int(year)
#         Date.date_valid(self.d, self.m, self.y)
#
#     #        print(f'd = {self.d}, m = {self.m}, y = {self.y}')
#
#     @classmethod
#     def set_info(cls, data):
#         d, m, y = data.split('-')
#         return cls(d, m, y)
#
#     @staticmethod
#     def date_valid(day, month, year):
#         if year < 1990 or year > 2100:
#             print(f'The year {year} is incorrect')
#         else:
#             if month < 1 or month > 12:
#                 print(f'The month {month} is incorrect')
#             else:
#                 if day < 1:
#                     print(f'The day {day} is incorrect')
#                 elif month % 2 == 0 and day > 30:
#                     print(f'The date {day}.{month} is incorrect combination')
#                 elif month % 2 != 0 and day > 31:
#                     print(f'The date {day}.{month} is incorrect combination')
#                 else:
#                     print(f'day = {day}, month = {month}, year = {year}')
#
#
# date1 = '10-01-2022'
# d1 = Date.set_info(date1)
# Date.date_valid(31, 3, 2022)
#
# #2
# class OwnError(Exception):
#     def __init__(self, txt):
#        self.txt = txt
#
# try:
#     num_a = int(input('num_a:'))
#     num_b = int(input('num_b:'))
#     if num_b ==0:
#         raise OwnError('Zerro division Error!')
# except ValueError:
#     print('Numbers only!')
# except OwnError as err:
#     print(err)
# else:
#     res = num_a / num_b
#     print(f'result: {res}')
# finally:
#     print('end')
#
# #3
# li = []
# el = 0
# while True:
#     if el == 's':
#         break
#     try:
#         el = input('Enter the number: ')
#         if el not in '0123456789':
#             raise OwnError('Numbers only!')
#     except OwnError as err:
#         print(err)
#     else:
#         li.append(int(el))
#
# print(list(li))

#7
class Comlex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Comlex_number(self.a + other.a, self.b +other.b)

    def __str__(self):
        return f'{self.a}+{self.b}*i'

    def __mul__(self, other):
        return Comlex_number(self.a*other.a - self.b*other.b, self.a* other.b + self.b*other.a)

z1 = Comlex_number(-7,4)
z2 = Comlex_number(-12,2)
print(z1)
print(z2)
print(z1+z2)
print(z1*z2)
