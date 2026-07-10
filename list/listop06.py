#Write a program to find second largest element in an array.				
a=[1,2,3,4,5]
max1=max(a)
a.remove(max1)
max2=max(a)
print("Second largest",max2)