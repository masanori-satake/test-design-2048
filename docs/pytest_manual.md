# pytest クイックマニュアル

本ハンズオンの目的は「何をテストすべきかというデザイン（設計）」を学ぶことです。
Pythonのテストフレームワーク `pytest` の文法で迷って時間を取られないよう、必要な書き方をこのマニュアルにまとめています。

---

## 1. 基本形（Arrange-Act-Assert）

`pytest` では、`test_` で始まるファイル名および関数名を作成し、Python標準の `assert` 文で結果を検証します。

```python
# テスト対象の関数（例: 温度計算機）
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

# テスト関数
def test_celsius_to_fahrenheit_freezing_point():
    # 1. Arrange（準備）
    input_celsius = 0.0
    expected_fahrenheit = 32.0

    # 2. Act（実行）
    actual = celsius_to_fahrenheit(input_celsius)

    # 3. Assert（検証）
    assert actual == expected_fahrenheit

```

---

## 2. データ駆動テスト（`@pytest.mark.parametrize`）

同じテストロジックに対して、複数の「入力と期待値のセット」を渡してまとめて実行する手法です。

```python
import pytest

def calculate_discount(price: int, rank: str) -> int:
    if rank == "gold":
        return int(price * 0.8)
    elif rank == "silver":
        return int(price * 0.9)
    return price

# パラメータ化テスト
@pytest.mark.parametrize(
    "price, rank, expected_price",
    [
        # (入力1, 入力2, 期待値)
        (1000, "gold", 800),     # ゴールド会員は20%引き
        (1000, "silver", 900),   # シルバー会員は10%引き
        (1000, "regular", 1000), # 通常会員は割引なし
    ]
)
def test_calculate_discount(price, rank, expected_price):
    result = calculate_discount(price, rank)
    assert result == expected_price

```

---

## 3. モック・スタブ（`unittest.mock.patch`）

ランダム値や現在時刻、外部API呼び出しなどの「不確定要素」を固定の値に差し替える方法です。

```python
import random
from unittest.mock import patch

def roll_dice_and_check_win() -> str:
    """6が出たら勝利、それ以外は敗北"""
    number = random.randint(1, 6)
    return "WIN" if number == 6 else "LOSE"

def test_roll_dice_win_when_six():
    # random.randint が呼び出されたら、強制的に 6 を返すように設定
    with patch("random.randint", return_value=6):
        result = roll_dice_and_check_win()
        assert result == "WIN"

```

---

## 4. 組み合わせテスト（`allpairspy` との連携）

ペア構成法（All-Pairs技法）を使って自動生成された組み合わせを `pytest` で実行するパターンです。

```python
import pytest
from allpairspy import AllPairs

def search_products(category: str, in_stock_only: bool, sort_by: str) -> list:
    return ["product_a"]

def test_search_products_all_pairs():
    categories = ["electronics", "books", "clothing"]
    in_stock = [True, False]
    sort_orders = ["price_asc", "price_desc", "popularity"]

    parameters = [categories, in_stock, sort_orders]

    for category, stock_flag, sort_order in AllPairs(parameters):
        results = search_products(category, stock_flag, sort_order)
        assert isinstance(results, list)

```

---

## 5. テスト実行コマンド集

```bash
# すべてのテストを実行
pytest

# 詳細ログを表示して実行
pytest -v

# カバレッジ（網羅率）を計測して表示
pytest --cov=src

```
