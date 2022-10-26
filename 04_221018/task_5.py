# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0 40x9

degrees = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079"
           }

degrees_numb = {"0": "⁰",
               "1": "¹",
               "2": "²",
               "3": "³",
               "4": "⁴",
               "5": "⁵",
               "6": "⁶",
               "7": "⁷",
               "8": "⁸",
               "9": "⁹"
               }

def convertEquationFileToList(lNmae, fileName):
    # строка из файла в лист
    f = open(fileName, 'r', encoding='UTF-8')
    lNmae = f.readline()
    f.close()
    return lNmae

stage_1_1 = convertEquationFileToList('equation_lst_1', fileName='t5_1')
stage_1_2 = convertEquationFileToList('equation_lst_2', fileName='t5_2')

def parseEquationElementToList(lName):
    # разобрать числа на множители в каждый индекс
    tmp = lName.replace(" ", "")[:-2]
    result = tmp.replace("-", "+-").split("+")
    return result

stage_2_1 = parseEquationElementToList(stage_1_1)
stage_2_2 = parseEquationElementToList(stage_1_2)

def getExpressionDegree(lNameInput, pos):
    # в списке найти и подставить значение СТЕПЕНИ в выражении "00x⁰" по индексу
    lst = list(lNameInput[pos].partition('x'))
    degree = lst[2]
    if degree == '':
        degree_numb = 0
    else:
        deg = list(degree)
        for i in range(len(deg)):
            deg_value = deg[i]
            deg[i] = list(degrees_numb.keys())[list(degrees_numb.values()).index(str(deg_value))]
        lst[2] = ''.join(deg)
        degree_numb = ''.join(lst[2])
    # print(f'Значение степени в выражении: {degree_numb}')
    return degree_numb


def getExpressionNumber(lNameInput, pos):
    # в списке найти значение ЧИСЛА в выражении "00x⁰" по индексу
    lst = list(lNameInput[pos].partition('x'))
    # print(lst)
    numb = lst[0]
    if numb == '':
        numb = 1
    else:
        numb = lst[0]
    # print(f'Число в выражении: {numb}')
    return numb


def genDict(lName):
    dName = {}
    for i in range(len(lName)):
        key = getExpressionDegree(lName, i)
        value = getExpressionNumber(lName, i)
        dName[str(key)] = int(value)
    return dName

stage_3_1 = genDict(stage_2_1)
stage_3_2 = genDict(stage_2_2)


for key, value in stage_3_1.items():
    if key not in stage_3_2:
        stage_3_2[key] = value
    elif (key in stage_3_2) and (value + stage_3_2[key] == 0):
        del stage_3_2[key]
    else:
        stage_3_2[key] = value + stage_3_2[key]

def degreeReplace(equation):
    # Преобразует "00x^0" в "00x⁰"
    value = list(equation.partition('^'))
    value.pop(1)
    degree = list(value[1])
    for i in range(len(degree)):
        digit = degree[i]
        degree[i] = degrees[digit]
    value[1] = ''.join(degree)
    res = ''.join(value)
    return res


def sumEquationFromFile():
    pass
result_lst = []
count = 0
for key, value in sorted(stage_3_2.items(), reverse=True):
    if count == 0:
        equation = str(value) + 'x' + '^' + str(degreeReplace(key))
        count += 1
    elif value < 0 and int(key) == 0:
        equation = str(value)
    elif value > 0 and int(key) == 0:
        equation = "+" + str(value)
    elif value < 0 and int(key) == 1:
        equation = str(value) + 'x'
    elif value > 0 and int(key) == 1:
        equation = "+" + str(value) + 'x'
    elif value == 1 and value > 0:
        equation = '+' + 'x' + '^' + str(degreeReplace(key))
    elif value == -1 and value < 0:
        equation = '-' + 'x' + '^' + str(degreeReplace(key))
    elif value < 0 and count > 0:
        equation = str(value) + 'x' + '^' + str(degreeReplace(key))
    elif value > 0 and count > 0:
        equation = "+" + str(value) + 'x' + '^' + str(degreeReplace(key))

    result_lst.append(degreeReplace(equation))


result = ''.join(result_lst) + '=0'
print(result)
