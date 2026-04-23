class Bank:

    def __init__(self, balance: List[int]):
        self.balance=balance
        self.n=len(balance)
    
    def _valid(self, account: int)-> bool:
        return 1<=account<=self.n
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        balance=self.balance

        if not ( self._valid(account1) and self._valid(account2)):
            return False
        
        elif balance[account1-1]>= money :
            balance[account1-1]=balance[account1-1]-money
            balance[account2-1]=balance[account2-1]+money
            return True
        else:
            return False
        

    def deposit(self, account: int, money: int) -> bool:
        balance=self.balance
    
        if self._valid(account):
            balance[account-1]=balance[account-1]+money
            return True
        else:
            return False

        
    def withdraw(self, account: int, money: int) -> bool:
        balance=self.balance
  
        if not self._valid(account) or balance[account-1]<money:
            return False
        else:
            balance[account-1]=balance[account-1]-money
            return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)