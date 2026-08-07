list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]
common_elements = []
for i in list1:
    for j in list2:
        if i == j and i not in common_elements:
            common_elements.append(i)
print(f"Common elements: {common_elements}"