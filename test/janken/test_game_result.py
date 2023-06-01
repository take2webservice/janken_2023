"""
GameResultクラスのテストモジュール
"""
from unittest import TestCase
from src.games.janken.game_result import GameResult, Result
from src.games.janken.hand import Hand

class TestGameResult(TestCase):
    """
    GameResultのテスト
    """

    def test_create_game_result_instance(self):
        """
        GameResultのインスタンスが正常に作られることを確認
        """
        player_hand_paper = Hand.PAPER
        won_hand_scissors = Hand.SCISSORS
        lose_result = GameResult(won_hand_scissors, player_hand_paper)
        self.assertEqual(lose_result.won_hand, won_hand_scissors)
        self.assertEqual(lose_result.player_hand, player_hand_paper)
        self.assertEqual(lose_result.result, Result.LOSE)

        won_hand_rock = Hand.ROCK
        player_hand_rock = Hand.ROCK
        win_result = GameResult(won_hand_rock, player_hand_rock)
        self.assertEqual(win_result.result, Result.WIN)

        no_won_hand = None
        player_hand_scissors = Hand.SCISSORS
        draw_result = GameResult(no_won_hand, player_hand_scissors)
        self.assertEqual(draw_result.result, Result.DRAW)

    def test_create_result_message(self):
        """結果メッセージが正常に作成できる"""
        player_hand_paper = Hand.PAPER
        won_hand_scissors = Hand.SCISSORS
        lose_result = GameResult(won_hand_scissors, player_hand_paper)
        lose_message = lose_result.create_result_message()
        self.assertEqual(lose_message, "あなたの負け")

        won_hand_rock = Hand.ROCK
        player_hand_rock = Hand.ROCK
        win_result = GameResult(won_hand_rock, player_hand_rock)
        win_message = win_result.create_result_message()
        self.assertEqual(win_message, "あなたの勝ち")

        no_won_hand = None
        player_hand_scissors = Hand.SCISSORS
        draw_result = GameResult(no_won_hand, player_hand_scissors)
        draw_message = draw_result.create_result_message()
        self.assertEqual(draw_message, "あなたの引き分け")

