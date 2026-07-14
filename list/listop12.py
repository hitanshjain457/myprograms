# write a program to print unique character in list
a=[1,2,3,4,4,5,4,5,74,4]
b=[]
c=[]
for i in a:
    if(i%2==0):
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)