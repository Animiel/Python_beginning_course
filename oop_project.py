from bank_accounts import *

Flo = BankAccount(1000, "Flo")
Sara = BankAccount(500, "Sara")

Flo.getBalance()
Sara.getBalance()

Sara.deposit(250)
Flo.withdraw(5000)
Flo.withdraw(100)

Flo.transfer(5000, Sara)
Flo.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Flo)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)