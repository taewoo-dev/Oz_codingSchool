from models.transaction import Transaction
from utils.decorators import process_transaction,check_balance

class Account:
    """
    계좌 클래스
    잔고와 거래 내역을 관리
    매서드: 입금, 출금, 잔고확인, 거래내역 확인
    """

    bank_name = None

    @classmethod
    def get_bank_name(cls) -> str:

        return Account.bank_name
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:

        Account.bank_name = name

    def __init__(self) -> None:


        self.__balance = 0 # private 속성으로 잔액 생성
        self._transactions = []

    def deposit(self, amount: int) -> None:
        """
        입금 매서드 
        """

        process_transaction(amount) # 거래 금액 확인 함수

        self.__balance += amount
        self._transactions.append(Transaction("입금", amount, self.__balance)) # 거래 인스턴스 생성 후 transaction 리스트에 추가
        

    def withdraw(self, amount: int) -> None:
        """
        출금 매서드
        """

        process_transaction(amount) # 거래 금액 확인 함수
        check_balance(self.__balance,amount) # 출금 금액이 잔고보다 많을 시 오류 발생 함수

        self.__balance -= amount
        self._transactions.append(Transaction("출금", amount, self.__balance)) # 거래 인스턴스 생성 후 trnasaction 리스트에 추가

    def get_balance(self) -> int:
        """
        잔고 확인 매서드
        """
        return self.__balance 
    
    def get_transactions(self) -> list:
        """
        거래 내역 확인 매서드
        """

        return self._transactions