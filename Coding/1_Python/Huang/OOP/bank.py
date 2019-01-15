class BankAccount:
    #Constructor 構造器
    def __init__(self, number, name, balance):
        self.accountNumber = number
        self.accountName = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        #self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        #("Tom", 100.0)
        return "({}, {})".format(self.accountName, self.balance)

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance
