# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def inputNumber(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

numb = inputNumber(msg = "Пожалуйста, введите целое число: ")

result = ""
while numb > 0:
    tmp = str(numb % 2)
    result = tmp + result
    numb = int(numb / 2)

# result = bin(numb)[2:]
print(f'ОТВЕТ: {result}')