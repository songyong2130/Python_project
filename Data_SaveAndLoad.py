import json
import os
from datetime import datetime

def get_save_file_name(slot_num):
    return f"SaveData_{slot_num}.json"

def check_save_slots():
    slots_status = {}
    for i in range(1, 4):
        file_name = get_save_file_name(i)
        if os.path.exists(file_name):
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    data = json.load(f)
                slots_status[i] = f"Lv.{data['level']} {data['name']}"
            except Exception:
                slots_status[i] = "데이터 손상됨"
        else:
            slots_status[i] = "비어 있음"
    return slots_status

#데이터 저장 함수
def save_file(player, slot_num):
    save_data = {
        "name": player.name,
        "level": player.level,
        "exp": player.exp,
        "grade": player.grade,
        "title": player.title,
        "equipped_weapon": player.inventory.equipped_weapon,
        "items": player.inventory.items,
        "running_quests": {name: start_time.isoformat() for name, start_time in player.running.items()},
        "ended_quests": player.ended,
        "defeated_bosses" : player.defeated_bosses,
        "boss_timers" : {boss_name: fail_time.isoformat() for boss_name, fail_time in player.boss_timers.items()}
    }

    file_name = get_save_file_name(slot_num)
    with open(file_name, "w", encoding="utf-8") as f: 
        json.dump(save_data, f, ensure_ascii=False, indent=4)

#데이터 불러오는 함수
def Load_file(PlayerClass, slot_num):
    file_name = get_save_file_name(slot_num)
    if not os.path.exists(file_name):
        print("\n[시스템] 해당 슬롯에 저장 파일이 존재하지 않습니다.")
        return None
        
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
            
    # 파일에서 가져온 'name'으로 일단 플레이어 객체 틀잡기
    player = PlayerClass(data["name"])
        
    # 나머지 스탯과 데이터를 JSON 파일에서 통째로 덮어씌움
    player.level = data["level"]
    player.exp = data["exp"]
    player.grade = data["grade"]
    player.title = data["title"]
    player.inventory.equipped_weapon = data["equipped_weapon"]
    player.inventory.items = data["items"]
    player.ended = data["ended_quests"]
    player.defeated_bosses = data["defeated_bosses"]
    player.boss_timers = data["boss_timers"]
    # 문자열로 저장한 시간 데이터들은 다시 datetime객체로 복구
    player.running = {name: datetime.fromisoformat(time_str) for name, time_str in data["running_quests"].items()}
    timers = data.get("boss_timers", {}) #혹시모를 데이터 불러오기로 오류 생김 방지
    player.boss_timers = {boss_name: datetime.fromisoformat(time_str) for boss_name, time_str in timers.items()}
    
    # 배틀 스탯 재계산
    player.maxHp = 100 + (player.level * 50)
    player.hp = player.maxHp
    player.atk = 10 + (player.level * 4)
        
    print(f"\n {player.name}의 데이터 불러옴 (Lv.{player.level})")
    return player # 복구 완료된 플레이어 객체를 메인으로 돌려보냄
        