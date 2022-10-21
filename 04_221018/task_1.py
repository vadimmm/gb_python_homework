# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
#
# !!! не округлять константу math

d = str(input("Введите число 'd' от 0.1 до 0.0000000001: "))
d_len = len(str(d))-2

def piNilakanta(num):
    pi = 3.0
    n1, n2, n3, = 2, 3, 4
    for i in range(num):
        pi += 4/(n1 * n2 * n3)
        n1 += 2
        n2 += 2
        n3 += 2
        pi -= 4/(n1 * n2 * n3)
        n1 += 2
        n2 += 2
        n3 += 2
    return pi

result = round(piNilakanta(d_len+2), d_len)
print(piNilakanta(d_len))
print(f"\nОТВЕТ: Для введённого значения 'd' {d} результат округления π составляет {result}")