from datetime import datetime

class Product:
    def __init__(self, name="", price=0, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Ürün adı: {self.name}, KayitTarihi: {datetime.now()}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 8:
            self._name = value
        else:
            raise ValueError("Ürün adı 3 ile 8 karakter arasında olmalıdır.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Ürün fiyatı 0 veya daha büyük olmalıdır.")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self._quantity = value
        else:
            raise ValueError("Ürün adedi en az 1 olmalıdır.")

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.price}, Quantity: {self.quantity})"