from project.player.player import Player
from project.card.card import Card


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_point += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_point += 30

        # adding bonus points before fight
        attacker.health = sum(
            [card.health_points for card in attacker.card_repository.cards])
        enemy.health = sum(
            [card.health_points for card in enemy.card_repository.cards])

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
