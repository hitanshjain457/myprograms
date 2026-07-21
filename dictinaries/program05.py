subject={
    "science":55,
    "maths":62,
    "hindi":82
}
count =0

total_sum=0
for i in subject:
    count +=1
    total_sum+=subject[i]

print(list(subject.keys()))
print(list(subject.values()))  
print("subject count: ",count)
print("total marks sum: ",total_sum)
print("average marks: ", total_sum/count)