#write a program to check whether a number is prime or not
num=13
prime=True
if num>=1:
    for i in range(2,num):
        if num%i==0:
            prime=False
    if prime:
        print("is a prime number")
    else:
        print("is not a prime number")
else:
    print("number is negative or zero")
