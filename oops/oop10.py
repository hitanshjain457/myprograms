class Student:
    school = "ABC School"
    def __init__(self, name,age):
        self.name = name
        self.age=age
    def display(self):
      print(f"{self.name}")
      print(f"{self.age}")
      print(Student.school)
s1 = Student("Rahul",20)
s2 = Student("Amit",19)
s1.display()
s2.display()