class Result:
    def __init__(self, isSuccess, message, value=None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value

    def is_ok(self):
        return self.isSuccess


class Ok(Result):
    def __init__(self,  message, value=None):
        super().__init__(message, value)
        self.isSucces = True


class Error(Result):
    def __init__(self,  message, value=None):
        super().__init__(message, value)
        self.isSucces = False


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            return Ok("Succeded to withdraw", amount)

        return Error("You don't have enough money to withdraw", amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Result(False, "You don't have enough money to withdraw", amount)
