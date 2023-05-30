"""ゲーム結果の抽象クラス
"""
from abc import ABC, abstractmethod

class IGame(ABC):
    """ゲームのゲーム結果の抽象基底クラス
    ここには詳細は実装しない

    Raises:
        NotImplementedError: printメソッド未実装時に発生
        NotImplementedError: print_detailメソッド未実装時に発生
    """
    @abstractmethod
    def play(self) -> None:
        """ゲームの実行

        Raises:
            NotImplementedError: printメソッド未実装時に発生
        """
        raise NotImplementedError("playが未実装です")

    @abstractmethod
    def print_result(self) -> None:
        """ゲームの内容や過程といった詳細の出力

        Raises:
            NotImplementedError: print_detailメソッド未実装時に発生
        """
        raise NotImplementedError("print_detailが未実装です")
