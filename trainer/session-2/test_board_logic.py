import pytest
from src.board_logic import slide_and_merge_line


@pytest.mark.parametrize(
    "test_id, line, expected_new_line, expected_score",
    [
        ("TC-S1-01", [0, 0, 0, 0], [0, 0, 0, 0], 0),  # 移動も合成もない状態
        ("TC-S1-02", [0, 2, 0, 4], [2, 4, 0, 0], 0),  # 隙間がある場合のスライドのみ
        ("TC-S1-03", [2, 2, 0, 0], [4, 0, 0, 0], 4),  # 隣り合う同じ数値の合成
        ("TC-S1-04", [2, 2, 2, 2], [4, 4, 0, 0], 8),  # 連鎖しないことの検証
        ("TC-S1-05", [2, 2, 2, 0], [4, 2, 0, 0], 4),  # 左優先合成の検証
        ("TC-S1-06", [2, 0, 0, 2], [4, 0, 0, 0], 4),  # 離れた同じ数値の合成
    ],
)
def test_slide_and_merge_line_valid(test_id, line, expected_new_line, expected_score):
    """TC-S1-01〜06: 同値クラス・境界値をカバーする正常系テスト"""
    new_line, score = slide_and_merge_line(line)
    assert new_line == expected_new_line
    assert score == expected_score


def test_slide_and_merge_line_invalid_length():
    """TC-S1-07: 無効同値：配列長エラー"""
    with pytest.raises(ValueError):
        slide_and_merge_line([2, 2, 2])
