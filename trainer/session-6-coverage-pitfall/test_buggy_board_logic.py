import pytest
from buggy_board_logic import slide_and_merge_line


def test_slide_and_merge_len3():
    # 1回だけ合成が発生し、長さ3になるケース
    # if len(merged) == 3: の分岐をカバー
    line = [2, 2, 4, 8]
    expected = ([4, 4, 8, 0], 4)
    assert slide_and_merge_line(line) == expected


def test_slide_and_merge_len2():
    # 2回合成が発生し、長さ2になるケース
    # elif len(merged) == 2: の分岐をカバー
    line = [2, 2, 4, 4]
    expected = ([4, 8, 0, 0], 12)
    assert slide_and_merge_line(line) == expected


def test_slide_and_merge_len4():
    # 合成が発生せず、長さ4のままのケース
    # elif len(merged) == 4: の分岐をカバー
    line = [2, 4, 8, 16]
    expected = ([2, 4, 8, 16], 0)
    assert slide_and_merge_line(line) == expected


def test_slide_and_merge_invalid_length():
    # 例外処理の分岐をカバー
    with pytest.raises(ValueError):
        slide_and_merge_line([2, 2, 2])


# 【注意】
# 以下のテストケース（空きマスが多いパターン）が漏れている！
# しかし、上記の4つのテストだけでカバレッジ（C0, C1）は100%になってしまう。
#
# def test_slide_and_merge_len1():
#     line = [2, 0, 0, 0]
#     expected = ([2, 0, 0, 0], 0)
#     assert slide_and_merge_line(line) == expected
