# Object-Oriented Programming Introduction Note  

Original Tutorial from (__*黄浩杰*__ )  
Link: [https://www.youtube.com/watch?v=myuSbEHFLBA](https://www.youtube.com/watch?v=myuSbEHFLBA)  
`That's not me, I'm just taking the note.`  


### What is the Class and Object?
___
Example (a) - __SEAT__

1. *__There are so many seats in this cinema.__*  
Those seats are a class.
All of these seats are the same thing,even they have a different numbers,
on the different sopt and in the different room. but when we're mentioned about a seat, it could be any one of them, they all belonging the same class.

2. *__My seat number is D7.__*  
The __D7__ is a parameter of the __number__ of the __seat__.
`seat.number = D7`
While we need to process something we need an object,
When you whet to a cinema, you're planning to get a ticket which is also means to get a seat. For some reason they figured out give a Number for seats. It's a good way to manage and they are not willing to see customers arguing for a seat. Simply put, they offer customers a seat with a seat number.
Now, we can get into the cinema, if there's guy sit on __D7__, just ask him go away, that's your seat, you can also show the __D7__ on your ticket.

| __class__ | __object__ |
|-----------|------------|
| Seat      | Number: D7 |  

___
Example (b) - __Bank Account__
  
File name: bank.py  
```python
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

```
All of Bank Account has thoes attribute  
+ Account Number  
+ Account Name  
+ Account Balance  
  
if we have to import the file and use it.  
```python
from bank import BankAccount # If File name: bank.py and in the same folder

b1 = BankAccount("56789", "Tony", 500.0) 
'''We creat a Bank Account as [b1]
account number == "56789"
account name == "Tony"
account balance == 500.0
'''
b2 = BankAccount("12345", "Jerry", 190.0) 
'''We creat a Bank Account as [b2]
account number == "12345"
account name == "Jerry"
account balance == 190.0
'''
print(b1.accountName)
# It will show the name of [b1]
print(b2.accountName)
# It will show the name of [b2]
```

result:  
```python
Tony
Jerry
```
  
Now, we're going to deposit and withdraw both account.  
```python
from bank import BankAccount # If File name: bank.py and in the same folder

b1 = BankAccount("56789", "Tony", 500.0) 
b2 = BankAccount("12345", "Jerry", 190.0)

b1.withdraw(100.0)
b2.deposit(50.0)

print(b1.balance)
print(b2.balance)
```

result:  
```python
400
240
```
  
If we're going to print out b1  
```python
from bank import BankAccount # If File name: bank.py and in the same folder

b1 = BankAccount("56789", "Tony", 500.0) 
b2 = BankAccount("12345", "Jerry", 190.0)

b1.withdraw(100.0)
b2.deposit(50.0)

print(b1)
```

result:  
```python
<Bank.BankAccount object at 0x10bc4a2e8> 
# Numbers 0x10bc4a2e8 won't match, it's just a address of the memory
```

If we add \_\_str\_\_ into bank.py  
```python
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


```

and we excute again  
```python
from bank import BankAccount # If File name: bank.py and in the same folder

b1 = BankAccount("56789", "Tony", 500.0) 
b2 = BankAccount("12345", "Jerry", 190.0)

b1.withdraw(100.0)
b2.deposit(50.0)

print(b1)
```

result:  
```python
(Tom, 400.0)
```
  
If we would like to compare balance of [b1] and [b2],
we can add \_\_lt\_\_ and \_\_gt\_\_ into bank.py  
( The former one is `#(__LT__)`  stand for` less than` and the other is `greater than`)  
```python
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

```

then, excute main.py  
```python
from bank import BankAccount # If File name: bank.py and in the same folder

b1 = BankAccount("56789", "Tony", 500.0) 
b2 = BankAccount("12345", "Jerry", 190.0)

b1.withdraw(100.0)
b2.deposit(50.0)

print(b1 < b2)
print(b1 > b2)
```

result:  
```python
False
True
```
  
|  __class__   |    __object__   |
|--------------|-----------------|
| Bank Account | Account Number  |
|              | Account Name    |
|              | Account Balance |


___

Class  
+ class member  
+ method `It's an action, process the variable`  

__*instance variable == class member*__`#成員變量`  
__*method is a function in the class*__`#類中的函式稱為方法`
