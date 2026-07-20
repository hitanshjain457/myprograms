a = [10, 20, 30, 20, 40, 20, 50]
for i in range(len(a)):
    count = 1
    already_counted = False
    for j in range(i):
        if (a[i] == a[j]):
            already_counted = True
            break
    if already_counted:
        continue
    for j in range(i + 1, len(a)):
        if (a[i] == a[j]):
            count += 1
    if (count > 1):
        print(a[i], ":", count)
while 20 in a:
        a.remove(20)
print(a)