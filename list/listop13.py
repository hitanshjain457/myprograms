a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
dup = []

for i in range(len(a)):
    count=0
    for j in range(i + 1, len(a)):

        if a[i] == a[j] and a[i] not in dup:
			
            dup.append(a[i])
            count+=1 
print({a[i]},":", {count})
