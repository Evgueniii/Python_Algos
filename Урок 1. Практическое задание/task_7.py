"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
a = int(input('Введите сторону а:'))
b = int(input('Введите сторону b:'))
c = int(input('Введите сторону c:'))

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b or a == c or b == c:
        if a == b and b == c:
            print('Равносторонний треугольник')
        else:
            print('Равнобедренный треугольник')
    else:
        print('Разносторонний треугольник')
else:
    print('Такого треугольника не бывает')