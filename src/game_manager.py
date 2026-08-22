"""
ゲームの進行管理、ゲームオーバー判定を担当するモジュール。
"""
from src.board_logic import is_board_full

def is_game_over(board: list[list[int]]) -> bool:
    """
    盤面が全て埋まっており、かつ「上下左右に隣接する同じ数字が存在しない」場合に True を返す。

    :param board: 2次元配列の盤面
    :return: ゲームオーバーなら True、動かせる手があるなら False
    """
    if not is_board_full(board):
        return False

    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            val = board[r][c]
            # 右隣との比較
            if c + 1 < cols and board[r][c + 1] == val:
                return False
            # 下隣との比較
            if r + 1 < rows and board[r + 1][c] == val:
                return False

    return True
