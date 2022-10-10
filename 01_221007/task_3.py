# 3 Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
import os

class PositionInformer:
    answer_position = "Введённые координаты соответствуют плоскости "
    answer_axis = "Введённые координаты расположению "
    position_1 = "1"
    position_2 = "2"
    position_3 = "3"
    position_4 = "4"
    position_x = "на оси X"
    position_y = "на оси Y"

x, y = input("Введите через пробел целые числа координат X и Y точки: ").split()
print(f'Вы ввели следующие координаты x:y [{x}:{y}]')

if int(x) == 0 and int(y) == 0:
    print("Не допустимая позиция")
elif int(x) > 0 and int(y) > 0:
    result = PositionInformer.answer_position + PositionInformer.position_1
elif int(x) > 0 and int(y) < 0:
    result = PositionInformer.answer_position + PositionInformer.position_2
elif int(x) < 0 and int(y) < 0:
    result = PositionInformer.answer_position + PositionInformer.position_3
elif int(x) < 0 and int(y) > 0:
    result = PositionInformer.answer_position + PositionInformer.position_4
elif int(x) == 0 and ((y < 0) or (int(y) > 0)):
    result = PositionInformer.answer_axis + PositionInformer.position_x
elif ((int(x) < 0) or (int(x) > 0)) and int(y) == 0:
    result = PositionInformer.answer_axis + PositionInformer.position_y

print(result)

os.system("pause")