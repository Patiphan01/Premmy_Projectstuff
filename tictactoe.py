import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.board = [" " for _ in range(9)]  # Representing the board as a list

        self.current_player = "X"
        self.buttons = []

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", width=10, height=4,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

    def ai_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == " "]
        if available_moves:
            index = self.minimax(self.board, "O")["index"]
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            if self.check_winner("O"):
                messagebox.showinfo("Tic Tac Toe", "AI wins!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "X"

    def minimax(self, board, player):
        available_moves = [i for i, val in enumerate(board) if val == " "]

        if self.check_winner("X"):
            return {"score": -1}
        elif self.check_winner("O"):
            return {"score": 1}
        elif not available_moves:
            return {"score": 0}

        moves = []
        for move in available_moves:
            new_board = board.copy()
            new_board[move] = player
            if player == "O":
                result = self.minimax(new_board, "X")
                move_score = result["score"]
            else:
                result = self.minimax(new_board, "O")
                move_score = result["score"]
            moves.append({"index": move, "score": move_score})

        if player == "O":
            best_move = max(moves, key=lambda x: x["score"])
        else:
            best_move = min(moves, key=lambda x: x["score"])

        return best_move

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
