class Person:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    
    
  def display(self):
    print(f"{self.name},{self.marks} ")
p1=Person('aman',55)
p2=Person('rahul',65)
p1.display()
p2.display()