a = [1, 1, 1, 2, 1, 2, 3]
count = 1
max_count = 1
element = a[0]
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count
        element = a[i]
print(f"{element} lagataar {max_count} baar aaya hai")