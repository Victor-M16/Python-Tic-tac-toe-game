import tkinter as tk

class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x300")

        self.current_player = "X"
        self.board = [" "] * 9

        self.label = tk.Label(self.root, text="Current player: X")
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.frame, text=" ", width=8, height=4, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_board)
        self.reset_button.pack(pady=10)

    def make_move(self, i, j):
        index = i * 3 + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"
            self.label.config(text="Current player: " + self.current_player)
            winner = self.check_winner()
            if winner:
                self.label.config(text="Winner: " + winner)
                for row in self.buttons:
                    for button in row:
                        button.config(state="disabled")
            elif " " not in self.board:
                self.label.config(text="It's a tie!")
        else:
            self.label.config(text="That space is already taken.")

    def check_winner(self):
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        for i in range(3):
            col = self.board[i::3]
            if col[0] == col[1] == col[2] != " ":
                return col[0]
        diag1 = self.board[0] == self.board[4] == self.board[8] != " "
        diag2 = self.board[2] == self.board[4] == self.board[6] != " "
        if diag1 or diag2:
            return self.board[4]
        return None

    def reset_board(self):
        self.current_player = "X"
        self.board = [" "] * 9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")
        self.label.config(text="Current player: X")

root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()
