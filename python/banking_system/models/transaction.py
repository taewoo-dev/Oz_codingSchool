class Transaction:


    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:

        self._transaction_type = transaction_type
        self._amount = amount
        self._balance = balance

    def __str__(self) -> str:

        return f"거래 유형 : {self._transaction_type}, 거래 금액 : {self._amount}, 거래 후 잔고 : {self._balance} " 
    
    def to_tuple(self) -> tuple:

        return (self._transaction_type, self._amount, self._balance)