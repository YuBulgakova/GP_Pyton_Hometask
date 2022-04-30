# 4, 5, 6

size_dict = {'s':3, 'm':3.5, 'l': 4}
prin_li = ['Abstraction', 'Apple', 'Snoopy', 'Miccy Mouse']

class Clothes():
    name = None
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Clothes.count = 0


    def sewing(self, mat):
        quant_per_item = size_dict[self.size]
        mat.mat_count(quant_per_item)
        if Clothes.count == 1:
            print(f'The item is sewing...\n {self.color} {self.name} is ready! Size: {self.size}\n material left: {mat.q}')
        else:
            print('The item can"t be sewed')


class Hoodie(Clothes):
    name = 'Hoodie'
    c_count = 0

    def __init__(self, size, color, printt, warm):
        Clothes.__init__(self, size, color)
        self.pr = printt
        self.warm = warm

    def sewing(self, mat):
        Clothes.sewing(self, mat)
        if Clothes.count == 1:
            Hoodie.c_count +=1
        print(f'Item quantity: {Hoodie.c_count}')


class Joggers(Clothes):
    name = 'Joggers'
    c_count = 0
    def __init__(self, size, color, warm):
        Clothes.__init__(self, size, color)
        self.warm = warm

    def sewing(self, mat):
        Clothes.sewing(self, mat)
        if Clothes.count == 1:
            Joggers.c_count +=1
        print(f'Item quantity: {Joggers.c_count}')

class T_shirt(Clothes):
    name = 'T_shirt'
    c_count = 0

    def __init__(self, size, color, printt):
        Clothes.__init__(self, size, color)
        self.pr = printt

    def sewing(self, mat):
        Clothes.sewing(self, mat)
        if Clothes.count == 1:
            T_shirt.c_count +=1
        print(f'Item quantity: {T_shirt.c_count}')


class Material():
    def __init__(self, color, quantity):
        self.color = color
        self.q = quantity

    def mat_count(self, quant_per_item):
        try:
            print('*' * 20)
            print(f'Checking material stock... {self.q}m')
            if self.q < quant_per_item:
                raise No_mat(f'Not enough material! {self.q}m')
        except No_mat as err:
            print(err)
        else:
            self.q -= quant_per_item
            Clothes.count = 1

class No_mat(Exception):
    def __init__(self, txt):
        self.txt = txt

m_r = Material('red', 100)
h1 = Hoodie('m', 'red', None, False)
h1.sewing(m_r)

m_b = Material('blue',7)
h2 = Hoodie('m', 'blue', prin_li[1], True)
h2.sewing(m_b)
h3 = Hoodie('m', 'blue', prin_li[2], True)
h3.sewing(m_b)
h3 = Hoodie('m', 'blue', prin_li[3], True)
h3.sewing(m_b)

j1 = Joggers('s', 'blue', True)
j1.sewing(m_b)

t1 = T_shirt('l', 'blue', True)
t1.sewing(m_b)


