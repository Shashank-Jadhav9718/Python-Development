# Turn your BankAccount into an Abstract Base Class. Then, create a new @abstractmethod called generate_statement(). You must not write any code inside this method in the parent class. Instead, you must force your SavingsAccount child class to implement its own version of this method.

from abc import ABC, abstractmethod 

class InsufficientFundsError(Exception):
    pass 

class BankAccount(ABC):
    total_Account = 0
    
    def __init__(self , name , starting_balance):
        self.name = name
        self.__actual_amount = starting_balance
        BankAccount.total_Account += 1
        
    def deposit_money(self , amount : float):
        self.__actual_amount += amount
        print(f"Amount {amount} deposited")
        print(f"New Balance : {self.__actual_amount}")
        
    def withdraw_money(self , amount):
        if amount > self.__actual_amount:
            raise InsufficientFundsError(f"Insufficient Balance : {self.__actual_amount}")
        
        self.__actual_amount -= amount
        print(f"Withdrawn = {amount}")
        print(f"Balance = {self.__actual_amount}")
        
    
    @property
    def balance(self):
        return self.__actual_amount
    
    def __str__(self):
        print(f"Account Holder : {self.name} \n Balance : {self.__actual_amount}")
        
    @classmethod
    def get_total_account(self):
        return BankAccount.total_Account
    
    @abstractmethod
    def generate_statement(self):
        pass
        
    
    
class SavingsAccount(BankAccount):
    
    def withdraw_money(self, amount):
        total_deduction = amount + 2
        return super().withdraw_money(total_deduction)
    
    def generate_statement(self):
        print(f"--- {self.name.upper()}'S SAVINGS STATEMENT ---")
        print(f"Current Balance: ${self.balance}")
        
        
class Business_account(BankAccount):

    def __init__(self, name, starting_balance , Business_ID):
        super().__init__(name, starting_balance , Business_ID) 


def get_clean_prompt(prompt):
    while True : 
        try:
            amount = float(input(prompt))
            return amount 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        
if __name__ == "__main__":
    def main():
        print("Welcome to the simple Bank CLI")
        name = input("Enter account holder name: ").strip() or "Unnamed"
        starting = get_clean_prompt("Enter starting balance: ")
        account = SavingsAccount(name, starting)

        while True:
            print("\nChoose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Generate statement")
            print("4. Show balance")
            print("5. Total accounts")
            print("6. Exit")
            choice = input("Choice: ").strip()

            match choice:
                case "1":
                    amt = get_clean_prompt("Deposit amount: ")
                    account.deposit_money(amt)
                case "2":
                    amt = get_clean_prompt("Withdraw amount: ")
                    try:
                        account.withdraw_money(amt)
                    except InsufficientFundsError as e:
                        print(e)
                case "3":
                    account.generate_statement()
                case "4":
                    print(f"Current balance: {account.balance}")
                case "5":
                    print(f"Total accounts: {BankAccount.get_total_account()}")
                case "6" | "q" | "exit":
                    print("Exiting. Goodbye.")
                    break
                case _:
                    print("Invalid choice. Please select a valid option.")

    main()
