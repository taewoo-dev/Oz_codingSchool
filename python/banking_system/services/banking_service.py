from models.user import User
from utils.exceptions import UserNotFoundError 

class BankingService:

    
    def __init__(self) -> None:
        
        self._users = []

    def add_user(self, username: str) -> None:

        self._user = User(username)
        self._users.append(self._user)

    def find_user(self, username: str) -> User:

        try:
            for user in self._users:
                if user._username == username:
                    return user
            raise UserNotFoundError(username=username)
        except UserNotFoundError as e:
            print(e)

    def user_menu(self, username: str) -> None:

        for user in self._users:
            if user._username == username:
                while True:
                    try:
                        menu = input("원하시는 거래를 선택해주세요. [입금, 출금, 잔고 확인, 거래 내역], 거래 종료를 원하신다면 '종료'를 입력해주세요").strip()
                        
                        if menu == "종료":
                            print("거래를 종료합니다")
                            break
                        elif menu == "입금":
                            amount = int(input("원하시는 입금 금액을 입력하세요 : "))
                            user._account.deposit(amount)
                        elif menu == "출금":
                            amount = int(input("원하시는 출금 금액을 입력하세요 : "))
                            user._account.withdraw(amount)
                        elif menu == "잔고 확인":
                            print(f"{username}님의 잔액은 {user._account.get_balance()}원 입니다")
                        elif menu == "거래 내역":
                            for transaction in user._account.get_transactions():
                                print(transaction)
                        
                    except Exception as e:
                        print(e)