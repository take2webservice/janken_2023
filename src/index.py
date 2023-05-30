"""プログラムのエントリーポイント
実行時引数を用いてゲームを生成しプレイ
プレイ終了後に結果を表示する
"""
import sys
from games import IGame
from game_factory import GameFactory

if __name__ == '__main__':
    try:
        game: IGame = GameFactory.create_game(sys.argv)
        game.play()
        game.print_result()
    except Exception as e: # pylint: disable=broad-except
        print(f"エラーが発生しました: {str(e)}")
