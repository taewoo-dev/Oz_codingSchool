from models.transaction import Transaction
from utils.decorators import process_transaction,check_balance

class Account:


    bank_name = None

    @classmethod
    def get_bank_name(cls) -> str:

        return Account.bank_name
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:

        Account.bank_name = name

    def __init__(self) -> None:

        self.__balance = 0
        self._transactions = []

    def deposit(self, amount: int) -> None:

        process_transaction(amount)

        self.__balance += amount
        self._transactions.append(Transaction("입금", amount, self.__balance))
        

    def withdraw(self, amount: int) -> None:

        process_transaction(amount)
        check_balance(self.__balance,amount)

        self.__balance -= amount
        self._transactions.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        
        return self.__balance
    
    def get_transactions(self) -> list:

        return self._transactions