data = [10, 20, 30, 40, 50, 20, 30]
total_sum = 0
for i in data:
    total_sum += i
avg = total_sum // len(data)
print(avg)
print(total_sum)
max_val = max(data)
print(max_val)
min_val = min(data)
print(min_val)
while 20 in data:
    data.remove(20)
print(data)