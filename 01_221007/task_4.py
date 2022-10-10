# 4 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
import os

def InputQuota():
    try:
        number = int(input("Введите номер четверти: "))
        if 1 < number > 4:
            print(f"Вы ввели {number}, а четвертей всего 4. Попробуйте снова!")
            return InputQuota()
        return number
    except ValueError:
        print("Вы не ввели число, попробуйте снова!")
        return InputQuota()

quota = InputQuota()

if quota == 1:
    result = "x > 0; y > 0"
elif quota == 2:
    result = "x < 0; y > 0"
elif quota == 3:
    result = "x < 0; y < 0"
elif quota == 4:
    result = "x > 0; y < 0"

print(f"ОТВЕТ: Диапазон возможных координат точек {quota}й четверти: {result}")

os.system("pause")