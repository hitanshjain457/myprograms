employees = {
    101: 50000,
    102: 65000,
    103: 45000,
    104: 80000,
    105: 55000
}
total_salary = 0
for i in employees.values():
    total_salary += i
average_salary = total_salary / len(employees)
print("Total Salary:", total_salary)
print("Average Salary:", average_salary)