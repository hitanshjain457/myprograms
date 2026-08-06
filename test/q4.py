arr = [1, 2, 3, 2, 4, 5, 1, 6]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)