from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []

    # instead of adding self.count to init method and to amend each time we add to players list we just run len(list). whise ;)
    @property
    def count(self):
        return len(self.players)

    def add(self, player):
        if any(plr.username == player.username for plr in self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        found_player = self.find(player_name)
        self.players.remove(found_player)

    def find(self, username):
        player_to_return = [
            plr for plr in self.players if plr.username == username][0]
        return player_to_return
