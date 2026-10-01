# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def display(self):
#         print("Balance:", self.balance)

# s1 = BankAccount(2000)

# s1.display()
# s1.balance -= 1000
# s1.display()

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount

#     def display(self):
#         print(self.__balance)

# s1 = BankAccount(2000)
# # print(s1.__balance)
# s1._BankAccount__balance += 3000
# s1.display()