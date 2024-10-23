#1. Переменные

result = int (input ("Введите число: "))

#2. Функции

def fizz_buzz ():
    for x in range (1, result + 1):
        if x % 3 == 0 and x % 5 == 0:
            print ("fizzBuzz")
        if x % 3 == 0:
            print ("fizz")
        if x % 5 == 0:
            print ("buzz")
        else:
            print (x)

#3. Вызов функции

fizz_buzz ()