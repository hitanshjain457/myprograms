#Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.
X = 250  # Example withdrawal amount
balance = 3500  # Example account balance

if (X % 5 == 0 and balance >= X + 0.50):
    balance -= X + 0.50
    print("Withdrawal successful. Remaining balance:", balance)
else:
    print("Withdrawal failed.")