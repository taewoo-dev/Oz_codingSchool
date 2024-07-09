class InsufficientFundsError(Exception):
    

    def __init__(self, balance: int, message: str="출금 금액보다 잔고가 부족합니다") -> None:

        super().__init__(message)
        self._balance = balance
        self._message = message
    
    def __str__(self) -> str:

        return f"{self._message} : 현재 잔고 {self._balance}원"
    
class NegativeAmountError(Exception):

    
    def __init__(self, message: str="금액으로 음수가 입력되었습니다") -> None:


        super().__init__(message)
        self._message = message
    
    def __str__(self) -> str:

        return self._message
    
class UserNotFoundError(Exception):

    
    def __init__(self, username: str, message: str="고객님의 정보가 존재하지 않습니다") -> None:

        super().__init__(message)
        self._username = username
        self._message = message

    def __str__(self) -> str:
        return f"{self._username} {self._message}"
