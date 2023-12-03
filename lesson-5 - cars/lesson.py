class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

class Driver(Person):
    def __init__(self, full_name, driving_experience):
        super().__init__(full_name, driving_experience)

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Марка: {self.brand}, Класс: {self.car_class}, Вес: {self.weight}, " \
               f"Водитель: {self.driver.full_name}, Мотор: {self.engine.power}HP {self.engine.manufacturer}"

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, payload_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return super().__str__() + f", Грузоподъемность: {self.payload_capacity} тонн"

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", Предельная скорость: {self.max_speed} км/ч"

# Пример использования:

driver1 = Driver("Иван Иванов", 5)
engine1 = Engine(200, "Toyota")
car1 = Car("Toyota Camry", "Седан", 1500, driver1, engine1)

lorry1 = Lorry("Volvo", "Грузовик", 5000, driver1, engine1, 10)

sport_car1 = SportCar("Ferrari", "Спорткар", 1200, driver1, engine1, 300)

# Проверка методов:
car1.start()
car1.turn_left()
car1.stop()

print("\nИнформация о машине:")
print(car1)

print("\nИнформация о грузовике:")
print(lorry1)

print("\nИнформация о спорткаре:")
print(sport_car1)
