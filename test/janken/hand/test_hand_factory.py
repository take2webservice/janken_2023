from unittest import TestCase
from typing import List
from src.games.janken.hand import HandFactory, Hand
from src.games.janken import PlayerInput

class TestHandFactory(TestCase):
    """
    HandFactoryのテスト
    """
    def test_create_random_enemy_hands(self):
        """PlayerInputのインスタンスを元にHandを生成できる"""
        hand_str_rock = "r"
        player_num = "10"
        player_input_with_rock: PlayerInput = PlayerInput(hand_str_rock, player_num)
        enemy_hands: List[Hand]  = HandFactory.create_random_enemy_hands(player_input_with_rock)
        self.assertEqual(len(enemy_hands), int(player_num) - 1)
        self.assertTrue(
            all(isinstance(hand, Hand) for hand in enemy_hands)
        )
