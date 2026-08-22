# AIが作成したテストを評価できますか？ <br/>2048で学ぶ「仕様から組み立てる」ユニットテスト入門

## 概要
本リポジトリは、Pythonのパズルゲーム「2048」を題材とした、ユニットテストの設計および実装に関するハンズオン教材です。

生成AI（LLM）を使ってコードやテストケースを簡単に生成できる時代になりましたが、「生成されたテストコードが本当に仕様を満たしているか」「エッジケースや境界値を網羅できているか」を評価・検証する力（テスト設計力）がエンジニアに強く求められています。

本教材では、「AI丸投げ」からの脱却を目指し、仕様書からテスト観点を抽出し、テスト設計表を作成したうえで高品質なユニットテストを実装するプロセスを体験的に学びます。

---

## カリキュラム概要（全6回）

| セッション | タイトル | 主な学習内容・テーマ |
| :--- | :--- | :--- |
| **Session 1** | ユニットテストの基本と仕様の理解 | 単体テストの目的、pytestの基本操作、仕様からテスト観点を取り出す基礎 (`test_board_logic.py`) |
| **Session 2** | 境界値分析と同値分割 | 同値クラスの抽出、限界値・境界値のテスト設計 (`board_logic.py` のスライド・合成) |
| **Session 3** | モックとスタブの活用 | 依存関係の分離、`unittest.mock` / `pytest-mock` を用いたランダム要素の制御 (`tile_generator.py`) |
| **Session 4** | デシジョンテーブルを用いた複雑な仕様の整理 | 複数条件の組み合わせ整理、デシジョンテーブルに基づくテスト設計 (`game_manager.py`) |
| **Session 5** | Pairwise法（All-Pairs法）による組み合わせテスト | `allpairspy` を活用したパラメータ化テスト (`pytest.mark.parametrize`) |
| **Session 6** | コード網羅率（カバレッジ）とリファクタリング | `pytest-cov` によるカバレッジ測定、テスト主導での安全なリファクタリング |

---

## 開発環境とセットアップ

### 前提条件
* Python 3.10 以上
* Linux（Ubuntu/Debian等）でGUI環境を動かす場合は、Tkinterパッケージ（`python3-tk`）が必要です：
  ```bash
  sudo apt-get install python3-tk
  ```

### 1. 仮想環境の作成と有効化
```bash
# Linux / macOS の場合
python3 -m venv venv
source venv/bin/activate

# Windows の場合 (PowerShell / Command Prompt)
py -3 -m venv venv
# または: python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

### 3. ゲームの起動確認
```bash
python main.py
```
* 矢印キー（↑ ↓ ← →）でタイルを操作して2048ゲームをプレイできます。

### 4. pytest の実行方法
```bash
# 全テストの実行
pytest

# 詳細出力付きで実行
pytest -v

# カバレッジ測定付きで実行 (Session 6)
pytest --cov=src --cov-branch --cov-report=term-missing
```

---

## ドキュメント構成 (`docs/`)
各セッションの教材・ガイドラインは `docs/` ディレクトリに配置されています。セッションの進行に合わせて参照・実行してください。

* `docs/session-1-introduction.md`
* `docs/session-2-boundary-values.md`
* `docs/session-3-mocks-and-stubs.md`
* `docs/session-4-decision-table.md`
* `docs/session-5-all-pairs.md`
* `docs/session-6-coverage-refactoring.md`
