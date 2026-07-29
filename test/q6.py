student_dict = {}
for i in range(5):
    roll_no = int(input(f"Enter Roll Number for student {i + 1}: "))
    name = input(f"Enter Name for student {i + 1}: ")
    student_dict[roll_no] = name
print(student_dict)