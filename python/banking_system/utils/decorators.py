from typing import Callable
from utils.exceptions import NegativeAmountError,InsufficientFundsError

def validate_transaction(function: Callable) -> Callable:
    def new_function(amount: int, *args, **kwargs):
        """
        거래 금액이 음수이거나 0원으로 입력되었을 시 오류를 발생시키는 함수
        """
        if amount <= 0:
            raise NegativeAmountError
        return function(amount, *args, **kwargs)
    return new_function

def check_balance(balance: int, amount: int) -> None:
    """
    출금 시 잔액이 출금 금액보다 적을 경우 오류를 발생시키는 함수
    """
    print("check balance")
    if balance - amount < 0:
        raise InsufficientFundsError(balance=balance)
    
@validate_transaction
def process_transaction(amount: int) -> None:
    """
    거래 과정 중 거래 금액을 보여주는 함수
    """
    print(f"Processing transaction : {amount}")





