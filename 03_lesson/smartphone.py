# Есть класс Smartphone…
class Smartphone:

# Есть конструктор (self, марка телефона, модель телефона, абонентский номер +7)
    def __init__ (self, phone_brand, phone_model, phone_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.phone_number = phone_number

    def print_result (self):
        return f"{self.phone_brand} - {self.phone_model}. {self.phone_number}"