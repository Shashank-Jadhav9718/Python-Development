# Create a BusinessAccount class that inherits from your BankAccount class. It must require a name, an actual_amount, AND a business_id when it is created. You must use super() to let the parent class handle the name and amount, while the child class handles the new ID.


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
        
        
class BusinessAccount(BankAccount):
    def __init__(self, name , actual_amount , business_id):
        super().__init__(name , actual_amount)
        self.business_id = business_id
        
    def business_info(self):
        print("================================")
        print("Business Account Information:")
        print(f"Business Name: {self.name}")
        print(f"Business ID: {self.business_id}")   
        print(f"Balance: {self.actual_amount}")
        
        
if __name__ == "__main__":
    print("Create a Business Account")
    name = input("Enter the name of the business: ")
    starting_amount = float(input("Enter the starting amount: "))
    business_id = input("Enter the business ID: ")
    
    business_account = BusinessAccount(name, starting_amount, business_id)
    business_account.business_info()
    