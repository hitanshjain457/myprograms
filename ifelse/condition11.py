#"Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. 
#Calculate percentage and grade according to following:
#Percentage >= 80% : Grade B
#Percentage >= 70% : Grade C
#Percentage >= 60% : Grade D
#Percentage >= 40% : Grade E
#Percentage < 40% : Grade F"


physics=80
chemistry=70    
biology=60
mathematics=90
computer=85
total_marks=physics+chemistry+biology+mathematics+computer
percentage=(total_marks/500)*100
if(percentage>=80):
    print("Grade B")
elif(percentage>=70):
    print("Grade C")
elif(percentage>=60):
    print("Grade D")
elif(percentage>=40):
    print("Grade E")
else:
    print("Grade F")