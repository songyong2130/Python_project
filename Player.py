from datetime import datetime
from Quest import Quests
from Inventory import Inventory 

class Player :
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.grade = 1
        self.title = '[1학년 신입생]'
        self.inventory = Inventory(self.grade) # 
        self.running = {}
        self.ended = []

    def gain_exp(self,amount) :
        self.exp += amount
        print(f'{amount}exp 획득!')
        while self.exp >= self.remain_exp():
            self.exp -= self.remain_exp()
            self.Level_up()

    def complete_quest(self, quest_name):
        if quest_name not in self.running:
            print("진행 중인 퀘스트가 아닙니다.")
            return

        start_time = self.running[quest_name]
        now = datetime.now()
        
        duration_min = int((now - start_time).total_seconds() / 60)
        base_exp = Quests[quest_name]['exp']
        
        bonus_ratio = duration_min * 0.02
        final_exp = int(base_exp * (1 + bonus_ratio))

        print(f'\n★ 퀘스트 클리어: {quest_name} ★')
        print(f'진행 시간: {duration_min}분')
        print(f'보상: 기본 {base_exp} exp + 시간 보너스 {int(base_exp * bonus_ratio)} exp = 총 {final_exp} exp')

        self.gain_exp(final_exp)
        self.running.pop(quest_name)  
        self.ended.append(quest_name) 

    def accept_quest(self,quest_name):
        if quest_name in self.running:
            print('이미 퀘스트를 받았습니다.')
            return
        self.running[quest_name] = datetime.now()
        print('퀘스트 수락!')

    def remain_exp(self):
        if self.grade == 2:
            return 1500 + (self.level) * 300
        elif self.grade == 3:
            return 2000 + (self.level + 5) * 1000
        else:
            return 1000 + (self.level - 1) * 100

    def show_info(self):
        print(f'{self.name} \n 학년: {self.grade}학년 \n 칭호: {self.title} \n 무기: {self.inventory.equipped_weapon} \n 레벨: Lv.{self.level} \n 레벨업까지 남은 exp: {self.exp}/{self.remain_exp()}\n')

    def Level_up(self):
        self.level += 1
        print(f' 레벨 업! \n 현재 레벨: Lv.{self.level}')

        if self.level > 40:
            print(f" 축하합니다! {self.name}님은 Lv.{self.level}에 도달하여")
            print("[졸업]하셨습니다! ")
            print('게임을 종료합니다.')
            exit() 

        # [레벨 40] 취업예정자 진급
        elif self.level == 40:
            if self.grade != '취업예정자':
                self.grade = '취업예정자'
                self.title = "[졸업예정 취업솔져]" 
                print(f"축하합니다! {self.grade}로 진급했습니다! (최종 보스가 해금됩니다.)")
                print(f"새로운 칭호 획득: {self.title}")
                self.inventory.update_weapon(self.grade)

        # [레벨 30 이상] 3학년 진급
        elif self.level >= 30:
            if self.grade != 3:
                self.grade = 3
                self.title = "[3학년 프로젝트 헌터]" 
                print(f"축하합니다! {self.grade}학년으로 진급했습니다! (새로운 퀘스트가 해금됩니다)")
                print(f"새로운 칭호 획득: {self.title}")
                self.inventory.update_weapon(self.grade)
                
        # [레벨 15 이상] 2학년 진급
        elif self.level >= 15:
            if self.grade != 2:
                self.grade = 2
                self.title = "[2학년 협업의 마스터]" 
                print(f"축하합니다! {self.grade}학년으로 진급했습니다! (새로운 퀘스트가 해금됩니다)")
                print(f"새로운 칭호 획득: {self.title}")
                self.inventory.update_weapon(self.grade)