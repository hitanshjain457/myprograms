even_numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if(num % 2 == 0):
        even_numbers.append(num)
print("Even numbers:", even_numbers)