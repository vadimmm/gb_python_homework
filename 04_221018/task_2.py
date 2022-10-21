# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите натуральное число: "))
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return inputNumber()

N = inputNumber()
result_lst = []


def simpleMultiplier(lName, numb):
   i = 2
   while i * i <= numb:
       while numb % i == 0:
           lName.append(i)
           numb /= i
       i += 1
   if numb > 1:
       lName.append(int(numb))
   return lName

result = simpleMultiplier(result_lst, N)

print(f'\nОТВЕТ: Для числа {N} найдены следующие множители {result}, в количестве {len(result)}')