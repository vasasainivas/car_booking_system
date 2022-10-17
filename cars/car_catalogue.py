from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def __init__(self, model, manufacturer, price, mileage, engine, fuel_type, seating_capacity):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.mileage = mileage
        self.engine = engine
        self.fuel_type = fuel_type
        self.seating_capacity = seating_capacity


class CarsBeforeAirbag(Car):
    def __init__(self,  model, manufacturer, price, mileage, engine, fuel_type, seating_capacity):
        super().__init__(model, manufacturer, price, mileage, engine, fuel_type, seating_capacity)


class CarWithAirBag(Car):
    def __init__(self,  model, manufacturer, price, mileage, engine, fuel_type, seating_capacity, air_bag):
        super().__init__(model, manufacturer, price, mileage, engine, fuel_type, seating_capacity)
        self.air_bag = air_bag


class CarModels:
    @staticmethod
    def car_models():
        innova = CarWithAirBag("Toyota", "Innova", "18.08", "10.2 to 15.6", "2393 to 2694 cc", "petrol and diesel",
                               7, "Available")
        fortuner = CarWithAirBag("Toyota", "Fortuner", "32.58", "10 to 14.4", "2694 to 2755 cc", "petrol and diesel",
                                 7, "Available")
        all_toyota_cars = [innova, fortuner]
        baleno = CarWithAirBag("Maruthi", "Baleno", "6.42", "22.3 to 22.9", "1197 cc", "petrol", 5, "Available")
        ertiga = CarWithAirBag("Maruthi", "Ertiga", "8.35", "20.3 to 26.1", "1462 cc", "petrol and CNG", 7, "Available")
        all_maruthi_cars = [baleno, ertiga]
        indica = CarWithAirBag("Tata", "Indica", "4.05", "22.7 to 25", "1396 cc", "Diesel & CNG", 5, "Available")
        safari = CarWithAirBag("Tata", "Safari", "15.35", "14 to 16.1", "1956 cc", "Diesel", 7, "Available")
        all_tata_cars = [indica, safari]
        brv = CarWithAirBag("honda", "BR-V", "9.61", "15.39 to 21.9", "1497 cc to 1498 cc", "Petrol & Diesel", 7,
                            "Available")
        city = CarWithAirBag("honda", "city", "11.57", "24.1 to 25", "1498 cc", "Petrol & Diesel", 5, "Available")
        all_honda_cars = [brv, city]
        return [all_toyota_cars, all_tata_cars, all_maruthi_cars, all_honda_cars]


class PrintCars:
    @staticmethod
    def print_car_models(selection, car_model: CarModels):
        car_object = car_model.car_models()[selection-1]
        count = 0
        for i in car_object:
            count += 1
            car = str(count)+" "+i.model+" "+i.manufacturer
            print(car)

    @staticmethod
    def show_car(selection, car_selection, car_model: CarModels):
        car_model = car_model.car_models()[selection - 1][car_selection-1]
        car = [car_model.model, car_model.manufacturer, car_model.price, car_model.mileage, car_model.engine,
               car_model.fuel_type, str(car_model.seating_capacity), car_model.air_bag]
        return car
