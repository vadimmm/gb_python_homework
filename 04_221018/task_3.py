# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите натуральное число: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

number = 1113384455229
# number = inputNumber()
print(f'Введённое число для проверки: {number}')

numbers_lst = [int(i) for i in str(number)]
# print(f'numbers_lst = {numbers_lst}')

def foundUnicumNumb(lNameInput, lName):
    for i in range(len(lNameInput)):
        count = 0
        for j in range(len(lNameInput)):
            if lNameInput[i] == lNameInput[j]:
                count += 1
        if count == 1:
            lName.append(lNameInput[i])

result_lst = []
foundUnicumNumb(numbers_lst, result_lst)

print(f'\nОТВЕТ: {number} -> {result_lst}')
