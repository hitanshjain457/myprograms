n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
print(a)
largest=a[0]
smallest=a[0]
for j in a:
    if (j>=largest):
        largest=j
    if(j<=smallest):
        smallest=j
print("largest number",largest)
print("smallest number",smallest)