"""
PlayerInputクラスのテストモジュール
"""
from unittest import TestCase
from src.games.janken import PlayerInput

class TestPlayerInput(TestCase):
    """
    PlayerInputのテスト

    - PlayerInputのコンストラクタの正常系
      - test_create_player_input_with_valid_hand
      - test_create_player_input_with_valid_player_num
    
    - PlayerInputのコンストラクタの異常系
      - test_create_player_input_with_invalid_hand
      - test_create_player_input_with_invalid_player_num
      - test_create_player_input_with_invalid_type_args
    
    - prepare_user_inputメソッドの正常系
      - test_prepare_user_input
    
    - prepare_user_inputメソッドの異常系
      - test_prepare_user_input_with_invalid_length
    """
    def test_create_player_input_with_valid_hand(self):
        """PlayerInputのインスタンスをr, s, pで正常に作成できる"""
        try:
            hand_str_rock = "r"
            player_input_with_rock: PlayerInput = PlayerInput(hand_str_rock)
            self.assertEqual(player_input_with_rock.hand, hand_str_rock)

            hand_str_scissors = "s"
            player_input_with_scissors: PlayerInput = PlayerInput(hand_str_scissors)
            self.assertEqual(player_input_with_scissors.hand, hand_str_scissors)

            hand_str_paper = "p"
            player_input_with_paper: PlayerInput = PlayerInput(hand_str_paper)
            self.assertEqual(player_input_with_paper.hand, hand_str_paper)

        except Exception as error: # pylint: disable=broad-except
            self.fail(f"意図しない例外が発生しました。{error}")


    def test_create_player_input_with_valid_player_num(self):
        """PlayerInputのインスタンスをプレイヤー数を指定し正常に作成できる"""
        try:
            hand_str: str = "r"
            min_player_num: str = "2"

            player_input_with_player_num: PlayerInput\
                  = PlayerInput(hand_str, min_player_num)
            self.assertEqual(player_input_with_player_num.player_num, int(min_player_num))

            max_player_num: str = "10"
            player_input_with_player_num: PlayerInput = PlayerInput(hand_str, max_player_num)
            self.assertEqual(player_input_with_player_num.player_num, int(max_player_num))
        except Exception as error: # pylint: disable=broad-except
            self.fail(f"意図しない例外が発生しました。{error}")

    def test_create_player_input_with_invalid_hand(self):
        """PlayerInputのインスタンスをr, s, p以外で作成すると例外が発生する"""
        invalid_hand_str = "e"
        with self.assertRaises(ValueError):
            PlayerInput(invalid_hand_str)

    def test_create_player_input_with_invalid_player_num(self):
        """PlayerInputのインスタンスを範囲外のプレイヤー数でで作成すると例外が発生する"""
        hand_str = "r"
        player_num_lower_than_min: str = "1"
        with self.assertRaises(ValueError):
            PlayerInput(hand_str, player_num_lower_than_min)

        player_num_greater_than_max: str = "11"
        with self.assertRaises(ValueError):
            PlayerInput(hand_str, player_num_greater_than_max)

        float_player_num: str = "8.1"
        with self.assertRaises(ValueError):
            PlayerInput(hand_str, float_player_num)

    def test_create_player_input_with_invalid_type_args(self):
        """PlayerInputのインスタンスを不正な型で作成すると例外が発生する"""
        hand_obj = {}
        with self.assertRaises(TypeError):
            PlayerInput(hand_obj)

        hand_str = "r"
        player_num: int = 2
        with self.assertRaises(TypeError):
            PlayerInput(hand_str, player_num)

    def test_prepare_user_input(self):
        """prepare_user_inputメソッドの正常系"""
        entry_point_fila_name: str = "index.py"
        hand_str: str = "r"
        min_player_num: str = "2"
        max_player_num: str = "10"

        player_input_with_hand: PlayerInput = \
            PlayerInput.prepare_user_input([entry_point_fila_name, hand_str])
        self.assertEqual(player_input_with_hand.hand, hand_str)
        self.assertEqual(player_input_with_hand.player_num, int(min_player_num))

        player_input_with_player_num: PlayerInput = \
            PlayerInput.prepare_user_input([entry_point_fila_name, hand_str, max_player_num])
        self.assertEqual(player_input_with_player_num.hand, hand_str)
        self.assertEqual(player_input_with_player_num.player_num, int(max_player_num))

    def test_prepare_user_input_with_invalid_length(self):
        """prepare_user_inputメソッドを意図しない長さの配列で呼びだす"""
        less_than_min_length_arg = []
        with self.assertRaises(ValueError):
            PlayerInput.prepare_user_input(less_than_min_length_arg)

        greater_than_max_length_arg = [None, None, None, None]
        with self.assertRaises(ValueError):
            PlayerInput.prepare_user_input(greater_than_max_length_arg)
