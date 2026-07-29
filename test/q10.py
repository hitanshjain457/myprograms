unique_numbers = set()
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    unique_numbers.add(num)  
print("\nFinal Set of Unique Numbers:", unique_numbers)
print("Total Unique Numbers:", len(unique_numbers))