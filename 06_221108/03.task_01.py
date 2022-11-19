# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint


def inputNumber(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()


numb = inputNumber(msg="Пожалуйста, введите длину списка: ")
rnd_interval = inputNumber(msg="Введите размер симметричного пула случайных чисел: ")


def old_realization(numb, rnd_interval):
    rnd_list = {}

    for i in range(0, numb, 1):
        rnd_numb = randint(round(-rnd_interval / 2), round(rnd_interval / 2) + 1)
        rnd_list[i] = rnd_numb

    print(f'Сгенерированный список: {rnd_list}')

    sum = 0
    for i in range(1, len(rnd_list), 2):
        sum += rnd_list[i]

    print(f'\nОТВЕТ: Сумма нечётных позиций индексов составляет {sum}')


def new_realization(numb, rnd_interval):
    rnd_list = [randint(round(-rnd_interval / 2), round(rnd_interval / 2) + 1) for i in range(0, numb, 1)]

    print(f'Сгенерированный список: {rnd_list}')

    result = sum(rnd_list[i] for i in filter(lambda x: x, range(1, len(rnd_list), 2)))

    print(f'\nОТВЕТ: Сумма нечётных позиций индексов составляет {result}')


print('old_realization()')
old_realization(numb, rnd_interval)

print('\nnew_realization()')
new_realization(numb, rnd_interval)