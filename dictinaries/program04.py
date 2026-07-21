employee={
    "emp_id":"2001",
    "emp_name":"harsh",
    "salary":20000
}
test = input("enter emp id: ")

print(type(test))
if( test == employee["emp_id"]):
    print(employee["emp_name"])
else:
    print("employee not found")