#1. Переменные

result = int (input ("Введите номер месяца (1-12), чтобы узнать название сезона, к которому он относится: "))

#2. Функции

def month_to_season ():
    if result == 12 or result == 1 or result == 2:
        print ("Зима")
    elif result == 3 or result == 4 or result == 5:
        print ("Весна")
    elif result == 6 or result == 7 or result == 8:
        print ("Лето")
    elif result == 9 or result == 10 or result == 11:
        print ("Осень")
    else:
        print ("Ошибка  Такого месяца не существует")
    

#3. Вызов функции

month_to_season ()