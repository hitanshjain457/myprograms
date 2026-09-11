class Employee:
    company = "ABC company"
    def __init__(self, name,salary):
        self.name = name
        self.salary=salary
    def display(self):
      print(f"{self.name}")
      print(f"{self.salary}")
      print(Employee.company)
s1 = Employee("Rahul",20000)
s2 = Employee("Amit",19000)
s1.display()
s2.display()
