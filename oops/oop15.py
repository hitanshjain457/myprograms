class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
class Manager(Employee):
  def __init__(self,name,salary,department):
    super().__init__(name,salary)
    self.department=department
  def display(self):
    print(f"name:{self.name}")
    print(f"salary:{self.salary}")
    print(f"department:{self.department}")
e1=Manager('hitansh',500000,'it')
e1.display()
    