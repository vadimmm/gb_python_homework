# 5) Реализуйте алгоритм перемешивания списка.

import random
import datetime

dt = datetime.datetime.now()

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите число для установки длины списка: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

N = inputNumber()

rnd_list = {}

for i in range(0, N, 1):
    rnd_list[i] = random.randint(1, round(datetime.datetime.now().microsecond / N, 0))

print(f'Сгенерированный список: {rnd_list}')

for i in range(len(rnd_list)):
    rnd_index = random.randint(0, N-1)
    # tmp = rnd_list[i]
    # rnd_list[i] = rnd_list[rnd_index]
    # rnd_list[rnd_index] = tmp

    rnd_list[i], rnd_list[rnd_index] = rnd_list[rnd_index], rnd_list[i]

print(f'Перемешанный список: {rnd_list}')