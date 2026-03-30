import numpy as np

accounts = []
num = 0

class Account:
    def __init__(self, name, income, password):
        self.user_name = name
        self.user_balance = income
        self.user_account_number = self.make_num()
        self.user_password = password
        accounts.append({
            "user_account_number" : self.user_account_number,
            "user_name" : self.user_name,
            "user_password" : self.user_password,
            "user_balance" : self.user_balance
        })
    def make_num(self):
        rng = np.random.default_rng()
        return rng.integers(100_000_000, 1_000_000_000) # 정수형(최솟값포함, 최댓값미포함)
class AccountValid:
    def valid(self, account_number, password):
        for acc in accounts:
            if acc["user_account_number"] == account_number and acc["user_password"] == password :
                print("로그인 되었습니다.")
                return True
        print("로그인 실패")
        return False
class Banking:
    def __init__(self, account):
        self.account = account
    def deposite(self, amount):
        self.account.user_balance += amount
        print(f"잔액 : {self.account.user_balance}원")
    def withdrawal(self, amount):
        if self.account.user_balance >= amount:
            self.account.user_balance -= amount
            print(f"잔액 : {self.account.user_balance}원")
        else : 
            print(f"잔액 부족. 고객님의 잔액은 {self.account.user_balance}입니다.")
    def inquiry(self):
        print(f"잔액 : {self.account.user_balance}원")

a_account = Account("hyemin", 10000, "1234")
validator = AccountValid()

if validator.valid(a_account.user_account_number, "1234"):
    bank = Banking(a_account)
    bank.inquiry()
    bank.deposite(500)
    bank.withdrawal(300)