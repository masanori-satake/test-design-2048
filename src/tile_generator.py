"""
空きマスへの新しいタイル生成ロジックを担当するモジュール。
"""
import random
import copy

def spawn_tile(board: list[list[int]]) -> list[list[int]]:
    """
    盤面内の空きマス（0）をランダムに1つ選び、タイル（90%で2、10%で4）を生成する。

    :param board: 2次元配列の盤面
    :return: タイルが生成された新しい盤面（空きマスがない場合は元の盤面のコピー）
    """
    new_board = copy.deepcopy(board)
    empty_positions = []

    for r in range(len(new_board)):
        for c in range(len(new_board[r])):
            if new_board[r][c] == 0:
                empty_positions.append((r, c))

    if not empty_positions:
        return new_board

    r, c = random.choice(empty_positions)
    # 90%の確率で2、10%の確率で4
    new_board[r][c] = 2 if random.random() < 0.9 else 4

    return new_board
