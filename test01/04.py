students = {
    "Rahul": 78,
    "Aman": 45,
    "Priya": 89,
    "Neha": 32,
    "Riya": 67
}

total_sum = 0
for marks in students.values():
    total_sum += marks
average = total_sum / len(students)
print("Average Marks:", average)
highest_marks = -1
top_student = ""
for student, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = student
print("Highest Marks:", top_student, "with", highest_marks)
lowest_marks = 101
lowest_student = ""
for student, marks in students.items():
    if marks < lowest_marks:
        lowest_marks = marks
        lowest_student = student
print("Lowest Marks:", lowest_student, "with", lowest_marks)