class BankAccount:
    def __init__(self, balance=0, logger=None):
        self.balance = balance
        self.logger = logger

    def deposit(self, amount):
        self.balance += amount
        if self.logger:
            self.logger.log(f"deposit: {amount} kr, saldo {self.balance} kr")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            if self.logger:
                self.logger.log(f"withdraw: {amount} kr, saldo {self.balance} kr")
            return True

        if self.logger:
            self.logger.log(f"withdraw: kunde inte ta ut {amount} kr från kontot")
        return False