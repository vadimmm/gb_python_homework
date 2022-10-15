# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def inputNumber(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

numb = inputNumber(msg = "Пожалуйста, введите длину списка: ")
rnd_interval = inputNumber(msg = "Введите размер симметричного пула случайных чисел: ")
rnd_list = {}


for i in range(0, numb, 1):
    rnd_numb = random.randint(round(-rnd_interval / 2), round(rnd_interval / 2)+1)
    rnd_list[i] = rnd_numb

print(f'Сгенерированный список: {rnd_list}')

sum = 0
for i in range(1,len(rnd_list), 2):
    sum += rnd_list[i]

print(f'\nОТВЕТ: Сумма нечётных позиций индексов составляет {sum}')
