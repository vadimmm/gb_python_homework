# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите целое положительное число: "))
        if number <= 0:
            print(f"Вы ввели отрицательное число '{number}'! Введите положительное число больше 0!")
            return inputNumber()
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

k = inputNumber()
fibonacci_list = []

def negafibonacci(k):
        f1, f2 = 1, -1
        fibonacci_list.insert(0, f1)
        fibonacci_list.insert(0, f2)
        for j in range(2, k):
            f1, f2 = f2, f1 - f2
            fibonacci_list.insert(0, f2)
def fibonacci(k):
    if k == 0:
        fibonacci_list.append(0)
    else:
        f1, f2 = 0, 1
        fibonacci_list.append(f1)
        fibonacci_list.append(f2)
        for i in range(2, k + 1):
            f1, f2 = f2, f1 + f2
            fibonacci_list.append(f2)


negafibonacci(k)
fibonacci(k)


result = fibonacci_list
print(f'\nОТВЕТ: Последовательность Фибоначчи \n{result}')
