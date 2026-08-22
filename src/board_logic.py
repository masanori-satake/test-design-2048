"""
2048の盤面およびスライド・合成ロジックを担当するモジュール。
"""


def slide_and_merge_line(line: list[int]) -> tuple[list[int], int]:
    """
    1行分（長さ4）のスライドと合成処理を行い、(新しい行, 獲得スコア) を返す純粋関数。

    仕様:
    - 0以外の要素を左側に寄せる。
    - 隣り合う同じ数値は1回だけ合成され、合計値となる。
    - 連鎖合成を防ぐ（例: [2, 2, 2, 2] -> [4, 4, 0, 0], スコア: 8）。
    - 合成された数値の合計値が得点（獲得スコア）として加算される。
    """
    # 0を取り除いた要素のリストを作成
    non_zero = [x for x in line if x != 0]

    merged = []
    score = 0
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged_val = non_zero[i] * 2
            merged.append(merged_val)
            score += merged_val
            i += 2  # スキップして連鎖合成を防ぐ
        else:
            merged.append(non_zero[i])
            i += 1

    # 残りを0で埋めて長さ4にする
    while len(merged) < len(line):
        merged.append(0)

    return merged, score


def is_board_full(board: list[list[int]]) -> bool:
    """
    盤面に空きマス（0）がないかを判定する関数。

    :param board: 4x4などの2次元配列
    :return: 空きマスがない場合は True、空きマス（0）が存在する場合は False
    """
    for row in board:
        if 0 in row:
            return False
    return True
