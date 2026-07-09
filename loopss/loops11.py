#Write a program to enter a number and print its reverse.		
a=788
reverse=0
while(a>0):
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
print("Reverse of the number:", reverse)
