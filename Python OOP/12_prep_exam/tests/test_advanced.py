from project.player.advanced import Advanced
import unittest


class TestAdvancedPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Advanced('Peter')

    def test_init_should_create_player_attributes(self):
        self.assertEqual(self.player.username, 'Peter')
        self.assertEqual(self.player.health, 250)
        self.assertEqual(
            self.player.card_repository.__class__.__name__, 'CardRepository')


if __name__ == "__main__":
    unittest.main()
