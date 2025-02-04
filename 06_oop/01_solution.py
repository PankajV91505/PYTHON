class Car:
    total_car = 0
    def __init__(self, brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand + " !!"
    def fuel_type(self):
        return "Petrol & Diesel"
    
    @staticmethod
    def general_info():
        return "This is a car class"
    
    @property
    def model (self):
        return self.__model
    
    

class ElectricCar(Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electricity"
    
# safari = Car("Tata", "Safari")
# print(safari.fuel_type())
        
my_tesla_car = ElectricCar("Tesla", "Model S", '100kWh')

# print(isinstance(my_tesla_car, ElectricCar))
# print(isinstance(my_tesla_car, Car))
# print(my_tesla_car.__brand)
# print(my_tesla_car.get_brand())
# print(my_tesla_car.fuel_type())

# print(Car.total_car)

# my_car = Car("Toyota", "Corolla")
# Car("Tata", "nexon")

# print(my_car.model)

# # print(my_car.general_info())
# # print(Car.general_info())


# print(my_tesla_car.model)
# print(my_tesla_car.full_name())
    
# my_car = Car("toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("honda", "civic")
# print(my_new_car.brand)
# print(my_new_car.model)


class Battery:
    def battery_size(self):
        return "this is battery "

class Engine:
    def engine_type(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_testla = ElectricCarTwo("Tesla", "Model S")
print(my_new_testla.battery_size())
print(my_new_testla.engine_type())