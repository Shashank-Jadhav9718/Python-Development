# Add the __str__ magic method to your existing BankAccount class so that printing the object directly returns a clean, human-readable summary of the account instead of a memory address.

class BankAccount:
    
    def __init__(self , name , actual_amount):
        self.name = name
        self.__actual_amount = actual_amount    #To make a variable private in Python, you simply add two underscores to the front of its name inside the __init__ method.
    
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
        
    def __str__(self):
        return f"Account holder : {self.name} , Balance : {self.actual_amount}"
    
    
    
if __name__ == "__main__":
    print('Create Account')
    name = input("Enter Name : ")
    starting_balance = float(input("Enter Starting amount : "))
    my_account = BankAccount(name, starting_balance)

    choice = 0
    while choice != 5:
        print("MENU")
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Check balance")
        print(" 4. Account Details:")
        print(" 5. Exit")
        choice = int(input("Enter Your Choice : "))

        match choice:
            case 1:
                amount = int(input("Enter Amount to deposit : "))
                my_account.deposit_money(amount)
            case 2:
                amount = int(input("Enter Amount to withdraw : "))
                my_account.withdraw_money(amount)
            case 3:
                my_account.check_balance()
            case 4:
                print(my_account)
            case 5:
                print("Exiting" )
            case _:
                print("Invalid choice. Please try again.")