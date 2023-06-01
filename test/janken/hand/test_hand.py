"""Handクラスのテスト用モジュール"""
from unittest import TestCase
from src.games.janken.hand import Hand

class TestHand(TestCase):
    """
    Handのテスト

    - 正常系
      - test_display_text
      - test_judge_won_hand_from_set_returns_winner
      - test_judge_won_hand_from_set_returns_none
    - 異常系
      - test_judge_won_hand_from_set_raise_error
    """
    def test_display_text(self):
        """display_textが正しい値を返す"""
        self.assertEqual(Hand.ROCK.display_text, "グー")
        self.assertEqual(Hand.SCISSORS.display_text, "チョキ")
        self.assertEqual(Hand.PAPER.display_text, "パー")

    def test_judge_won_hand_from_set_returns_winner(self):
        """judge_won_hand_from_setが正しい勝利手を返す"""
        scissors_vs_paper = set([Hand.SCISSORS, Hand.PAPER])
        scissors_vs_paper_resul = Hand.judge_won_hand_from_set(scissors_vs_paper)
        self.assertEqual(scissors_vs_paper_resul, Hand.SCISSORS)

        rock_vs_scissors = set([Hand.ROCK, Hand.SCISSORS])
        rock_vs_scissors_resul = Hand.judge_won_hand_from_set(rock_vs_scissors)
        self.assertEqual(rock_vs_scissors_resul, Hand.ROCK)

        paper_vs_rock = set([Hand.PAPER, Hand.ROCK])
        paper_vs_rock_resul = Hand.judge_won_hand_from_set(paper_vs_rock)
        self.assertEqual(paper_vs_rock_resul, Hand.PAPER)

    def test_judge_won_hand_from_set_returns_none(self):
        """あいこの時はjudge_won_hand_from_setがNoneを返す"""
        all_hands = set([Hand.SCISSORS, Hand.PAPER, Hand.ROCK])
        all_hands_resul = Hand.judge_won_hand_from_set(all_hands)
        self.assertIsNone(all_hands_resul)

        rock_only = set([Hand.ROCK])
        rock_only_resul = Hand.judge_won_hand_from_set(rock_only)
        self.assertIsNone(rock_only_resul)

    def test_judge_won_hand_from_set_raise_error(self):
        """
        Set以外を引数にjudge_won_hand_from_setを呼び出す
        Hand以外が含まれるSetを引数にjudge_won_hand_from_setを呼び出す
        """
        with self.assertRaises(TypeError):
            Hand.judge_won_hand_from_set([Hand.ROCK, Hand.PAPER])

        with self.assertRaises(ValueError):
            Hand.judge_won_hand_from_set(set([Hand.ROCK, "PAPER"]))
