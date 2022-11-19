# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите число: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

n = inputNumber()


def old_realization(n):
    result_formula_calculation = {}
    for i in range(1, n + 1, 1):
        result_formula_calculation[i] = round(((1 + 1 / i) ** i), 2)

    print(result_formula_calculation)

    sum = float(0)
    for i in range(1, len(result_formula_calculation) + 1, 1):
        sum += result_formula_calculation[i]

    result = round(sum, 2)

    print(f'ОТВЕТ: Для числа {n} сумма составляет {result}')


def new_realization(n):
    result_formula_calculation = list(map(lambda x: round(((1 + 1 / x) ** x), 2), range(1, n + 1, 1)))
    print(result_formula_calculation)

    result = sum(result_formula_calculation)

    print(f'ОТВЕТ: Для числа {n} сумма составляет {result}')


print('old_realization()')
old_realization(n)

print('\nnew_realization()')
new_realization(n)
