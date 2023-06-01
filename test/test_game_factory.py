from unittest import TestCase
from src.games import IGame
from src.games.janken import Game as JankenGame
from src.games.game_factory import GameFactory

class TestGameFactory(TestCase):
    """
    GameFactoryのテスト(正常系だけ実施し異常系のテストは内部で使うクラスで実施)
    # """
    def test_create_janken_game_with_hand_and_players(self):
        """手札とプレイヤーを引数に正常にジャンケンが作れる"""
        try:
            janken_game: IGame = GameFactory.create_game(["index.py", "r", "10"])
            self.assertIsInstance(janken_game, JankenGame)
        except Exception as error: # pylint: disable=broad-except
            self.fail(f"意図しない例外が発生しました。{error}")
