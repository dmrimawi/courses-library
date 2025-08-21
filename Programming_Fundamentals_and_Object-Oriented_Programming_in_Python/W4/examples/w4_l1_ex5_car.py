class Car:
    tax_rate = 100
    def __init__(self, brand, year, price, color="Black"):
        self.brand = brand
        self.year = year
        self.price = price
        self.color = color

    def description(self):
        return f"{self.brand} ({self.year}) in color: {self.color}"

    def is_new(self):
        return self.year >= 2022

    def get_price(self):
        return (Car.tax_rate / 100.0) * self.price + self.price

    @staticmethod
    def ask():
        print("This a Car class")
