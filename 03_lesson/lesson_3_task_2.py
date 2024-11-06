# есть список catalog…
from smartphone import Smartphone

iphone = ("apple", "iPhone 15 Pro 256 naturlal", "+79876543212")
samsung = ("samsung", "Samsung s24 Ultra", "+79876543200")
xiaomi = ("xiaomi", "Xiaomi 13 Ultra", "+79876543201")
sony = ("sony", "Xperia", "+79870010203")
blackberry = ("blackberry", "10", "+79870020304")

catalog = [iphone, samsung, xiaomi, sony, blackberry]

# ЦИКЛ «Марка» - «модель». «номер телефона»

for phone_brand, phone_model, phone_number in catalog:
    smartphone = Smartphone (phone_brand, phone_model, phone_number)
    print (smartphone.print_result ())