class Car:

    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod 
    def general_description():
        return "Cars are a means of transport"
    
    @property
    def model(self):
        return self.__model
    
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = Electric_car("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, Electric_car))

# safari = Car("Tata", "Safari")
# safari.model = "city"
# nexon = Car("Tata", "Nexon")

# print(safari.model)


# print(safari.general_description())
# print(Car.general_description())

# print(Car.total_car)

# print(my_tesla.fuel_type())
# print(safari.fuel_type())



# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.full_name())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

class Engine:
    def engine_info(self):
        return "This is engine"
    
class Battery:

    def battery_info(self):
        return "This is battery info"
    
class Electric_car_two(Battery, Engine, Car):
    pass

my_new_tesla = Electric_car_two("Tesla", "Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
    