#Write a program to print all Prime numbers between 1 to n.		
n=10
for num in range(1, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)