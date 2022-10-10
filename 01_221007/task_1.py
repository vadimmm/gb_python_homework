# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
import os

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите номер дня недели: "))
        if number >= 8 or number <= 0:
            print(f"Упс! Вы ввели {number}, но в неделе всего 7 дней! Попробуйте снова!")
            return inputNumber()
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

day_numb = inputNumber()

if 1 <= day_numb <= 5:
    print("ОТВЕТ: Нет, это будний день")
else:
    print("ОТВЕТ: Да, это выходной день")

os.system("pause")