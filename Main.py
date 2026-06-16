from Quest import Quests
from Player import Player
from datetime import datetime
#──────데이터──────

#──────유틸───────
def separation():
    print("─" * 32)
def Start_menu():
    menus = [
        ('1','새로시작'),
        ('2','불러오기'),
        ('3','나가기'),
    ]
    for k,v in menus:
        print(f'        [{k}] {v}')
def Main_menu():
    menus = [
        ('1','퀘스트'),
        ('2','진행중인 퀘스트'),
        ('3','퀘스트 클리어'),
        ('4','인벤토리'),
        ('5','미니보스 도전'),
        ('0','로그아웃')
    ]
    for k,v in menus:
        print(f'        [{k}] {v}')
#────────시스템─────────
def Print_Quest(player):
    print('         [퀘스트 목록]')
    available_quests = []

    num = 1
    for name, info in Quests.items():
        if info['grade'] == player.grade:
            print(f'[{num}] {name}    exp:{info["exp"]}')
            available_quests.append(name)
            num += 1

    return available_quests
def show_accept_quest(player):
        separation()
        print('현재 진행중 퀘스트\n')
        num = 1
        now = datetime.now()
        if player.running == {}:
            print('현재 받은 퀘스트가 없습니다.')
        else:
            for name,start_time in player.running.items():
                pass_time = int((now - start_time).total_seconds() / 60)
                print(f'[{num}] {name} 상태 : 진행중 [시작 시간: {start_time.strftime('%H:%M:%S')}]')
                num += 1
def quest_clear(player):
    separation()
    print('현재 진행중 퀘스트')
    num = 1
    if player.running == {}:
        print('현재 받은 퀘스트가 없습니다.')
        return
    running_list = []
    now = datetime.now()

    for name,start_time in player.running.items():
        pass_time = int((now - start_time).total_seconds() / 60)
        base_exp = Quests[name]['exp']
        raise_exp = int(base_exp * (1 + pass_time * 0.01))
        print(f'[{num}] {name} [{start_time.strftime('%H:%M:%S')}] 예상보상: {raise_exp}exp')

        running_list.append(name)
        num += 1
    separation()
    try : 
        clear_input = int(input('클리어할 퀘스트를 입력하세요.'))
        if clear_input == 0:
            return
        if 1 <= clear_input <= len(running_list):
            select_quest = running_list[clear_input - 1]
            player.complete_quest(select_quest)
        else: 
            print('번호에 없는 퀘스트입니다.')
    except ValueError:
        print('숫자만 입력하세요.')
#────────메인 기능─────────
def Player_Quest(player) :
    while True:
        separation()
        available_quests = Print_Quest(player)
        separation()
        try:
            quest_input = int(input("진행할 퀘스트를 입력하세요. (0 입력시 돌아가기)>> "))

            if 1 <= quest_input <= len(available_quests):
                selected_quest = available_quests[quest_input - 1]
                player.accept_quest(selected_quest)
                return
            else:
                print('번호에 없는 퀘스트 입니다.')
        except ValueError:
            print('문자열을 입력하지 마세요.')
            continue
        if quest_input == 0:
            return
print('[평범한 학생인 줄 알았던 내게 퀘스트 창이 보이기 시작했는데 졸업하기 위해선 최종보스를 잡아야하는 건에 대하여]')
while True:
    Start_menu()
    Start_input = (input(' >> '))
    if Start_input == '1':
        Name_input = input('이름을 입력하세요. (기본: 황금독수리온세상을놀라게하다) 취소하려면 0입력 >>')
        if Name_input == "":
            player = Player('황금독수리온세상을놀라게하다')
        elif Name_input == "0":
            print('취소됨')
            continue
        else:
            player = Player(Name_input)
        print('새 게임을 시작합니다.')
        break
    elif Start_input == '2':
        print('불러오기 할 내용이 없습니다.')
        continue
    elif Start_input == '3':
        print('게임을 종료합니다.')
        exit()
while True:
    try:
        separation()
        print('             [메인]')
        player.show_info()
        Main_menu()
        separation()
        player_input = int(input('당신의 입력 > '))
        if player_input == 1:
            Player_Quest(player)
        elif player_input == 2:
            show_accept_quest(player)
        elif player_input == 3:
            quest_clear(player)
        elif player_input == 4:
            print(4)
        elif player_input == 5:
            print(5)
        elif player_input == 0:
            print(0)
            break
        else : 
            print('잘못된 입력')
            continue
    except ValueError:
        print('문자열을 입력하지마세요.')
        continue