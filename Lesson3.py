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
    # except ValueError:
    #     print('Numbers only!')
    except ZeroDivisionError:
        print('Деление на ноль (Zero Division)!')
    # except ArithmeticError:
    #     print('Arithmetic Error')

print(my_func1())

#2
