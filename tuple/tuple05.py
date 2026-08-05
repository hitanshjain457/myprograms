n = int(input("How many numbers: "))
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
    t= tuple(numbers)
print(t)
largest=t[0]
smallest=t[0]
for i in t:
    if (i>=largest):
        largest=i
    if(i<=smallest):
        smallest=i
print("largest number",largest)
print("smallest number",smallest)
count=0
for j in t:
    count+=j
print(f"total number: {count}")
print(f"average number;{count/len(t)}")
even=0
odd=0
for z in t:
    if(z%2==0):
        even+=1
    else:
        odd+=1
print(f"count of even number {even}")
print(f"count of odd number {odd}")