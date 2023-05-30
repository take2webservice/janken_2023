"""このモジュールは、じゃんけんゲームで使用する手の形を表現するためのEnumを提供します。

主なクラスは以下のとおりです:

- Hand: じゃんけんの手の形を表現するためのEnum。'r'はグー、's'はチョキ、'p'はパーを表します。
"""
from enum import Enum
from typing import Set, Optional

class Hand(Enum):
    """じゃんけんの手の形を表現するEnumです。

    このEnumのメンバーはジャンケンの手を表現し、それぞれに文字列の値が関連付けられ実行時引数として利用しています。
    'r' は ROCK（グー）
    's' は SCISSORS（チョキ）
    'p' は PAPER（パー）
    """
    ROCK = "r"
    SCISSORS = "s"
    PAPER = "p"

    @property
    def display_text(self) -> str:
        """printなどの出力用の手の形を日本語の文字列で返します。

        手の形が ROCK（グー）の場合は "グー" を返します。
        手の形が SCISSORS（チョキ）の場合は "チョキ" を返します。
        手の形が PAPER（パー）の場合は "パー" を返します。
        """
        if self.value == Hand.ROCK.value:
            return "グー"
        elif self.value == Hand.SCISSORS.value:
            return "チョキ"
        elif self.value == Hand.PAPER.value:
            return "パー"
        else :
            raise ValueError(f"value = {self.value}は想定されていません。")

    @classmethod
    def judge_won_hand_from_set(cls, hands: Set['Hand']) -> Optional['Hand']:
        """
        与えられた手のセットから勝利した手を判断します。

        Args:
            hands (Set[Hand]): 判断する手のセット
        
        return:
            Optional[Hand]: 勝利した手。引き分けの場合は None を返す
        """
        if not isinstance(hands, Set):
            raise TypeError("handsはSet型を渡してください。")
        all_hands_used = 3
        one_hand_used = 1
        if len(hands) == one_hand_used or len(hands) == all_hands_used:
            return None
        elif hands == {Hand.ROCK, Hand.SCISSORS}:
            return Hand.ROCK
        elif hands == {Hand.PAPER, Hand.ROCK}:
            return Hand.PAPER
        elif hands == {Hand.SCISSORS, Hand.PAPER}:
            return Hand.SCISSORS
        else:
            raise ValueError("渡されたhandsの内容はは想定されていません。")
