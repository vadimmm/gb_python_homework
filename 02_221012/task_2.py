# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите целое число: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

N = inputNumber()

product_of_numbers = []
digit = 1
for i in range(1, N+1, 1):
    digit *= i
    product_of_numbers.append(digit)

print(f'\nОТВЕТ: Для числа {N} произведением чисел является {product_of_numbers}')

