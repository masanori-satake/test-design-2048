import pytest
from unittest.mock import patch
from src.tile_generator import spawn_tile

@patch("src.tile_generator.random.choice")
@patch("src.tile_generator.random.random")
def test_spawn_tile_generates_2(mock_random, mock_choice):
    """
    空きマスがある場合に、特定の位置に「2」が生成されることの検証。
    (90%の確率で2が生成されるため、random.random() < 0.9 を返すようモック)
    """
    mock_choice.return_value = (0, 3)
    mock_random.return_value = 0.5  # 0.9より小さい値
    
    board = [
        [2, 4, 2, 0],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    
    expected_board = [
        [2, 4, 2, 2], # (0, 3) に 2 が生成される
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    
    new_board = spawn_tile(board)
    assert new_board == expected_board

@patch("src.tile_generator.random.choice")
@patch("src.tile_generator.random.random")
def test_spawn_tile_generates_4(mock_random, mock_choice):
    """
    空きマスがある場合に、特定の位置に「4」が生成されることの検証。
    (10%の確率で4が生成されるため、random.random() >= 0.9 を返すようモック)
    """
    mock_choice.return_value = (1, 1)
    mock_random.return_value = 0.95  # 0.9以上の値
    
    board = [
        [2, 4, 2, 4],
        [4, 0, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    
    expected_board = [
        [2, 4, 2, 4],
        [4, 4, 4, 2], # (1, 1) に 4 が生成される
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    
    new_board = spawn_tile(board)
    assert new_board == expected_board

def test_spawn_tile_no_empty_space():
    """
    盤面に空きマスがない場合、入力を変更せず盤面のコピーがそのまま返されることの検証。
    """
    board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    
    new_board = spawn_tile(board)
    assert new_board == board
    assert new_board is not board # コピーが返されているか

