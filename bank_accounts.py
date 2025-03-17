class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initAmount, acctName):
        self.balance = initAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' has ${self.balance:.2f}")

    def deposit(self, amount):
        print(f"\nAccount '{self.name}' has ${self.balance:.2f}")
        self.balance = self.balance + amount
        print(f"\nAdded ${amount:.2f} to '{self.name}'")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nYou withdrawed ${amount:.2f} from account '{self.name}'")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")
    
    def transfer(self, amount, account):
        try:
            print("\n**********\n\n↔️ Beginning transfer... ↔️")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\n✅ Transfer complete. ✅\n\n**********")
        except BalanceException as error:
            print(f"\n❌ Transfer interrupted : {error} ❌")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initAmount, acctName):
        super().__init__(initAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")