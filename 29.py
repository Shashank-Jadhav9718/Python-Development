# Refactor your BankAccount class by replacing your get_balance() method with a @property called balance. The user should be able to check their funds using my_account.balance instead of calling a function with parentheses.

class BankAccount:
    
    def __init__(self , name , actual_amount):
        self.name = name
        self.__actual_amount = actual_amount    
    
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
            
            
    @property
    def balance(self):
        return self.__actual_amount
    
            
    def __str__(self):
        return f"Account holder : {self.name} , Balance : {self.__actual_amount}"
    
    
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
                Balance = my_account.balance
                print(f"Balance = {Balance}")
            case 4:
                print(my_account)
            case 5:
                print("Exiting" )
            case _:
                print("Invalid choice. Please try again.")