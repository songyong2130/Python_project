from datetime import datetime
class Player :
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.grade = 1
        self.running = {}
        self.ended = []
    def gain_exp(self,amount) :
        self.exp += amount
    def accept_quest(self,quest_name):
        if quest_name in self.running:
            print('이미 퀘스트를 받았습니다.')
            return
        self.running[quest_name] = datetime.now()
        print('퀘스트 수락!')
    def remain_exp(self):
        return 100 + (self.level - 1) * 30
    def show_info(self):
        print(f'{self.name} \n 학년: {self.grade}학년 \n 레벨: Lv.{self.level} \n 레벨업까지 남은 exp: {self.exp}/{self.remain_exp()}\n')
    def Level_up(self):
        self.level += 1
        print(f'레벨 업! \n 현재 레벨: {self.level}')