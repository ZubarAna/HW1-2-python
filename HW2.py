'''1 Подсчитать сумму цифр в вещественном числе.'''
'''
n = input("Введите вещественное число: ")
sum = 0
for i in n:
    if i.isdigit():
        sum += int(i)
print(f'Cуммa цифр в вещественном числе {n} = {sum}')
'''
'''2 Написать программу получающую набор произведений чисел от 1 до N.
Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]'''
'''
N = int(input('Введите число N: '))
result = []
x = 1
for i in range(1, N + 1):
    result.append(x)
    x *= i + 1
print(result)
'''
'''3 Задать список из n чисел последовательности (1+ 1/n)**n и вывести на экран их сумму.'''
'''
n = int(input('Введите число N: '))
result = []
sum = 0
for i in range(1, n + 1):
    x = (1 + 1/ i) ** i
    sum += x
    result.append(x)
print(result)
print()
print(f'Сумма {n} чисел последовательности равна {sum}')
'''
'''4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
positions = [1, 3, 6]).'''
'''
from random import Random, randint

N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
print(numbers)

print(f'Введите позиции (номер позиции от 0 до {N-1})')
print('Для перехода к следующей позиции нажимайте enter')
print('Для окончания ввода нажмите enter')
a = int(input('-> '))
list = []
while True:
    try:
        positions.append(a)
        a = int(input('-> '))
    except:
        break
print(positions)
prod = 1
x = len(positions)
for i in range(0, x):
    prod *= numbers[positions[i]]
print(prod)
'''
'''5 Реализовать алгоритм перемешивания списка.'''
'''
from random import Random, randint
a = input("Введите элементы списка через пробел: ").split()
print(a)
l = len(a)
for i in range(len(a)):
    j = random.randint(0, i + 1)
    a[i], a[j] = a[j], a[i]
print()
print(a)
'''
