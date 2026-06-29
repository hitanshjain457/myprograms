#Write a program to input all sides of a triangle and check whether triangle is valid or not.
side1=3
side2=4
side3=5
if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("The triangle is valid")  
else:
    print("The triangle is not valid")