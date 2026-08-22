"""
tests/test_board_logic.py
src/board_logic.py に対するテストコード。
Session 1 & 2 で受講生がテストケースを拡張・完成させます。
"""
from src.board_logic import is_board_full, slide_and_merge_line


def test_is_board_full_returns_true_when_full():
    """
    [サンプルテストケース]
    盤面に 0 が含まれていない場合、is_board_full が True を返すことを検証する。
    """
    full_board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    assert is_board_full(full_board) is True


# ==============================================================================
# 演習: 以下のテストケースを受講生自身で設計・実装してください
# ==============================================================================

# TODO: test_is_board_full_returns_false_when_empty_spot_exists()
# 盤面に 0 (空きマス) が含まれている場合、is_board_full が False を返すことを検証するテスト。

# TODO: test_slide_and_merge_line_basic()
# [2, 0, 2, 0] をスライドした際、[4, 0, 0, 0] になり、スコア 4 が返されることを検証するテスト。

# TODO: test_slide_and_merge_line_no_chained_merge()
# [2, 2, 2, 2] をスライドした際、1回の移動で連鎖合成されず [4, 4, 0, 0] (スコア 8) になることを検証するテスト。

# TODO: test_slide_and_merge_line_no_merge()
# [2, 4, 8, 16] のように合成が発生しない場合、そのままの配置とスコア 0 が返されることを検証するテスト。
