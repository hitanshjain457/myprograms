flag = True
arr = []

while flag:
    user_input = int(input('please add numbers: '))
    if user_input != -1:
        arr.append(user_input)
    elif user_input == -1:
        flag = False
print(arr)
print(f"total numbers : {len(arr)}")
sum=0
for i in arr:
    sum+=i
print(f"sum:{sum}")
print(f"average:{sum//len(arr)}")
largest=arr[0]
smallest=arr[0]
for j in arr:
    if (j>=largest):
        largest=j
    if(j<=smallest):
        smallest=j
print("largest number",largest)
print("smallest number",smallest)