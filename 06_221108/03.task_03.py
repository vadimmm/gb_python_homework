# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
import random

def inputNumber(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

numb = inputNumber(msg="Пожалуйста, введите длину списка: ")
rnd_interval = inputNumber(msg="Введите размер положительного пула случайных чисел: ")


def old_realization(numb, rnd_interval):
    rnd_list = []
    for i in range(numb):
        rnd_numb = random.uniform(1, round(rnd_interval / 2)+1)
        rnd_list.append(round(rnd_numb, 2))

    print(f'Сгенерированный список: {rnd_list}')

    max = 0
    for i in rnd_list:
        if max < (i - math.trunc(i)):
            max = (i - math.trunc(i))

    min = rnd_list[0]
    for i in rnd_list:
        if min > (i - math.trunc(i)):
            min = (i - math.trunc(i))

    result = max - min
    print(f'\nОТВЕТ: Разница между максимальной [{round(max,2)}] и минимальной [{round(min,2)}] дробной частью '
          f'составляет {round(result,2)}')


def new_realization(numb, rnd_interval):
    rnd_list = [round(random.uniform(1, round(rnd_interval / 2)+1), 2) for i in range(numb)]
    print(rnd_list)

    print(f'\nОТВЕТ: Разница между максимальной [{round(max(rnd_list),2)}] и минимальной [{round(min(rnd_list),2)}] дробной частью '
          f'составляет {round(max(rnd_list) - min(rnd_list),2)}')


print('old_realization()')
old_realization(numb, rnd_interval)

print('\nnew_realization()')
new_realization(numb, rnd_interval)