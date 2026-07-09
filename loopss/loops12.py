#Write a program to find frequency of each digit in a given integer.		
a=1234
frequency={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
while(a>0):
    digit=a%10
    frequency[digit]+=1
    a=a//10
print("Frequency of each digit:", frequency)