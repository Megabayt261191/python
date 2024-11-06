# есть список catalog…
from smartphone import Smartphone

iphone = Smartphone ("apple", "iPhone 15 Pro 256 naturlal", "+79876543212")
samsung = Smartphone ("samsung", "Samsung s24 Ultra", "+79876543200")
xiaomi = Smartphone ("xiaomi", "Xiaomi 13 Ultra", "+79876543201")
sony = Smartphone ("sony", "Xperia", "+79870010203")
blackberry = Smartphone ("blackberry", "10", "+79870020304")

catalog = [iphone, samsung, xiaomi, sony, blackberry]

# ЦИКЛ «Марка» - «модель». «номер телефона»

for phone in catalog:
    print(phone)