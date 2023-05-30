"""
このモジュールでは、プレイヤーの入力情報を管理するためのクラスを定義しています。

クラス：
- PlayerInput: プレイヤーの手とプレイヤー数を管理します。
"""
from typing import List

class PlayerInput():
    """プレイヤーが引数で指定するプレイヤーの手とプレイヤー数を管理するクラス。

    メソッド：
    - prepare_user_input: ユーザー入力を処理してPlayerInputオブジェクトを返します。
    """
    __slots__ = ['hand', 'player_num']
    def __init__(self, hand: str, player_num_str: str = "2") -> None:
        """PlayerInputクラスのインスタンスを作成します。

        Args:
            hand (str): プレイヤーの手。
            player_num_str (str, optional): プレイヤーの数。デフォルトは2。
        """
        self.__validate(hand, player_num_str)
        self.hand: str = hand
        self.player_num = int(player_num_str)

    def __validate(self, hand: str, player_num_str: str) -> None:
        """入力値を検証します。

        Args:
            hand (str): プレイヤーの手。
            player_num_str (str): プレイヤーの数。
        """
        self.__validate_hand(hand)
        self.__validate_player_num(player_num_str)

    def __validate_hand(self, hand: str) -> None:
        """手の入力を検証します。

        Args:
            hand (str): プレイヤーの手。

        Raises:
            ValueError: 手の値が不正な場合。
        """
        if not isinstance(hand, str):
            raise TypeError("hand はstr型を渡してください")
        if not (hand in ["r", "s", "p"]):
            raise ValueError("手はr, s, pのいずれかを入力してください")

    def __validate_player_num(self, player_num_str: str) -> None:
        """プレイヤー数の入力を検証します。

        Args:
            player_num_str (str): プレイヤーの数。

        Raises:
            ValueError: プレイヤー数の値が不正な場合。
        """
        if not isinstance(player_num_str, str):
            raise TypeError("player_num_str はstr型を渡してください")
        min_players = 2
        max_players = 10
        try:
            int(player_num_str)
        except ValueError as exc:
            raise ValueError("プレイヤー人数は整数で入力してください") from exc
        if not min_players <= int(player_num_str) <= max_players:
            raise ValueError("プレイヤー人数は2~10の間で入力してください")

    @classmethod
    def prepare_user_input(cls, args: List[str]):
        """ユーザー入力を処理してPlayerInputオブジェクトを作成します。

        Args:
            args (List[str]): ユーザーからの入力リスト。

        Returns:
            PlayerInput: ユーザー入力から作成されたPlayerInputオブジェクト
        """
        has_hand_only = 2
        has_hand_and_player_num = 3
        if len(args) == has_hand_only:
            return PlayerInput(args[1])
        elif len(args) == has_hand_and_player_num:
            return PlayerInput(args[1], args[2])
        raise ValueError("引数は最低1つ、最大2つまでです")
