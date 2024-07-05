# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random
import string

ALPHABET = string.ascii_lowercase

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]


# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
    ---""",
]


class HangmanGame:

    def __init__(self) -> None:

        self.words = []
        self.hangman_pics = []
        self.hangman_word = ''
        self.hidden_word = []
        self.life = 0
        self.count = 0
        self.answer_word = []

    def start_setting(self,words : list,hangman_pics : list) -> None:

        self.words = words
        self.hangman_pics = hangman_pics
        self.life = len(self.hangman_pics)
        self.hangman_word = random.choice(words) 
        self.hidden_word = len(self.hangman_word)*['_']

        self.hangman_pics.reverse()

    def display(self) -> None:

        print(" ".join(self.hidden_word))
        print(self.hangman_pics[self.life-1])

    def start_ment(self) -> None:

        print("hangman game을 시작합니다")

        print(f"게임 시작 시 목숨은 {self.life}개이며, 총 10회의 정답을 맞출 기회가 주어집니다")


    def user_input_check(self,user_input : str) -> bool:
        
        if len(user_input) != 1:
            print("알파벳이 여러개 입력되었습니다. 다시 시도해주세요")
            return True
        elif user_input not in ALPHABET:
            print("알파벳이 아닌 글자가 입력되었습니다. 다시 시도해 주세요")
            return True 

        return False
    
    def uncover_text(self,user_input : str) -> None:
        for index, value in enumerate(self.hangman_word):
            if value == user_input:
                    self.hidden_word[index] = user_input

    def view_life(self) -> None:

        print(f"현재 남은 목숨은 [{self.life}/7] 입니다")

        print(f"현재 시도 횟수는 [{self.count}/10] 입니다")

        print(f"현재 확인한 알파벳은 [{self.answer_word}] 입니다")

    def check_duplicates(self,user_input : str) -> bool:

        if user_input in self.answer_word:
            print("이미 확인한 알파벳입니다, 다시 시도해주세요")
            return True
        else:
            self.answer_word.append(user_input)
            return False


    
    def play(self) -> None:
        
        self.start_ment()

        self.display()

        while True:
            
            try:

                user_input = input("생각하는 알파벳 단어 하나를 입력해주세요!, 게임의 종료를 원하시면 '종료'를 입력해주세요").strip().lower()

                if user_input == "종료":

                    print("게임을 종료합니다")
                    break

                if self.user_input_check(user_input):
                    continue

                if self.check_duplicates(user_input):
                    continue

                if user_input in self.hangman_word:

                    print(f"{user_input}은 맞습니다!")

                    self.uncover_text(user_input)

                    self.count += 1

                    self.view_life()

                    self.display()
                    

                    if "".join(self.hidden_word) == self.hangman_word:
                        print("정답을 맞추셨습니다~!~!~! 게임을 종료합니다")
                        break

                else:
                    self.life -= 1

                    self.count += 1

                    print("당신은 틀렸습니다...")

                    self.view_life()

                    self.display()
                    
                    if self.life == 0 or self.count == 10:

                        print("당신이 사람을 죽였습니다...")

                        print("게임을 종료합니다")

                        break
            except:
                print("오류가 발생했습니다. 값을 다시 입력해 주세요")

if __name__ == "__main__":
    game = HangmanGame()
    game.start_setting(words,hangman_pics)
    game.play()
