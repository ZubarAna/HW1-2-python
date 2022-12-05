'''
a = 5
b = 3
out_str = '{} + {}'.format(a, b)
out_str = f'{a} + {b}'
print(out_str)
'''

'''1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N
членов.
Пример:
- Для N = 5: 1, -3, 9, -27, 81'''
n = int(input('Enter N: '))
result = []
for i in range(0, n):
    res = (-3) ** i
    result.append(res)
print(*result, sep = ',')