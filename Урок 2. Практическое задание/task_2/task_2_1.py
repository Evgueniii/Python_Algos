"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
Для извлечения цифр числа используйте арифм. операции
Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
number = int(input('Введите натуральное число: '))
n = number
even = 0
not_even = 0

while not n == 0:
    tmp = n % 10
    if tmp % 2 == 0:
        even += 1
    else:
        not_even += 1
    n = n // 10

print(f'Число {number} состоит из {even + not_even} цифр, '
      f'в числе присутствуют {even} четных и {not_even} нечетных цифры.')
