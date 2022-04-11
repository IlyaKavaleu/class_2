class Car():
    """класс-тренировка"""
    def __init__(self, model, speed, color):
        "метод инит-конструктор"
        self.model = model
        self.speed = speed
        self.color = color


    def caro(self):
        "метод машины бугати"
        print("Your " + self.model +" move with " + str(self.speed) + " and have " + self.color + "!")


class ElectrickCar(Car):
    """класс-наследник"""
    def __init__(self, tesla, battery, color):
        super().__init__(tesla, battery, color)
        self.tesla = tesla
        self.battery = battery
        self.color = color

    def electro(self):
        print("I have new " + self.tesla + " and she have " + str(self.battery) + " akm. She have " + self.color + " color." )

        def kierowca():
            """внутреннний класс"""
            self.name = "Ilya"
            self.last_name = " Kavaleu"
            print(f"Driver have name " + self.name + self.last_name + "!")
        kierowca()

car = Car("Bugatti", 320, "gold")
car.caro()

electrickcar = ElectrickCar("Tesla", 1000, "silver")
electrickcar.electro()
