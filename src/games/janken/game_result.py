"""
このモジュールではジャンケンのゲームの結果を表現するためのクラスを定義しています。

クラス：
- Result: 勝ち、負け、引き分けをEnumで表現します。
- GameResult: ゲームの結果を表現し、プレイヤーと相手の手を判定します。
"""
from enum import Enum
from typing import Optional

from .hand import Hand

class Result(Enum):
    """じゃんけんの結果を表すEnumクラスです。
    """
    WIN = "勝ち"
    LOSE = "負け"
    DRAW = "引き分け"

class GameResult():
    """じゃんけんのゲーム結果を表現するクラスです。
    
    メソッド：
    - judge_player_result: プレイヤーの結果を判定します。
    - print: 結果メッセージを表示します。
    - create_result_message: 結果メッセージを作成します。
    """
    __slots__ = ['won_hand', 'player_hand', 'result']

    def __init__(self, won_hand: Optional[Hand], player_hand: Hand) -> None:
        """GameResultクラスのインスタンスを作成します。

        Args:
            won_hand (Optional[Hand]): 相手の手。Noneの場合は引き分けと判定します。
            player_hand (Hand): プレイヤーの手。
        """
        self.won_hand: Hand = won_hand
        self.player_hand: Hand = player_hand
        self.result = self.judge_player_result()

    def judge_player_result(self):
        """プレイヤーの結果を判定します。

        Returns:
            Result: プレイヤーの結果（勝ち、負け、引き分け）
        """
        if self.won_hand is None:
            return Result.DRAW
        if self.won_hand == self.player_hand:
            return Result.WIN
        return Result.LOSE

    def create_result_message(self) -> str:
        """結果メッセージを作成します。

        Returns:
            str: 結果メッセージ。
        """
        return f"あなたの{self.result.value}"
