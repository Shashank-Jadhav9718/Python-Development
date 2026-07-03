# Create a SavingsAccount class that inherits from yesterday's BankAccount class. It must automatically have the ability to deposit, withdraw, and check balance, but you must add a brand new method called add_interest() that applies a percentage increase to the current balance.

class BankAccount:
    
    def __init__(self , name , actual_amount):
        self.name = name
        self.actual_amount = actual_amount
    
    def deposit_money(self ,amount : int):
        self.actual_amount += amount
        print(f"deposited {amount}")
        print(f"Balance = {self.actual_amount}")    
        
        
    def withdraw_money(self, amount):
        if amount <= self.actual_amount:
            self.actual_amount -= amount
            print(f"Withdrawn = {amount}")
            print(f"Balance = {self.actual_amount}")
        else:
            print(f"Insufficient Balance : {self.actual_amount}")
            
            
    def check_balance(self):
        print(f"Balance = {self.actual_amount}")
        

class SavingsAccount(BankAccount):
    def add_interest(self , interest_rate : float):
        interest = self.actual_amount * (interest_rate / 100)
        self.actual_amount += interest
        print(f"Interest added : {interest}")
        print(f"New Balance = {self.actual_amount}")    
        
        
if __name__ == "__main__":
    print('Create Savings Account')
    name = input("Enter Name : ")
    starting_balance = float(input("Enter Starting amount : "))
    saving_account = SavingsAccount(name, starting_balance)
    choice = 0
    while choice != 5:
        print("MENU")
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Check balance")
        print(" 4. Add Interest")
        print(" 5. Exit")
        choice = int(input("Enter Your Choice : "))

        match choice:
            case 1:
                amount = int(input("Enter Amount to deposit : "))
                saving_account.deposit_money(amount)
            case 2:
                amount = int(input("Enter Amount to withdraw : "))
                saving_account.withdraw_money(amount)
            case 3:
                saving_account.check_balance()
            case 4:
                interest_rate = float(input("Enter Interest Rate (in %): "))
                saving_account.add_interest(interest_rate)  
            case 5:
                print("Exiting")
            case _:
                print("Invalid choice. Please try again.")
    