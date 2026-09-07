"""
2048ゲームのTkinter GUI描画およびキー入力ハンドラ。
GUI層は描画とキー操作に特化し、ゲームロジックは src/ の各モジュールを呼び出す。
"""

import tkinter as tk
from tkinter import messagebox

from src.board_logic import slide_and_merge_line
from src.game_manager import is_game_over
from src.tile_generator import spawn_tile

CELL_COLORS = {
    0: "#CDC1B4",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#EDC22E",
}

TEXT_COLORS = {
    0: "#776E65",
    2: "#776E65",
    4: "#776E65",
    8: "#F9F6F2",
    16: "#F9F6F2",
    32: "#F9F6F2",
    64: "#F9F6F2",
    128: "#F9F6F2",
    256: "#F9F6F2",
    512: "#F9F6F2",
    1024: "#F9F6F2",
    2048: "#F9F6F2",
}


class Game2048GUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("2048 - ユニットテスト入門教材")
        self.root.resizable(False, False)

        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0

        self._init_ui()
        self._reset_game()

    def _init_ui(self):
        # スコア表示エリア
        self.header_frame = tk.Frame(self.root, bg="#FAF8EF", padx=10, pady=10)
        self.header_frame.pack(fill=tk.X)

        self.score_label = tk.Label(
            self.header_frame,
            text="Score: 0",
            font=("Helvetica", 18, "bold"),
            bg="#FAF8EF",
            fg="#776E65",
        )
        self.score_label.pack(side=tk.LEFT)

        # 4x4 グリッド描画エリア
        self.grid_frame = tk.Frame(self.root, bg="#BBADA0", padx=10, pady=10)
        self.grid_frame.pack()

        self.cells = []
        for r in range(4):
            row_cells = []
            for c in range(4):
                cell_frame = tk.Frame(
                    self.grid_frame, width=80, height=80, bg="#CDC1B4"
                )
                cell_frame.grid(row=r, column=c, padx=5, pady=5)
                cell_frame.grid_propagate(False)

                cell_label = tk.Label(
                    cell_frame,
                    text="",
                    font=("Helvetica", 22, "bold"),
                    bg="#CDC1B4",
                    fg="#776E65",
                )
                cell_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                row_cells.append(cell_label)
            self.cells.append(row_cells)

        # キーバインド設定
        self.root.bind("<Left>", lambda event: self._move("Left"))
        self.root.bind("<Right>", lambda event: self._move("Right"))
        self.root.bind("<Up>", lambda event: self._move("Up"))
        self.root.bind("<Down>", lambda event: self._move("Down"))

    def _reset_game(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.board = spawn_tile(self.board)
        self.board = spawn_tile(self.board)
        self._update_ui()

    def _update_ui(self):
        self.score_label.config(text=f"Score: {self.score}")
        for r in range(4):
            for c in range(4):
                val = self.board[r][c]
                bg_color = CELL_COLORS.get(val, "#3C3A32")
                fg_color = TEXT_COLORS.get(val, "#F9F6F2")
                label = self.cells[r][c]
                label.config(
                    text=str(val) if val > 0 else "",
                    bg=bg_color,
                    fg=fg_color,
                )
                label.master.config(bg=bg_color)

    def _move(self, direction: str):
        moved = False
        gained_score = 0
        new_board = [[0] * 4 for _ in range(4)]

        if direction in ("Left", "Right"):
            for r in range(4):
                line = self.board[r]
                if direction == "Right":
                    line = line[::-1]
                merged_line, line_score = slide_and_merge_line(line)
                if direction == "Right":
                    merged_line = merged_line[::-1]

                new_board[r] = merged_line
                gained_score += line_score
                if new_board[r] != self.board[r]:
                    moved = True

        elif direction in ("Up", "Down"):
            for c in range(4):
                line = [self.board[r][c] for r in range(4)]
                if direction == "Down":
                    line = line[::-1]
                merged_line, line_score = slide_and_merge_line(line)
                if direction == "Down":
                    merged_line = merged_line[::-1]

                for r in range(4):
                    new_board[r][c] = merged_line[r]
                gained_score += line_score

                if [new_board[r][c] for r in range(4)] != [
                    self.board[r][c] for r in range(4)
                ]:
                    moved = True

        if moved:
            self.board = new_board
            self.score += gained_score
            self.board = spawn_tile(self.board)
            self._update_ui()

            if is_game_over(self.board):
                messagebox.showinfo(
                    "Game Over", f"Game Over!\nFinal Score: {self.score}"
                )
