from unittest import TestCase
from typing import List
from src.games.janken import Game, PlayerInput
from src.games.janken.game_result import Result
from src.games.janken.hand import Hand

class TestGame(TestCase):
    """
    Gameのテスト(正常系だけ実施し異常系のテストは内部で使うクラスで実施)
    """
    def create_rock_hands(self, player_input: PlayerInput) -> List[Hand]:
        """グーの手だけを返すテスト用メソッド"""
        return [Hand.ROCK for i in range(player_input.player_num - 1)]

    def test_play_is_callable(self):
        """Gameインスタンスが正常に動作する"""
        player_input: PlayerInput = PlayerInput("r", "3")
        game =  Game(player_input, self.create_rock_hands)
        game.play()
        self.assertEqual(game.result.result,Result.DRAW)
        player_hand_message = game.create_player_hand_message()
        self.assertEqual(player_hand_message, "あなたの手はグーでした")
        enemy_hands_message = game.create_enemy_hands_message()
        self.assertEqual(enemy_hands_message, "相手の手はグー, グーでした")

    def test_print_result_must_call_after_play(self):
        """print_resultをplay()実行前に実行すると例外が発生する"""
        player_input: PlayerInput = PlayerInput("r", "3")
        game =  Game(player_input, self.create_rock_hands)
        with self.assertRaises(RuntimeError):
            game.print_result()
