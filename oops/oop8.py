class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def deposit(self, am):
        self.amount += am
acc = Bank("hit", 5000)
acc.deposit(2000)
print(acc.amount)  