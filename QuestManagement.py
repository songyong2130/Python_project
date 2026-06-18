from Quest import Quests
from datetime import datetime
#구분선 함수
def separation():
    print("─" * 32)
# 현재 가능한 퀘스트 목록 보여줌
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
# 수락한 퀘스트 보여줌
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
#퀘스트 클리어 함수
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
        clear_input = int(input('클리어할 퀘스트를 입력하세요. (0 입력시 취소)'))
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
#플레이어 퀘스트 수락할수 있는 함수
def Player_Quest(player) :
    while True:
        separation()
        available_quests = Print_Quest(player)
        separation()
        try:
            quest_input = int(input("진행할 퀘스트를 입력하세요. (0 입력시 돌아가기)>> "))
            if quest_input == 0:
                return
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