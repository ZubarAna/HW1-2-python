'''
1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
*Пример:*

- 6 -> да
- 7 -> да
- 1 -> нет
'''
'''
n = int(input("Введите цифру от 1 до 7: "))
if 6 <= n <=7:
    print("ДА")
elif 0 <= n <=5:
    print("НЕТ")
else:
    print('Попробуй еще раз')
    '''
'''1 По двум заданным числам проверить является ли одно квадратом
второго.'''
'''
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a**2 == b:
    print("Число", b, "является квадратом числа", a)
elif b**2 == a:
    print("Число", a, "является квадратом числа", b)
else:
    print("Число", b, "является квадратом числа", a, "и", "число", a, "является квадратом числа", b)
    '''
'''2 Найти максимальное из пяти чисел.'''
'''
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвертое число: "))
e = int(input("Введите пятое число: "))
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if d > mx:
    mx = d
if e > mx:
    mx = e
print("Максимальное число -", mx)
'''
'''3 Вывести на экран числа от -N до N.'''
'''
n = int(input("Введите число N: "))
for i in range(-n, n+1):
    print(i, end = ',')
    '''
'''4 Показать первую цифру дробной части числа.'''
'''
n = float(input("Введите вещественное число: "))
a = int((n*10)%10)
print(a)
'''
'''5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30'''
'''
n = int(input("Введите число: "))
if n % 30 == 0:
    print("Число кратно 30, попробуй еще раз")
elif n % 5 == 0 and n % 10 == 0:
    print("Число", n, "кратно 5 и 10")
elif n % 15 == 0:
    print("Число", n, "кратно 15")
else:
    print("Не кратно 5 и 10 или 15")
    '''
'''6 Дано число обозначающее день недели. Вывести его название и
указать является ли он выходным.'''
'''
n = int(input("Введите число: "))
while not 1 <= n <= 7:
    n = int(input("Введите число: "))
else:
    if n == 1:
        print("Понедельник - рабочий день")
    if n == 2:
        print("Вторник - рабочий день")
    if n == 3:
        print("Среда - рабочий день")
    if n == 4:
        print("Четверг - рабочий день")
    if n == 5:
        print("Пятница - рабочий день")
    if n == 6:
        print("Суббота - выходной день")
    if n == 7:
        print("Воскресенье - выходной день")
'''
'''7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.'''
'''
for x in (0, 1):
     for y in (0, 1):
         for z in (0, 1):
             left = not(x or y or z)
             right = not x and not y and not z
             # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
             print(f'x = {x}, y = {y}, z = {z}')
             print(left == right)
'''
'''8 Сообщить в какой четверти координатной плоскости или на какой
оси находится точка с координатами Х и У.'''
'''
x = float(input('Введите координату Х: '))
y = float(input('Введите координату У: '))
if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif x == 0 and y == 0:
    print('точка лежит в начале координат')
elif x == 0 and y != 0:
    print('точка лежит на оси X')
else:
    print('точка лежит на оси Y')

'''
'''9 Указав номер четверти прямоугольной системы координат, показать
допустимые значения координат для точек этой четверти.'''
'''
a = input('Введите номер четверти: ')
if a == '1':
    print('x > 0, y > 0')
elif a == '2':
    print('x < 0, y > 0')
elif a == '3':
    print('x < 0, y < 0')
elif a == '4':
    print('x > 0, y < 0')
else:
    print(a, '-ой четверти не существует')
'''
'''10 Найти расстояние между двумя точками пространства.'''
import math
ax = float(input('Введите координату x точки А: '))
ay = float(input('Введите координату y точки А: '))
az = float(input('Введите координату z точки А: '))
bx = float(input('Введите координату x точки Б: '))
by = float(input('Введите координату y точки Б: '))
bz = float(input('Введите координату z точки Б: '))
D = math.sqrt((ax - bx)**2 + (ay - by)**2+(az - bz)**2)
print(round(D, 3))
# test A(0, -3, 3), B(3, 1, 3). D = 5