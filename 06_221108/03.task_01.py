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

# N = inputNumber()

def old_realization(N):

    numb = inputNumber(msg="Пожалуйста, введите длину списка: ")
    rnd_interval = inputNumber(msg="Введите размер симметричного пула случайных чисел: ")
    rnd_list = {}

    for i in range(0, numb, 1):
        rnd_numb = randint(round(-rnd_interval / 2), round(rnd_interval / 2) + 1)
        rnd_list[i] = rnd_numb

    print(f'Сгенерированный список: {rnd_list}')

    sum = 0
    for i in range(1, len(rnd_list), 2):
        sum += rnd_list[i]

    print(f'\nОТВЕТ: Сумма нечётных позиций индексов составляет {sum}')

def new_realization(N):
    N_list = [randint(-10, 10) for i in range(10)]
    # for i in range(N):
    #     N_list[i] = random.randint(-N, N)

    print(f"Сгенерированные значения: {N_list}")


    input_position = input("Введите актуальные позиции для расчёта: ").split()
    input_list = [int(numb) for numb in set(input_position) if -N <= int(numb) < N]

    print(f"Введённые позиции для произведения: {input_list}")

    product_of_numbers = 1

    for i in range(len(input_list)):
        for j in range(len(N_list)):
            if j == i:
                product_of_numbers *= N_list[input_list[i]]

    print(f'\nОТВЕТ: Произведение выбранных индексов составляет {product_of_numbers}')

# print('old_realization(n)')
# old_realization(N)

print('\nnew_realization(n)')
new_realization(N)