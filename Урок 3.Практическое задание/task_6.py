"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

from random import randint

r = [randint(0, 88) for n in range(10)]
print(f'Массив: {r}')

min = 0
max = 0
step = 1
sum = 0

for i in r:
    if r[min] > i:
        min = r.index(i)
    elif r[max] < i:
        max = r.index(i)

if max - min < 0:
    step = -1

for i in r[min + step:max:step]:
    sum += i

print(f'Сумма элементов между минимальным {r[min]}', f' и максимальным {r[max]} элементами: {sum}')
