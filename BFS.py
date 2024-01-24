import tkinter as tk
import random
from collections import deque

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text=" ", font=('normal', 20), width=6, height=3, command=lambda i=i: self.make_move(i))
            self.buttons.append(button)
            button.grid(row=i // 3, column=i % 3)

    def make_move(self, index):
        if self.board[index] == " " and not self.check_game_over():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            self.current_player = "X" if self.current_player == "O" else "O"

            if self.current_player == "O":
                self.computer_move()

    def computer_move(self):
        best_move = self.bfs(self.board.copy(), "O")
        self.make_move(best_move)

    def bfs(self, board, player):
        queue = deque()
        for i, cell in enumerate(board):
            if cell == " ":
                queue.append((i, board.copy()))

        while queue:
            index, current_board = queue.popleft()
            current_board[index] = player
            if self.check_winner(current_board, player):
                return index
            
            next_player = "X" if player == "O" else "O"
            empty_cells = [i for i, cell in enumerate(current_board) if cell == " "]
            for cell in empty_cells:
                new_board = current_board.copy()
                new_board[cell] = next_player
                queue.append((cell, new_board))

        return random.choice(empty_cells)

    def check_winner(self, board, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True

        return False

    def check_game_over(self):
        if self.check_winner(self.board, "X"):
            self.declare_winner("X")
            return True
        if self.check_winner(self.board, "O"):
            self.declare_winner("O")
            return True
        if " " not in self.board:
            self.declare_winner("Draw")
            return True
        return False

    def declare_winner(self, winner):
        result_label = tk.Label(self.window, text="Winner: " + winner, font=('normal', 20))
        result_label.grid(row=3, column=0, columnspan=3)
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def play(self):
        self.window.mainloop()

game = TicTacToe()
game.play()
