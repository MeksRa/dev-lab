class GameConfig:
    START_HAND_SIZE = 6
    MAX_HAND_SIZE = 10

    TURN_DRAW_COUNT = 2
    PASS_DRAW_COUNT = 1

    HERO_START_HP = 25
    BOSS_START_HP = 25


class Card:
    """Represents an individual card in the game."""

    def __init__(self, card_id: int, description: str):
        self.card_id = card_id
        self.description = description

    def __repr__(self) -> str:
        return f"<{self.description}>"


class Deck:
    """Manages a collection of cards, handling drawing and empty states."""

    def __init__(self, cards_dict: dict):
        self.cards = cards_dict

    def draw(self) -> Card | None:
        if self.is_empty():
            return None
        card_id, card_obj = self.cards.popitem()
        return card_obj

    def is_empty(self) -> bool:
        return len(self.cards) == 0


class Player:
    """Represents a game participant (Hero or Boss) with stats, deck, and hand."""

    def __init__(self, name: str, hp: int, deck_cards: dict):
        self.name = name
        self.hp = hp
        self.deck = Deck(deck_cards)
        self.hand: list[Card] = []
        self.graveyard: list[Card] = []

    def draw_cards(self, count: int) -> int:
        """Draws cards into the player's hand, respecting the hand limit."""
        drawn_count = 0
        for _ in range(count):
            if len(self.hand) >= GameConfig.MAX_HAND_SIZE:
                print(
                    f"[{self.name}] Hand is full ({GameConfig.MAX_HAND_SIZE} cards)! Cannot draw more."
                )
                break

            card = self.deck.draw()
            if card is None:
                print(f"[{self.name}] Deck is empty!")
                break

            self.hand.append(card)
            drawn_count += 1
        return drawn_count

    def show_status(self) -> None:
        print(f"--- Status: {self.name} (HP: {self.hp}) ---")
        print(f"Cards in deck: {len(self.deck.cards)}")
        print(f"Hand ({len(self.hand)}/{GameConfig.MAX_HAND_SIZE}): {self.hand}")
        print("-" * 35)


class CardGameManager:
    """Manages the main game lifecycle, turns, and interactions."""

    def __init__(self):
        hero_initial_deck = {i: Card(i, f"HeroCard_{i}") for i in range(1, 25)}
        boss_initial_deck = {i: Card(i, f"BossCard_{i}") for i in range(1, 25)}

        self.hero = Player("Hero", GameConfig.HERO_START_HP, hero_initial_deck)
        self.boss = Player("Boss", GameConfig.BOSS_START_HP, boss_initial_deck)

        self.is_running = True
        self.current_turn = "hero"
        self.game_phase = "menu"

    def start_game(self) -> None:
        print("=== GAME STARTED ===")
        drawn = self.hero.draw_cards(GameConfig.START_HAND_SIZE)
        print(f"Hero drew starting cards: {drawn} cards.")
        self.hero.show_status()

    def player_turn_draw(self) -> None:
        print("\n>>> Hero's turn start: drawing +2 cards")
        drawn = self.hero.draw_cards(GameConfig.TURN_DRAW_COUNT)
        print(f"Added to hand: {drawn} cards.")
        self.hero.show_status()

    def player_pass_turn(self) -> None:
        print("\n>>> Hero passes turn: bonus draw +1 card")
        drawn = self.hero.draw_cards(GameConfig.PASS_DRAW_COUNT)
        print(f"Added to hand: {drawn} card.")
        self.hero.show_status()


# --- Console Demonstration ---
if __name__ == "__main__":
    game = CardGameManager()

    # 1. Start the game
    game.start_game()

    # 2. Simulate turn 1 draw (+2 cards)
    game.player_turn_draw()

    # 3. Simulate turn 2 pass (pass turn and draw +1 card)
    game.player_pass_turn()
