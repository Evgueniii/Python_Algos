"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""
import random
min_number = 1
max_number = 100
random_number = int(random.random() * (max_number - min_number + 1)) + min_number
print(f'Целое число от {min_number} до {max_number}: {random_number}')

min_number = 3.14
max_number = 12.7
real_number = float(random.random() * (max_number - min_number)) + min_number
print(f'Вещественное число от {min_number} до {max_number}: {round(real_number,3)}')

min_char = 'a'
max_char = 'z'
random_char = chr(int(random.random() * (ord(max_char) - ord(min_char) + 1)) + ord(min_char))
print(f'Символ от {min_char} до {max_char}: {random_char}')