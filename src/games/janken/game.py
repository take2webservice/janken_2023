"""
このモジュールでは、ジャンケンゲームの核となる機能を提供します。Gameクラスはゲームの進行を管理し、
手の勝敗を判断します。
"""
from typing import List, Set, Optional, Callable

from ..igame import IGame
from .player_input import PlayerInput
from .hand import Hand
from .game_result import GameResult

class Game(IGame):
    """
    Gameクラスはジャンケンゲームの進行を管理します。プレイヤーの手と敵の手を元に、勝敗を判断します。
    """
    __slots__ = ['player_input', 'player_hand', 'enemy_hands', 'result']

    def __init__(self, player_input: PlayerInput, create_enemy_hands:Callable[[PlayerInput], List[Hand]]) -> None:
        """
        Gameクラスのインスタンスを初期化します。

        Args:
            param player_input (PlayerInput): プレイヤーからの入力情報
            param enemy_hands (List[Hand]): 敵の手のリスト
        """
        self.player_hand: Hand = Hand(player_input.hand)
        self.enemy_hands: List[Hand] = create_enemy_hands(player_input)
        self.result: Optional[GameResult] = None

    def play(self) -> GameResult:
        """
        ゲームを進行し、ゲームの結果を返します。

        return: 
            GameResult: ゲームの結果
        """
        all_hands: Set[Hand] = set([self.player_hand] + self.enemy_hands)
        won_hand: Hand = Hand.judge_won_hand_from_set(all_hands)
        self.result = GameResult(won_hand, self.player_hand)
        return self.result

    def print_result(self) -> None:
        """
        ゲームの結果を出力する
        """
        if self.result is None:
            raise RuntimeError("playを先に実行してください")
        result_message: str = self.result.create_result_message()
        player_hand_message: str = self.create_player_hand_message()
        enemy_hands_message: str = self.create_enemy_hands_message()
        print(result_message)
        print(player_hand_message)
        print(enemy_hands_message)

    def create_player_hand_message(self) -> str:
        """
        プレイヤーの選択した手を表すメッセージを返す
        """
        return f"あなたの手は{self.player_hand.display_text}でした"

    def create_enemy_hands_message(self) -> str:
        """
        敵プレイヤーの選択した手を表すメッセージを返す
        """
        enemy_hands_str: str = ", ".join([hand.display_text for hand in self.enemy_hands])
        return f"相手の手は{enemy_hands_str}でした"
        