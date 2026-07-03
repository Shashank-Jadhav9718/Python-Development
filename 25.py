# Create a CheckingAccount class that inherits from BankAccount. Checking accounts have transaction fees. You must OVERRIDE the withdraw_money method so that every time a withdrawal is made, it secretly adds a $2 fee to the requested amount before processing it.

class BankAccount:
    
    def __init__(self , name , actual_amount):
        self.name = name
        self.__actual_amount = actual_amount    #To make a variable private in Python, you simply add two underscores to the front of its name inside the __init__ method.
    
    def deposit_money(self ,amount : int):
        self.__actual_amount += amount
        print(f"deposited {amount}")
        print(f"Balance = {self.__actual_amount}")    
        
        
    def withdraw_money(self, amount):
        if amount <= self.__actual_amount:
            self.__actual_amount -= amount
            print(f"Withdrawn = {amount}")
            print(f"Balance = {self.__actual_amount}")
        else:
            print(f"Insufficient Balance : {self.__actual_amount}")
            
            
    def check_balance(self):
        return self.__actual_amount
    
    def __str__(self):
        return f"Account holder : {self.name} , Balance : {self.__actual_amount}"
    
class CheckingAccount(BankAccount):
    def withdraw_money(self, amount):
        fee = 2
        total_deduction = amount + fee
        if total_deduction <= self.check_balance():
            super().withdraw_money(total_deduction) 
    
    
class BusinessAccount(BankAccount):
    def withdraw_money(self, amount):
        print(f"--> [Business] Verifying corporate ID for {self.name}...")
        # Business accounts have no fees, just a security print statement
        super().withdraw_money(amount)
        
            
    
if __name__ == "__main__":
    standard = BankAccount("Alice", 100)
    checking = CheckingAccount("Bob", 100)
    business = BusinessAccount("CorpInc", 100)
    
    bank_database = [standard, checking, business]

    print("--- PROCESSING BATCH WITHDRAWALS ---")

    # We loop through the list and tell EVERY account to withdraw $20
    for account in bank_database:
        # Python dynamically checks the object type at runtime and picks the right method!
        account.withdraw_money(20)
        print("-" * 40)