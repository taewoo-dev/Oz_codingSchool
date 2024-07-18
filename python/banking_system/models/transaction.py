class Transaction:
    """
    거래 클래스
    거래의 종류와 거래 금액, 잔고를 관리하는 클래스
    """


    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:

        self._transaction_type = transaction_type
        self._amount = amount
        self._balance = balance

    def __str__(self) -> str:

        return f"거래 유형 : {self._transaction_type}, 거래 금액 : {self._amount}, 거래 후 잔고 : {self._balance} " 
    
    def to_tuple(self) -> tuple:
        """
        거래 내역을 튜플 형식으로 반환하는 매서드
        """
        return (self._transaction_type, self._amount, self._balance)