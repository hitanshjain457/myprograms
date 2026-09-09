class Person:
  def __init__(self,lenght,width):
    self.lenght=lenght
    self.width=width
  def display(self):
    print(self.lenght * self.width)
p1=Person(50,10)
p1.display()