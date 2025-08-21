class Car:
    def __init__(self, brand, year, color="Black"):
        self.brand = brand
        self.year = year
        self.color = color

    def description(self):
        return f"{self.brand} ({self.year}) in color: {self.color}"

    def is_new(self):
        return self.year >= 2022


# if __name__ == "__main__":
car1 = Car("Toyota", 2023)
car2 = Car(color="Red", brand="Ford", year=2018)
print(car1.description()) # Toyota (2023)
print(car2.description()) # Ford (2018)
print(car1.is_new()) # True
print(car2.is_new()) # False
