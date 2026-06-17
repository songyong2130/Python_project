GRADE_WEAPONS = {
    1: "키보드&마우스",
    2: "전공서적(두꺼움)",
    3: "맥북(프로젝트 진행중)",
    "취업예정자": "포트폴리오(강함)"
}

class Inventory:
    def __init__(self, grade):
        self.items = []  # 소비 아이템이나 기타 아이템을 담을 리스트 (추후 확장용)
        self.equipped_weapon = GRADE_WEAPONS.get(grade, "맨손") # 현재 장착 무기

    # 학년이 올랐을 때 무기를 교체해주는 메서드
    def update_weapon(self, new_grade):
        if new_grade in GRADE_WEAPONS:
            self.equipped_weapon = GRADE_WEAPONS[new_grade]
            print(f"학년이 올라 무기가 자동으로 변경되었습니다!")
            print(f"현재 장착 무기: [{self.equipped_weapon}]")

    # 인벤토리 상태 보기 (Main.py 4번 메뉴용)
    def show_inventory(self):
        print("\n ====== 인벤토리 ======")
        print(f" 장착 중인 무기: {self.equipped_weapon}")
        print(" 보유 중인 아이템:")
        if not self.items:
            print("  - 비어 있음")
        else:
            for item in self.items:
                print(f"  - {item}")
        print("=========================")