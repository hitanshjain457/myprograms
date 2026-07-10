#Write a program to count total number of negative elements in an array.					
a=[-1,0,3,5,-2,-4]
negative=0
for i in a:
    if(i<0):
        negative+=1
print(" negative:",negative)