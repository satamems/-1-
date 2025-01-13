class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self):
        return f"{self.make} {self.model}"
    

class Car(Vehicle):
    def __init__(self, make: str, model: str, fuel_type: str):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{super().get_info()} Fuel type: {self.fuel_type}"


