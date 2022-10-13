# # 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # *Пример:*
# # - 6782 -> 23
# # - 0,56 -> 11

def inputNumber():
    try:
        float(number := input('Пожалуйста, введите число: ').replace(',', '.'))
        return number
    except ValueError:
        print('Ошибка ввода. Допускается только ввод чисел.', end=' ')
        return inputNumber()

numb = inputNumber().replace('.', '')

result = sum(int(i) for i in numb)

print(f'\nОТВЕТ: Сумма чисел равняется {result}')