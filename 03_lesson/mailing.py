from address import Address

class Mailing:
    def __init__ (self, addressTo, addressFrom, track, cost):
        self.addressTo = addressTo
        self.addressFrom = addressFrom
        self.track = track
        self.cost = cost

    def __str__ (self):
         return f"Отправление '{self.track}' из '{self.addressFrom}' в '{self.addressTo}'. Стоимость {self.cost} рублей"