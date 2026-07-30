num=int(input("enter any number:"))
value=0
for i in range(1,11):
    value+=num
    print(f"{i} * {num} : {value}")