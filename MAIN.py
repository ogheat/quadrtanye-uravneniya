print(('Уравнение a*x^2+b*x+c=0'))
a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
d = b**2 - 4*a*c
print('Дискриминант =', d)
if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / (2 * a)
    print('x =', x)
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 =', x1)
    print('x2 =', x2)