"""
2048の盤面およびスライド・合成ロジックを担当するモジュール。
（Session 6 リファクタリング適用後の一例）
"""


def slide_and_merge_line(line: list[int]) -> tuple[list[int], int]:
    """
    1行分（長さ4）のスライドと合成処理を行い、(新しい行, 獲得スコア) を返す純粋関数。
    """
    if len(line) != 4:
        raise ValueError("line must contain exactly 4 cells")

    # リスト内包表記で簡潔に0を除外
    non_zero = [x for x in line if x != 0]

    merged = []
    score = 0
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged_val = non_zero[i] * 2
            merged.append(merged_val)
            score += merged_val
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1

    # パディング処理を演算子で簡潔に記述
    merged += [0] * (4 - len(merged))

    return merged, score


def is_board_full(board: list[list[int]]) -> bool:
    """
    盤面に空きマス（0）がないかを判定する関数。
    """
    # ジェネレータ式と any() で早期リターンするPythonicな実装
    return not any(0 in row for row in board)

