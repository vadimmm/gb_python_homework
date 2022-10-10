# 2 Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import os


def displayResult():
    count = 0
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                if not (x or y or z) == (not x and not y and not z):
                    # print(x, 'и', y, 'или', z, '=', x and y or z)
                    count += 1
    return count

statement = displayResult()

if statement == 8:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")

os.system("pause")