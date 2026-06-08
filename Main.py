#──────util───────
def separation():
    print("─" * 32)
def Main_menu():
    menus = [
        ('1','퀘스트'),
        ('2','인벤토리'),
        ('3','미니보스 도전'),
        ('0','로그아웃')
    ]
    for k,v in menus:
        print(f'        [{k}] {v}')
#────────main─────────

while True:
    try:
        separation()
        Main_menu()
        separation()
        player_input = int(input('당신의 입력 > '))
        if player_input == 1:
            print(1)
        elif player_input == 2:
            print(2)
        elif player_input == 3:
            print(3)
        elif player_input == 0:
            print(0)
            break
        else : 
            print('잘못된 입력')
            continue
    except ValueError:
        print('문자열을 입력하지마세요.')
        continue