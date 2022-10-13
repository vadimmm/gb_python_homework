# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

import random

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите число: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

N = inputNumber()

N_list = {}
for i in range(N):
    N_list[i] = random.randint(-N, N)

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