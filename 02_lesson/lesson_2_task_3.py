#1. Переменные, модули

import math

ent = float (input ("Введите сторону квадрата (Можно целое и не целое число): "))

#2. Функция

def square ():
    res = ent ** 2
    if res % 1 == 0:
        print (f"Площадь квадрата: {int(res)}")
    if res % 1 != 0:
        res_Ceil = math.ceil (res)
        print (f"Площадь квадрата (округлено до ближайшего целого числа): {res_Ceil}")

#3. Вызов функции

square ()