products = {
    "Apples": 10,
    "Bananas": 3,
    "Milk": 2,
    "Bread": 8,
    "Eggs": 4
}
print("Products with quantity less than 5:")
for product, quantity in products.items():
    if quantity < 5:
        print(product)