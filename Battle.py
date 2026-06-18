from datetime import datetime
from Boss import Bosses

def separation():
    print("─" * 32)

def Challenge_MiniBoss(player):
    separation()
    print('         [미니 보스 도전]')
    
    boss_list = list(Bosses.keys())
    
    for idx, name in enumerate(boss_list, 1):
        info = Bosses[name]
        if name in player.defeated_bosses:
            status = "공략완료"
        else:
            status = f"공략가능 (권장Lv.{info['req_level']})"
        print(f'[{idx}] {name} {status}')
        
    separation()
    try:
        choice = int(input("도전할 보스 번호를 선택하세요 (0 입력시 뒤로가기) >> "))
        if choice == 0:
            return
        if not (1 <= choice <= len(boss_list)):
            print("잘못된 번호입니다.")
            return
            
        selected_boss_name = boss_list[choice - 1]
        boss_data = Bosses[selected_boss_name]
        
        # 1. 영구 처치 완료 여부 검사
        if selected_boss_name in player.defeated_bosses:
            print("❌ 이미 처치 완료된 일회성 보스입니다. 다시 싸울 수 없습니다.")
            return
            
        # 2. 10분(600초) 패배 쿨타임 검사
        now = datetime.now()
        if selected_boss_name in player.boss_timers:
            last_fail = player.boss_timers[selected_boss_name]
            passed_time = (now - last_fail).total_seconds()
            if passed_time < 600:
                rem_sec = int(600 - passed_time)
                print(f"멘탈 회복중... 멘탈 회복 시간: {rem_sec // 60}분 {rem_sec % 60}초")
                return

        b_hp = boss_data['hp']
        b_dmg = boss_data['dmg']
        b_exp = boss_data['exp']
        
        print(f"\n{selected_boss_name}과의 배틀!")
        print(f" 나의 무기: [{player.inventory.equipped_weapon}] (총 공격력: {player.total_dmg()})")
        print(f" 보스 스펙 -> HP: {b_hp} / 공격력: {b_dmg}")
        
        battle_choice = int(input("정말 전투를 시작하겠습니까? (1:시작 / 0:도망) >> "))
        if battle_choice != 1:
            print("잠시 적을 외면합니다.")
            return
            
        # 💡 턴제 루프
        turn = 1
        while player.hp > 0 and b_hp > 0:
            print(f"\n[TURN {turn}] ───────────────────────")
            print(f" 내 HP: {player.hp}/{player.maxHp} | 보스 HP: {b_hp}")
            print(" [1] 공격하기  [2] 도망치기")
            
            try:
                act = int(input("행동을 고르세요 > "))
            except ValueError:
                print("숫자만 입력하세요.")
                continue
                
            if act == 2:
                print("\n💨 긴급 도망에 성공했습니다! (도망 시 10분 제약이 걸리지 않습니다)")
                player.hp = player.maxHp
                return
                
            if act == 1:
                # 플레이어 선제 공격
                p_atk = player.total_dmg()
                b_hp -= p_atk
                print(f" {player.name}의 공격! [{player.inventory.equipped_weapon}]로 {p_atk} 데미지를 입힘")
                
                if b_hp <= 0:
                    break
                    
                # 보스 반격
                player.hp -= b_dmg
                print(f"{selected_boss_name}의 공격! {b_dmg}의 대미지를 입음")
                
                turn += 1
                
        # 결과 처리
        if b_hp <= 0:
            player.victory_boss(selected_boss_name, b_exp)
        elif player.hp <= 0:
            player.defeat_boss(selected_boss_name)

    except ValueError:
        print("올바른 숫자를 작성해 주세요.")