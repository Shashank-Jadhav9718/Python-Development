# Create a custom exception class called InsufficientFundsError. Then, modify your withdraw_money method so that instead of using print(), it uses the raise keyword to throw your custom error when a user tries to overdraw. Finally, catch that specific error in a try...except block.

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    
    def __init__(self , name , actual_amount):
        self.name = name
        self.__actual_amount = actual_amount
    
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



def get_valid_amount(prompt_message):
    while True:
        try:
            amount = float(input(prompt_message))
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
        
if __name__ == "__main__":
    print('Create Account')
    name = input("Enter Name : ")
    starting_balance = get_valid_amount("Enter Starting amount : ")
    my_account = BankAccount(name, starting_balance)

    choice = 0
    while choice != 4:
        print("MENU")
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Check balance")
        print(" 4. Exit")
        choice = int(input("Enter Your Choice : "))

        match choice:
            case 1:
                amount = get_valid_amount("Enter Amount to deposit : ")
                my_account.deposit_money(amount)
            case 2:
                amount = int(input("Enter Amount to withdraw : "))
                try:
                    my_account.withdraw_money(amount)
                except InsufficientFundsError as e:
                    print(f"TRANSACTION DENIED: {e}")
            case 3:
                Balance = my_account.check_balance()
                print(f"Balance = {Balance}")
            case 4:
                print("Exiting")
            case _:
                print("Invalid choice. Please try again.")
    
    