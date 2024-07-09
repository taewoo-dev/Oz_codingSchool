from models.account import Account

class User:


    def __init__(self, username: str) -> None:
        
        self._username = username
        self._account = Account()