# Add a class variable to your BankAccount class that tracks the total_accounts created. Increment this number every time a new account is instantiated. Then, create a class method called get_total_accounts() that prints this total.

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    total_accounts = 0
    
    def __init__(self , name , actual_amount):
        self.name = name
        self.__actual_amount = actual_amount
        BankAccount.total_accounts += 1
    
    def deposit_money(self ,amount : int):
        self.__actual_amount += amount
        print(f"deposited {amount}")
        print(f"Balance = {self.__actual_amount}")    
        
        
    def withdraw_money(self, amount):
        if amount > self.__actual_amount:
            raise InsufficientFundsError(f"Insufficient Balance : {self.__actual_amount}")
        
        self.__actual_amount -= amount
        print(f"Withdrawn = {amount}")
        print(f"Balance = {self.__actual_amount}")
        
        
    def check_balance(self):
        return self.__actual_amount
    
    def __str__(self):
        return f"BankAccount(Name: {self.name}, Balance: {self.__actual_amount})"
    
    @classmethod
    def get_total_accounts(cls):
        print(f"Total Accounts created : {cls.total_accounts}")



def get_valid_amount(prompt_message):
    while True:
        try:
            amount = float(input(prompt_message))
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
        
if __name__ == "__main__":
    choice = 0
    while choice != 6:
        print("MENU")
        print(" 1. Create Account")
        print(" 2. Deposit")
        print(" 3. Withdraw")
        print(" 4. Check balance")
        print(" 5. Total Accounts")
        print(" 6. Exit")
        choice = int(input("Enter Your Choice : "))

        match choice:
            case 1:
                print('Create Account')
                name = input("Enter Name : ")
                starting_balance = get_valid_amount("Enter Starting amount : ")
                my_account = BankAccount(name, starting_balance)
            case 2:
                amount = get_valid_amount("Enter Amount to deposit : ")
                my_account.deposit_money(amount)
            case 3:
                amount = int(input("Enter Amount to withdraw : "))
                try:
                    my_account.withdraw_money(amount)
                except InsufficientFundsError as e:
                    print(f"TRANSACTION DENIED: {e}")
            case 4:
                Balance = my_account.check_balance()
                print(f"Balance = {Balance}")
            case 5:
                BankAccount.get_total_accounts()
                print(my_account)
            case 6 :
                print("Exiting")
            case _:
                print("Invalid choice. Please try again.")
    
    