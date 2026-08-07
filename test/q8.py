dic={
    'hitansh' : 45,
    'ivaid': 55,
    'aayush': 65
}
largest=0
student=''
for name,marks in dic.items():
    if(marks>=largest):
        largest=marks
        student=name
print(marks)
print(name)
