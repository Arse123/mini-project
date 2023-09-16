import sys

def arithmetic(x,op,y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "Неизвестная операция"

while True:
    x= float(input('Введи первое число:'))
    op = input('Операция:')
    y= float(input('Введи второе число:'))
    
    result = arithmetic(x, op, y)
    print(float(result))
    
    choice = input('Хотите продолжить? (y/n)')
    if choice.lower() != 'y':
        break

