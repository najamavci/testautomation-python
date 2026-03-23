class Transaction:
    def transfer(self, amount, from_account, to_account):
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False