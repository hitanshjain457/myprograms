a=[1,2,22,5,55,6,66,10]
largest=a[0]
smallest=a[0]
for i in a:
    if (i>=largest):
        largest=i
    if(i<=smallest):
        smallest=i
print("largest number",largest)
print("smallest number",smallest)