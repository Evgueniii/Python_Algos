"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))


if number_1 == number_2 or number_2 == number_3 or number_3 == number_1:
    print('Введите три разных числа')

if number_2 < number_1 < number_3 or number_2 > number_1 > number_3:
    print(f'{number_1} - среднее число')

elif number_1 < number_2 < number_3 or number_1 > number_2 > number_3:
    print(f'{number_2} - среднее число')

elif number_1 < number_3 < number_2 or number_1 > number_3 > number_2:
    print(f'{number_3} - среднее число')