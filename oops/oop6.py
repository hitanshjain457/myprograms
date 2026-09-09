class Person:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def display(self):
    print(f"name : {self.name}")
    print(f"salary : {self.salary}")
p1=Person('siddharth',55000)
p1.display()
