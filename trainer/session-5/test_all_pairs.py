import pytest
from allpairspy import AllPairs

# テストに使う因子と水準の定義
parameters = [
    ["empty_space_exists", "no_empty_space"], # F1: 空きマスの有無
    ["horizontal_mergeable", "no_horizontal_mergeable"], # F2: 水平可動
    ["vertical_mergeable", "no_vertical_mergeable"] # F3: 垂直可動
]

# AllPairsによる2因子網羅のペア生成
def generate_pairs():
    return list(AllPairs(parameters))

@pytest.mark.parametrize("f1, f2, f3", generate_pairs())
def test_game_over_all_pairs_demo(f1, f2, f3):
    """
    allpairspyを使用して因子を組み合わせたテストの骨組み。
    実際の盤面生成と組み合わせてアサーションを行う想定の解答例です。
    
    全組合せ（直積）は 2×2×2 = 8 通りですが、
    Pairwise法（2因子網羅）を用いることでテストケース数が削減されていることを
    確認するためのデモ用テストです。
    """
    assert f1 in parameters[0]
    assert f2 in parameters[1]
    assert f3 in parameters[2]

