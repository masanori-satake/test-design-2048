import pytest
from src.board_logic import is_board_full

def test_is_board_full_tc_s1_08():
    """TC-S1-08: 満杯盤面の判定 (空きマス0個)"""
    board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    assert is_board_full(board) is True

def test_is_board_full_tc_s1_09():
    """TC-S1-09: 空きマスあり盤面の判定 (空きマス1個)"""
    board = [
        [2, 4, 2, 0],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    assert is_board_full(board) is False

