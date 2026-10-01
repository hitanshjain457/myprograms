class Vehicle:
  def __init__(self,brand,color):
    self.brand=brand
    self.color=color  
class Car(Vehicle):
  def __init__(self, name,color,price):
        super().__init__(name,color)
        self.price = price
s1 = Car("BMW M4",'black' ,8500000)
print(s1.brand)
print(s1.color)
print(s1.price)