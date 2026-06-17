GRADE_WEAPONS = {
    1: "시나공|프로그래밍기능사 필기[타격폼]",
    2: "C++,Node.js등 전공서적[투척,타격폼]",
    3: "맥북[프로젝트 진행중]",
    "취업예정자": "포트폴리오[강함]"
}

class Inventory:
    def __init__(self, grade):
        self.items = []  # 소비 아이템 및 이전에 끼던 장비들이 들어갈 배낭
        self.equipped_weapon = GRADE_WEAPONS.get(grade, "맨손") # 현재 장착 무기

    # 학년이 올라 무기가 바뀔 때 기존 장비를 인벤토리로 보내는 로직 추가
    def update_weapon(self, new_grade):
        if new_grade in GRADE_WEAPONS:
            #현재 끼고 있던 장비를 보관함에 저장
            old_weapon = self.equipped_weapon
            self.items.append(old_weapon)
            
            # 새 학년에 맞는 신규 무기 장착
            self.equipped_weapon = GRADE_WEAPONS[new_grade]
            
            print(f"\n---------------------------------------")
            print(f" 장비 변경 및 인벤토리 이동")
            print(f" [기존 장비 해제] -> [{old_weapon}]이(가) 가방으로 들어갔습니다.")
            print(f" [신규 장비 착용] -> [{self.equipped_weapon}]을(를) 장착했습니다.")
            print(f"---------------------------------------\n")

    def show_inventory(self):
        print("\n------ 인벤토리 ------")
        print(f" 장착 중인 무기: {self.equipped_weapon}")
        print(" 보유 중인 아이템 목록:")
        if not self.items:
            print("  - (비어 있음)")
        else:
            num = 1
            for item in self.items:
                print(f"  - [{num}] {item}")
                num += 1
        print("---------------------------------------\n")