#1. Классы, конструкторы
class User:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    #2.1. Перевод объекта класса в строку
    def __str__ (self):
        return f"{self.first_name, self.last_name}"

    #2. Печать имени
    def print_name (self):
        print (self.first_name)

    #3. Печать фамилии
    def print_last_name (self):
        print (self.last_name)

    #4. Печать имени + фамилии
    def print_both (self):
        print (self.first_name + " " + self.last_name)