from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return self.cards.__len__

    def add(self, card: Card):
        if any(card.name == c.name for c in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card_name: str):
        if card_name == "":
            ValueError("Card cannot be an empty string!")
        card_found = [c for c in self.cards if c.name == card_name][0]
        self.cards.remove(card_found)

    def find(self, name: str):
        card_found = [c for c in self.cards if c.name == name][0]
        return card_found
