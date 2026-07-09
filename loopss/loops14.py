#write a program to check wehether number is armstrong or not
a=153
temp=a
sum=0
while(temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if(a==sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong")