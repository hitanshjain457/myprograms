#"Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#An additional surcharge of 20% is added to the bill"

unit=350
if(unit<=50):
    bill=unit*0.50
elif(unit<=150):
    bill=25+((unit-50)*0.75)
else:
    bill=100+((unit-150)*1.20)
surcharge=bill*0.20
total_bill=bill+surcharge
print("Total electricity bill:", total_bill)