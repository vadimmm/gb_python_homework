# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def inputNumber(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

numb = inputNumber(msg = "Пожалуйста, введите длину списка: ")
rnd_interval = inputNumber(msg = "Введите размер положительного пула случайных чисел: ")
rnd_list = []

for i in range(numb):
    rnd_numb = random.randint(1, round(rnd_interval / 2)+1)
    rnd_list.append(rnd_numb)

print(f'Сгенерированный список: {rnd_list}')

count = 0
print(f'\nОТВЕТ:\nПроизведение для пар')
for i in range(len(rnd_list)//2):
    numberFirst = rnd_list[i]
    numberSecond = rnd_list[len(rnd_list) - (1 + i)]
    numberMultiply = numberFirst * numberSecond
    count += 1
    print(f'\t\tпара чисел {count}:\t[{numberFirst} * {numberSecond} составляет {numberMultiply}]')