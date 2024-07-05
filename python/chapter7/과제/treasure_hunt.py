import random


class TreasureHunt():

    def __init__(self) -> None:
        self.board = []
        self.__treasure_position = []
        self.player_position = []
        self.board_size = 0
        self.count = 0
        
# 게임 초기화
    def initialize_game(self,n : int) -> None:
        
        self.board_size = n 

        for i in range(n):
            for j in range(n):
                self.board.append([i,j])
        
        self.treasure_position = random.choice(self.board)
        self.player_position = random.choice(self.board)

# 화면 출력
    def display(self) -> None:
        pass
    
# 거리 계산
    def calculate_distance(self) -> None:
        distance = 0
        distance += abs(self.treasure_position[0]-self.player_position[0])
        distance += abs(self.treasure_position[1]-self.player_position[1])
        print(f"현재 위치에서 보물은 {distance}칸 이동하면 찾을 수 있습니다")


# 플레이어 이동
    def move_player(self,direction) -> None:
        
        self.count += 1

        print(f'현재 당신은 {self.player_position}에 있습니다')

        if direction == '북' and self.player_position[0] < self.board_size-1:
            print("북쪽으로 한칸 이동합니다")
            self.player_position[0] += 1
        elif direction == '남' and self.player_position[0] > 0:
            print("남쪽으로 한칸 이동합니다")
            self.player_position[0] -= 1
        elif direction == '서' and self.player_position[1] > 0:
            print("서쪽으로 한칸 이동합니다")
            self.player_position[1] -= 1
        elif direction == '동' and self.player_position[1] < self.board_size-1:
            print("동쪽으로 한칸 이동합니다")
            self.player_position[1] += 1
        else:
            print("해당구역으로는 갈 수 없습니다")
            self.count -= 1
           
    
    # 게임 실행
    def play_game(self) -> None:

        print("보물찾기 게임을 시작합니다")

        while True:
            
            try:
                print(f"총 {self.count}회 시도중")
                print(f"당신의 현재 위치 : {self.player_position}")
                direction = input("방향을 입력하세요 ['북','남','서','동'] 힌트를 원한다면 '힌트'를 입력하세요").strip()

                if direction == '종료':
                    break
                
                if direction == '힌트':
                    self.calculate_distance()
                    continue

                self.move_player(direction)

                if self.player_position == self.treasure_position:
                    print("보물을 찾았습니다!!!!")
                    break

            except:
                print("잘못된 값이 입력되었습니다. 다시 입력해주세요")

# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  # 보드 크기를 5x5로 설정
    game = TreasureHunt()
    game.initialize_game(board_size)
    game.play_game()