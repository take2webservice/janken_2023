"""ゲームのFactoryクラスを記述するモジュール
"""
from typing import List

from .igame import IGame
from .janken import PlayerInput as JankenPlayerInput, Game as JankenGame
from .janken.hand import HandFactory

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
        return JankenGame(player_input, HandFactory.create_random_enemy_hands)
