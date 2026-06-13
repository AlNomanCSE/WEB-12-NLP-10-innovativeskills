class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        # self._balance = balance  # protected
        self.__balance = balance  # private
        self.__pin = "1234"  # private

    @property
    def xyz(self):
        return self.__balance

    @xyz.setter
    def xyz(self, amount):
        if amount < 0:
            raise ValueError("Balance is negative!")
        self.__balance = amount


account1 = BankAccount("Noman", 1200000)

print(account1.xyz)
account1.xyz = 120
print(account1.xyz)
