from bank import BankAccount # If File name: bank.py and in the same folder

b1 = BankAccount("56789", "Tony", 500.0)
b2 = BankAccount("12345", "Jerry", 190.0)

b1.withdraw(100.0)
b2.deposit(50.0)

print(b1 < b2)
print(b1 > b2)
