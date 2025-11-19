class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.brand} {self.model} accelerated to {self.speed} km/h")
    
    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} slowed down to {self.speed} km/h")

# Example usage
car1 = Car("Tesla", "Model S")
car1.accelerate(50)
car1.brake(20)
