import math

print('Введите коэфициенты для уравнения')
print('ax^4 + bx^2 + c = 0: ')
while True:
    try:
        a=float(input("a - "))
        break
    except ValueError:
            continue
while True:
    try:
        b = float(input('b - '))
        break
    except ValueError:
            continue
while True:
    try:
        c = float(input('c - '))
        break
    except ValueError:
            continue

discr = b**2 - 4*a*c
print('Дискриминант D = ', discr)

if discr > 0:
    t1 = (-b + math.sqrt(discr)) / (2 * a)
    t2 = (-b - math.sqrt(discr)) / (2 * a)
    x1 = math.sqrt(t1)
    x2 = - math.sqrt(t1)
    x3 = math.sqrt(t2)
    x4 = - math.sqrt(t2)
    print(f'x1 = {x1:5f} ')
    print(f'x2 = {x2:5f} ')
    print(f'x3 = {x3:5f} ')
    print(f'x4 = {x4:5f} ')
elif discr == 0:
    t = (-b ) / (2 * a)
    x1 = math.sqrt(t)
    x2 = - math.sqrt(t)
    print('x1 = ', x1)
    print('x2 = ', x2)
else:
    print('Корней нет')


