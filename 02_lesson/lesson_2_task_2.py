#1. Переменные

year = int (input ("Чтобы определить, високосный ли год, введите его в формате YYYY: "))

#2. Функции

def is_year_leap (year):
    if year % 4 == 0:
        print (f"год {year}: TRUE")
    if year % 4 != 0:
        print (f"год {year}: FALSE")

#3. Вызов функции

result = is_year_leap (year)
