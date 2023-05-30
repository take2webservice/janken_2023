"""ゲームのFactoryクラスを記述するモジュール
"""
from typing import List

from games import IGame
from games.janken import PlayerInput as JankenPlayerInput, \
    Game as JankenGame, ResultWriter as JankenResultWriter
from games.janken.hand import HandFactory, Hand

class GameFactory():
    """ゲームのFactoryクラス
    """

    @classmethod
    def create_game(cls, argv: List[str]) -> IGame:
        """ゲームオブジェクトのの生成メソッド

        Args:
            argv (List[str]): プログラムの実行時引数

        Returns:
            IGame: IGameを継承したゲームの具象クラス
        """
        player_input: JankenPlayerInput = JankenPlayerInput.prepare_user_input(argv)
        result_writer: JankenResultWriter = JankenResultWriter()
        enemy_hands: List[Hand] = HandFactory.create_random_enemy_hands(player_input)
        return JankenGame(result_writer, player_input, enemy_hands)
