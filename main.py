"""
2048ゲームエントリーポイント。
"""

import tkinter as tk
from src.gui import Game2048GUI


def main():
    root = tk.Tk()
    Game2048GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
