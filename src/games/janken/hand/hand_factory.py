"""このモジュールは、じゃんけんゲームで使用する手の形を生成する機能を提供します

主なクラスは以下のとおりです:

- HandFactory: じゃんけんの手を生成するためのFactoryクラス
"""
import random
from ..player_input import PlayerInput
from . import Hand

class HandFactory():
    """じゃんけんの手を生成するためのFactoryクラス

    クラスメソッド：
    - create_hand_from_player_input: プレイヤーの入力から手を生成します。
    - create_random_enemy_hands: プレイヤーの人数に基づいてランダムな敵の手を生成します。
    """

    @classmethod
    def create_hand_from_player_input(cls, player_input: PlayerInput) -> Hand:
        """プレイヤーの入力からじゃんけんの手を生成します。

        Args:
            player_input (PlayerInput): プレイヤーからの入力

        Returns:
            Hand: プレイヤーの入力に対応するじゃんけんの手
        """
        return Hand(player_input.hand)

    @classmethod
    def create_random_enemy_hands(cls, player_input: PlayerInput):
        """プレイヤーの人数に基づいてランダムな敵の手を生成します。

        Args:
            player_input (PlayerInput): プレイヤーからの入力。

        Returns:
            List[Hand]: ランダムに生成された敵の手のリスト。
        """
        return [cls.__create_hand_as_random() for i in range(player_input.player_num - 1)]

    @classmethod
    def __create_hand_as_random(cls):
        """ランダムにじゃんけんの手を生成します。

        Returns:
            Hand: ランダムに選ばれたじゃんけんの手。
        """
        return random.choice([Hand.ROCK, Hand.SCISSORS, Hand.PAPER])
