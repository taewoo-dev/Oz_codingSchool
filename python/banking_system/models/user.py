from models.account import Account

class User:
    """
    사용자 클래스
    사용자의 이름과 계좌를 관리
    """

    def __init__(self, username: str) -> None:
        
        self._username = username
        self._account = Account()