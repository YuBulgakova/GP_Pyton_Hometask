#1
def my_func1 ():
    try:
        num1 = int(input('Enter number 1:'))
        num2 = int(input('Enter number 1:'))
    except ValueError:
        print('Numbers only!')
        return
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        print('Деление на ноль (Zero Division)!')
    # except ArithmeticError:
    #     print('Arithmetic Error')

result = my_func1()
if result: #чтобы не выводился None в случае попадания в except
        print(result)

#2
def profile_func (Name, Surname, BYear,Email, Tel, City='Moscow'):
    profile =' '.join([Name, Surname, BYear, City, Email, Tel])
    return profile

print(profile_func (Name ='Anna',Surname = 'Ivanova',BYear = '1990', Email ='Email@google.com',Tel = '123'))

#3
def my_func3(num1, num2, num3):
    try:
        list = [num1, num2, num3]
        result = 0
        for num in list:
             if num != min(list):
                 result+=num
        return result
    except TypeError:
        print('Numbers only!')
        return

#4 via **
def my_func_4_1(x,y):
    try:
        result = abs(float(x))**int(y)
        return result
    except ZeroDivisionError:
        print('Деление на ноль (Zero Division)!')

print(my_func_4_1(2,-3))


#via cycle
def my_func_4_2(x,y):
    try:
        result = 1
        for i in range(abs(y)):
            result = result/x
        return result
    except ZeroDivisionError:
        print('Деление на ноль (Zero Division)!')

print(my_func_4_2(2,-3))