#Write a program to input month number and print number of days in that month.
month=5
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("The month has 31 days")
elif(month==4 or month==6 or month==9 or month==11):
    print("The month has 30 days")
elif(month==2):
    print("The month has 28 days")
else:
    print("Invalid month number")