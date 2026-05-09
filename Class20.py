class BankAccount():
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} successfully!")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdraw amount exceeds bank balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
            
    def get_balance_name(self):
        print(f"You are {self.account_holder} and your current balance is {self.__balance}.")
        
    def get_balance_amount(self):
        return self.__balance


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance_amount():
            super().withdraw(amount)
            print(f"{amount} withdrawn successfully.")
        elif amount <= self.get_balance_amount() + 500:
            super().withdraw(amount)
            print(f"{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded!")


name = input("Enter name: ")
balance  = float(input("Enter your initial balance: "))

acc1 = CurrentAccount(name, balance)


while True:
    
    print("Press:\n 1) To show account holder and balance")
    print("2) To deposit money ")
    print("3) To withdraw money")
    print("4) To exit the program")
    
    q = int(input("Press: "))
    
    if q == 1:
        acc1.get_balance_name()
    elif q == 2:
        amount = float(input("Enter deposit amount: "))
        acc1.deposit(amount)
    elif q == 3:
        amount = float(input("Enter withdraw amount: "))
        acc1.withdraw(amount)
    elif q == 4:
        print("Thanks for using our bank!")
        break
    else:
        print("Invalid output")