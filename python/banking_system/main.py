from services.banking_service import BankingService


def main(banking_service: BankingService):
    while True:
        username = input("당신의 이름을 적어주세요 (종료를 원하시면 '종료'를 입력하세요) : ")

        if username == "종료":
            break
        
        banking_service.find_user(username=username) # 거래 시작 전 사용자 명단 확인
        banking_service.user_menu(username=username) # 거래 시작 


if __name__ == "__main__":
    
    banking_service = BankingService()

    banking_service.add_user('홍길동') # 사용자 추가
    banking_service.add_user('고길동') 

    main(banking_service)