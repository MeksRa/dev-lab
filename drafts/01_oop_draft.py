class Player:
    def __init__(self, nickname: str, attack_power: int) -> None:
        self.nickname = nickname
        self.attack_power = attack_power
        self.hp = 100
        self.is_alive = True

    # behavior => methods
    def take_damage(self, amount: int) -> None:
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.nickname} died!")
        else:
            print(f"{self.nickname} took {amount} damage! HP left: {self.hp}")

    def attack(self, other_player: "Player") -> None:
        print(f"{self.nickname} attacked {other_player.nickname}")
        other_player.take_damage(self.attack_power)


def main() -> None:
    player1: Player = Player("Destroyer", 25)
    player2: Player = Player("Murderer", 10)
    while player1.is_alive and player2.is_alive:
        player1.attack(player2)
        if player2.is_alive:
            player2.attack(player1)


if __name__ == "__main__":
    main()
