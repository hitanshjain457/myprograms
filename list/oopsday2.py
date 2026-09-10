class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


s1 = Student("Rahul", 70)
s2 = Student("Amit", 30)

s1.show()
s1.result()

s2.show()
s2.result()