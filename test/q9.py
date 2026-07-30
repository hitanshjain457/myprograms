a = input("enter a line: ").split()
count_dict = {}
for word in a:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1
print(count_dict)