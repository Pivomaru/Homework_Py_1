# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input('Введите номер дня недели - '))
# if a == 6 and 7:
#     print('да')
# else :
#     print("нет")

################################################################################################


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

#############################################################################################

#  Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x , y = int(input("Введите х - ")), int(input("Введите у - "))

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#     print(4)

###################################################################

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input("Введите номер четверти - "))

# if number == 1:
#     print("Возможные координаты точки: x = [1, ∞), y = [1, ∞)")
# elif number == 2:
#     print("Возможные координаты точки: x = [-1, -∞), y = [1, ∞)")
# elif number == 3:
#     print("Возможные координаты точки: x = [-1, -∞), y = [-1, -∞)")
# elif number == 4:
#     print("Возможные координаты точки: x = [1, ∞), y = [-1, -∞)")
# else :
#     print("Ошибка")

##########################################################################

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from math import *

# x1, y1 = int(input("Точка х1: ")), int(input("Точка у1: "))
# x2, y2 = int(input("Точка х2: ")), int(input("Точка y2: "))

# d = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
# print(int(d * 100) / 100)
