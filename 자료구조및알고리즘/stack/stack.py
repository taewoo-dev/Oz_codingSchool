class Stack:
    def __init__(self) -> None:
        self._items = [] # 데이터 저장을 위한 빈 리스트 생성

    def push(self,val):
        self._items.append(val) # 단순 대입연산으로 단위 시간연산

    def pop(self):
        try:
            return self._items.pop() # 단순 제거 연산으로 단위 시간연산
        except IndexError:
            print("Stack is Empty")
    
    def top(self):
        try:
            return self._items[-1] # 단순 참조 단위시간 연산
        except IndexError:
            print("Stack is Empty")

    def __len__(self):
        return len(self._items)
    
    def isEmpty(self):
        return self.__len__()
    
arraystack = Stack()

            
from stack import Stack

arraystack = Stack()

for i in "HELLO":
    arraystack.push(i)

print("".join(arraystack._items))
print(arraystack.top())
print(arraystack.pop())
print(arraystack._items)
print(arraystack.top())
