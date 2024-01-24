import tkinter as tk
import random

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
        best_move = self.iterative_deepening(self.board.copy(), "O")
        self.make_move(best_move)

    def iterative_deepening(self, board, player):
        best_move = None
        for depth in range(1, 10):
            move = self.depth_limited_search(board, player, depth)
            if move is not None:
                best_move = move

        return best_move

    def depth_limited_search(self, board, player, depth):
        empty_cells = [i for i, cell in enumerate(board) if cell == " "]

        if depth == 0 or not empty_cells:
            return None
        if player == "O":
            best_value = float('-inf')
            best_move = None
            for cell in empty_cells:
                new_board = board.copy()
                new_board[cell] = player
                value = self.min_value(new_board, depth - 1)
                if value > best_value:
                    best_value = value
                    best_move = cell
            return best_move
        else:
            best_value = float('inf')
            best_move = None
            for cell in empty_cells:
                new_board = board.copy()
                new_board[cell] = player
                value = self.max_value(new_board, depth - 1)
                if value < best_value:
                    best_value = value
                    best_move = cell

            return best_move

    def max_value(self, board, depth):
        if self.check_winner(board, "O") or self.check_winner(board, "X") or depth == 0:
            return self.utility(board, "O")

        value = float('-inf')
        for cell in [i for i, cell in enumerate(board) if cell == " "]:
            new_board = board.copy()
            new_board[cell] = "O"
            value = max(value, self.min_value(new_board, depth - 1))

        return value

    def min_value(self, board, depth):
        if self.check_winner(board, "O") or self.check_winner(board, "X") or depth == 0:
            return self.utility(board, "O")

        value = float('inf')
        for cell in [i for i, cell in enumerate(board) if cell == " "]:
            new_board = board.copy()
            new_board[cell] = "X"
            value = min(value, self.max_value(new_board, depth - 1))

        return value

    def utility(self, board, player):
        if self.check_winner(board, player):
            return 1
        elif self.check_winner(board, "X" if player == "O" else "O"):
            return -1
        return 0

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
