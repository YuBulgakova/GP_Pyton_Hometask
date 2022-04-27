# 1
from random import randint


class Matrix:
    def __init__(self, li, a=0, b=0):
        # li - список списков
        # a - кол-во элементов в строке
        # b - кол-во элементов в столбце
        self.li_m = li
        if self.li_m == 'rand':  # если пользователь не передает список, а передает значение rand, создаем значения раодомом
            self.li = []
            self.li_m = []
            for _ in range(b):
                self.li = []
                for _ in range(a):
                    i = randint(1, 9)
                    self.li.append(i)
                self.li_m.append(self.li)

    #        print(self.li_m)  # печать для проверки

    def __str__(self):
        s1 = ''
        for i in range(len(self.li_m)):
            for j in range(len(self.li_m[i])):
                s1 += str(self.li_m[i][j]) + ' '
                if j == len(self.li_m[i]) - 1:
                    s1 += '\n'

        return s1

    def __add__(self, other):
        print(f'Matrix addition: ')
        li_sum = []
        li_sum_m = []

# проверяем число строк и столбцов в двух матрицах:
        if len(self.li_m) > len(other.li_m):
            return 'The matrices are not equal!'
        elif len(self.li_m) < len(other.li_m):
            return 'The matrices are not equal!'
        else:
            if len(self.li_m[0]) > len(other.li_m[0]):
                return 'The matrices are not equal!'
            elif len(self.li_m[0]) < len(other.li_m[0]):
                return 'The matrices are not equal!'
            else:
# складываем матрицы:
                for i in range(min(len(self.li_m), len(other.li_m))):
                    li_sum = []
                    for j in range(min(len(self.li_m[i]), len(other.li_m[i]))):
                        sum = self.li_m[i][j] + other.li_m[i][j]
                        li_sum.append(sum)
                    li_sum_m.append(li_sum)
                return Matrix(list(li_sum_m))


mx_a = Matrix('rand', 4, 4)
mx_b = Matrix('rand', 4, 4)
print(mx_a)
print(mx_b)
mx_c = mx_a + mx_b
print(mx_c)

#2
from abc import ABC, abstractmethod

class Clothes (ABC):
    @abstractmethod
    def clothcalc (self):
        pass

class Coat(Clothes):
   def __init__(self, size):
        self.__size = size

   @property
   def size(self):
       return self.__size

   @size.setter
   def size(self, size):
       if size <40:
           self.__size = 40
       elif size > 58:
           self.__size = 58
       else:
        self.__size = size


   def clothcalc(self):
        cloth = round(self.__size/ 6.5 + 0.5,2)
        return cloth

class Suit(Clothes):
   def __init__(self, height):
        self.__h = height

   def clothcalc(self):
        cloth = round(2*self.__h + 0.3, 2)
        return cloth

c1 = Coat(50)
print(c1.clothcalc())

print(c1.size)
c1.size = 44
print(c1.size)

s1 = Suit(180)
print(s1.clothcalc())

#3
class Cell:
    def __init__(self, nucl_num):
        self.nucl = nucl_num

    def __str__(self):
        return (f'Nucleus number: {self.nucl}')

    def __add__ (self, other):
        return Cell(self.nucl +other.nucl)

    def __sub__(self, other):
        if self.nucl > other.nucl:
            return Cell(self.nucl - other.nucl)
        else:
            return ('The number is nedative')

    def __mul__(self, other):
        return Cell(self.nucl * other.nucl)

    def __truediv__(self, other):
        return Cell(self.nucl // other.nucl)

    def make_order(self, cell_num):
        for i in range(self.nucl// cell_num):
            print('*' * cell_num)
        print('*' * (self.nucl% cell_num))

c1 = Cell(15)
c2 = Cell(13)
print(c1+c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
c1.make_order(5)
c2.make_order(5)





