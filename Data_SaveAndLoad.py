import json
import os
from datetime import datetime

# 저장될 파일 명칭 정의
SAVE_FILE = "SaveData.json"

#데이터 저장 함수
def save_file(player):
        # 플레이어 객체 내부의 필요한 실시간 데이터를 추출하여 딕셔너리로 만듬
        save_data = {
            "name": player.name,
            "level": player.level,
            "exp": player.exp,
            "grade": player.grade,
            "title": player.title,
            "equipped_weapon": player.inventory.equipped_weapon,  # 현재 장착 무기
            "items": player.inventory.items,                      # 가방 속 아이템 리스트
            "running_quests": {name: start_time.isoformat() for name, start_time in player.running.items()}, # 진행중 퀘스트 시간 문자열로 변환하여 저장
            "ended_quests": player.ended,
            "defeated_bosses" : player.defeated_bosses,
            "boss_timers" : {boss_name: fail_time.isoformat() for boss_name, fail_time in player.boss_timers.items()} # 보스 패널티 시간 문자열로 변환한뒤 저장
        }
    
        with open(SAVE_FILE, "w", encoding="utf-8",) as f: 
            json.dump(save_data, f, ensure_ascii=False, indent=4) # 저장함

#데이터 불러오는 함수
def Load_file(PlayerClass):
    # os 모듈을 활용해 세이브 파일이 진짜 컴퓨터에 있는지 체크
    if not os.path.exists(SAVE_FILE):
        print("\n 저장 파일이 존재하지 않음")
        return None
        
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
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
        