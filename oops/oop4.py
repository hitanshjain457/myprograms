class Person:
  def __init__(self,name,city):
    self.name=name
    self.city=city
  def display(self):
    print(f"{self.name} lives in {self.city} ")
p1=Person('aman','indore')
p2=Person('rahul','bhopal')
p1.display()
p2.display()