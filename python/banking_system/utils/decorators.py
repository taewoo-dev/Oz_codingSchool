from typing import Callable
from utils.exceptions import NegativeAmountError,InsufficientFundsError

def validate_transaction(function: Callable) -> Callable:
    def new_function(amount: int, *args, **kwargs):
        if amount <= 0:
            raise NegativeAmountError
        return function(amount, *args, **kwargs)
    return new_function

def check_balance(balance: int, amount: int) -> None:
    print("check balance")
    if balance - amount < 0:
        raise InsufficientFundsError(balance=balance)
    
@validate_transaction
def process_transaction(amount: int) -> None:
    print(f"Processing transaction : {amount}")





