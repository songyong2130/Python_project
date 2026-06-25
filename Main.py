from Player import Player
from Battle import Challenge_MiniBoss
import QuestManagement
from Data_SaveAndLoad import save_file, Load_file, check_save_slots

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
        ('6','저장하기'),
        ('0','로그아웃')
    ]
    for k,v in menus:
        print(f'        [{k}] {v}')
def select_slot_menu(title_mode="불러오기"):
    while True:
        separation()
        print(f"         [{title_mode} 슬롯 선택]")
        slots = check_save_slots()
        for num, info in slots.items():
            print(f"        [{num}] 슬롯 {num} : {info}")
        print("        [0] 돌아가기")
        separation()
        
        try:
            slot_input = int(input(f"{title_mode}할 슬롯 번호를 선택하세요 >> "))
            if slot_input == 0:
                return None
            if 1 <= slot_input <= 3:
                return slot_input
            print("잘못된 슬롯 번호입니다.")
        except ValueError:
            print("숫자만 입력해 주세요.")
#────── 메인 게임 안───────
print('[평범한 소마고학생인 줄 알았던 내게 퀘스트 창이 보이기 시작했는데 졸업하기 위해선 최종보스를 잡아야하는 건에 대하여]')

current_slot = 1
while True:
    Start_menu()
    Start_input = (input(' >> '))
    if Start_input == '1':
        Name_input = input('이름을 입력하세요. (Enter시 기본: 김철수) 취소하려면 0입력 >>')
        if Name_input == "":
            player = Player('김철수')
        elif Name_input == "0":
            print('취소됨')
            continue
        else:
            player = Player(Name_input) #새 겍체 생성

        slot = select_slot_menu("저장할 슬롯")
        if slot is None:
            print("캐릭터 생성을 취소하셨습니다.")
            continue
        current_slot = slot
        print('새 게임을 시작합니다.')
        break

    elif Start_input == '2':
        slot = select_slot_menu("불러오기")
        if slot is None:
            continue
        
        Load_data = Load_file(Player,slot)
        if Load_data is not None:
            player = Load_data
            current_slot = slot
            break
        else:
            continue
    elif Start_input == '3':
        print('게임을 종료합니다.')
        exit()
while True:
    save_file(player,current_slot)
    print('자동 저장!')
    try:
        separation()
        print('             [메인]')
        player.show_info()
        Main_menu()
        separation()
        player_input = int(input('당신의 입력 > '))
        if player_input == 1:
            QuestManagement.Player_Quest(player)
        elif player_input == 2:
            QuestManagement.show_accept_quest(player)
        elif player_input == 3:
            QuestManagement.quest_clear(player)
        elif player_input == 4:
            player.inventory.show_inventory()
        elif player_input == 5:
            Challenge_MiniBoss(player)
        elif player_input == 6:
            save_file(player)
            print('저장 완료! 데이터가 저장되었습니다.')
        elif player_input == 0:
            print("로그아웃 되었습니다.")
            break
        else : 
            print('잘못된 입력')
            continue
    except ValueError:
        print('문자열을 입력하지마세요.')
        continue