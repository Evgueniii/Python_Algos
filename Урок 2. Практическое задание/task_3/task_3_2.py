"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
Используйте арифм операции для формирования числа, обратного введенному
Пример:
Введите число: 123
Перевернутое число: 321
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

def reversed_number(number_1, number_2):
    if number_1 == 0:
        return f'Перевернутое число: {number_2}'
    else:
        tmp = number_1 % 10
        return  reversed_number(number_1 // 10, str(number_2) + str(tmp))

print(reversed_number(int(input('Введите число, которое впоследстии перевернется: ')), ' '))
