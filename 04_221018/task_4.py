# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите натуральное число: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

# k = inputNumber()
# k = 5

degree_symbol = '^'

degrees = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           }

def degreeReplace(equation):
    value = list(equation.partition(degree_symbol))
    value.pop(1)
    degree = list(value[1])
    for i in range(len(degree)):
        digit = degree[i]
        degree[i] = degrees[digit]
    value[1] = ''.join(degree)
    res = ''.join(value)
    return res

def genEquation(inputN):
    x = "x"
    sign = ["+", "-"]
    result_lst = []
    count = 0
    for i in range(inputN, -1, -1):
        rnd = random.randint(-100, 100 + 1)
        rnd_sign = random.choice(sign)

        if rnd == 0:
            continue
        elif i == inputN and count == 0 and rnd != 0:
            equation = str(rnd) + x + degree_symbol + str(i)
            count += 1
        elif rnd < 0 and i == 0:
            equation = str(rnd)
        elif i == 0:
            equation = str(rnd_sign) + str(rnd)
        elif rnd < 0 and i == 1:
            equation = str(rnd) + x
        elif i == 1:
            equation = str(rnd_sign) + str(rnd) + x
        elif rnd < 0 and i != inputN:
            equation = str(rnd) + x + degree_symbol + str(i)
        elif rnd < 0:
            equation = str(rnd) + x + degree_symbol + str(i)
        elif rnd > 0 and i != inputN:
            equation = str(rnd_sign) + str(rnd) + x + degree_symbol + str(i)

        # result_lst.append(equation)
        result_lst.append(degreeReplace(equation))

    result = ''.join(result_lst) + '=0'
    return result


# result = genEquation(k)
# print(result)

def genEquationFile(fName):
    # rnd_input = inputNumber()
    rnd_equation = genEquation(inputNumber())
    with open(fName, 'w', encoding='UTF-8') as file:
        file.write(rnd_equation)
        print(f'Файл "{fName}" создан со строкой со следующими данными:\n{rnd_equation} ')

genEquationFile('t4')