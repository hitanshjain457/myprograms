numbers = [12, 5, 7, 20, 33, 40, 18]
even=[]
odd=[]
for i in numbers:
  if(i%2==0):
    even.append(i)
  else:
    odd.append(i)
print(even)
print(odd)