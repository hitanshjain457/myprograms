student=[]
flag=True
print("1->add student ")
print("2->search student")
print("3->update student ")
print("4->delete student ")
print("5->display student ")
print("6->exit ")

while flag:
    user_input = int(input('choice: '))
    if user_input==1:
         dic={
             'name': input('enter your name: '),
             'age':int(input("enter age: "))
         }
         student.append(dic)
    elif user_input==2:
        data = input("enter a name to search: ")
        found = False
        for i in student:
            if i['name'].lower() == data.lower():
                print(f"Name: {i['name']}")
                print(f"Age: {i['age']}")
                found = True
                break
        if not found:
            print("student not found")
    elif user_input==3:
        update=input("enter a data: ")
        for i in student:
            if i['name'] in update:
                i['name'] = input("enter new name: ")
                i['age'] = int(input("enter new age: "))
    elif user_input==4:
        delete=input("enter a data: ")
        for i in student:
            if i['name'] in delete:
                student.remove(i)
                print("sucessfully deleted")
            else:
                print("student not found")
    elif user_input==5:
        for i in student:
            for key,value in i.items():
                print(key, ':', value)
    elif user_input==6:
        flag=False
        print("exist")