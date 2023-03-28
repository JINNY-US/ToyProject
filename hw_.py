import random


class Player:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power

    def normal_attack(self, monster):
        damage = random.randint(self.power - 2, self.power + 2)
        monster.hp -= damage
        print(f"{self.name}이(가) {monster.name}에게 일반공격으로 {damage}의 데미지를 입혔습니다.")

    def magic_attack(self, monster):
        if self.mp >= 1:
            self.mp -= 3
            damage = random.randint(self.power, self.power + 5)
            monster.hp -= damage
            print(f"{self.name}이(가) {monster.name}에게 마법공격으로 {damage}의 데미지를 입혔습니다.")
        else:
            print(f"{self.name}의 MP가 부족합니다.")


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def normal_attack(self, player):
        damage = random.randint(self.power - 1, self.power + 1)
        player.hp -= damage
        print(f"{self.name}이(가) {player.name}에게 일반공격으로 {damage}의 데미지를 입혔습니다.")


player_name = input("플레이어의 이름을 입력하세요: ")
player = Player(player_name, 50, 20, 10)
monster = Monster("슬라임", 30, 8)

print(f"{player.name} vs {monster.name} 전투를 시작합니다!")

while player.hp > 0 and monster.hp > 0:
    print("="*20)
    print(f"{player.name}: HP {player.hp}, MP {player.mp}")
    print(f"{monster.name}: HP {monster.hp}")
    print("="*20)

    choice = input("어떤 공격을 하시겠습니까? (1. 일반공격 / 2. 마법공격) ")
    if choice == "1":
        player.normal_attack(monster)
    elif choice == "2":
        player.magic_attack(monster)
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        continue

    if monster.hp <= 0:
        print(f"{player.name}이(가) {monster.name}을(를) 물리쳤습니다!")
        print("승리!")
        break

    monster.normal_attack(player)

    if player.hp <= 0:
        print(f"{player.name}이(가) 전투에서 패배했습니다.")
        print("패배!")
        break
