from address import Address
from mailing import Mailing

addressTo = Address ("0791", "Шир", "ул. Беггинса", "дом 3", "квартира 1")
addressFrom = Address ("0990", "Минас-Тирит", "ул. Кузнецов", "дом 98", "квартира 3")
shipment1 = Mailing (addressTo, addressFrom, "909809", "15 золотых")

print (shipment1)