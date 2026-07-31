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
        
        for j in student:
            for key,value in j.items():
                if(j==input('enter name to search: ')):
                    print(key, ':', value)
    
         
    elif user_input==5:
        for i in student:
            for key,value in i.items():
                print(key, ':', value)