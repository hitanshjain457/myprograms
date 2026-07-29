a=[10, -5, 0, 20, -2, 0, 8]
postive=0
negative=0
zero=0
for i in a:
    if(i>0):
        postive+=1
    elif(i<0):
        negative+=1
    else:
        zero+=1
print("postive",postive)
print("negative",negative)
print("zero",zero)