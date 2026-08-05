marks = (45,67,89,32,56,89,90)
largest=marks[0]
smallest=marks[0]
for i in marks:
    if (i>=largest):
        largest=i
    if(i<=smallest):
        smallest=i
print("largest number",largest)
print("smallest number",smallest)
count=0
for j in marks:
    count+=j
print(f"total number: {count}")
print(f"average number;{count/len(marks)}")