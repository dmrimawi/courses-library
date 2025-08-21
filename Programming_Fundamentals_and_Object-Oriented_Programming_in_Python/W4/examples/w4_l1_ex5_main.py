from w4_l1_ex5_car import Car


class Main:
    def run(self):
        car1 = Car("Toyotta", 2023, 80000, color="Red")
        car2 = Car("Ford", 2018, 45000)
        print(car1.description())
        print(car2.description())
        print(car1.is_new())
        print(car2.is_new())
        print(car1.get_price())
        print(car2.get_price())
        Car.tax_rate = 50
        print(car1.get_price())
        print(car2.get_price())
        Car.ask()


if __name__ == "__main__":
    main = Main()
    main.run()

