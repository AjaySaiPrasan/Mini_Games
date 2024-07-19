import tkinter as tk
from tkinter import messagebox

def issafe(board, a, b):
    return board[a][b] == "  "

def win(b, cur, r, c):
    # Check row
    if all(cell == cur for cell in b[r]):
        return True
    # Check column
    if all(b[i][c] == cur for i in range(3)):
        return True
    # Check diagonals
    if all(b[i][i] == cur for i in range(3)) or all(b[i][2-i] == cur for i in range(3)):
        return True
    return False 

def isfull(board):
    return all(cell != "  " for row in board for cell in row)

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [["  " for _ in range(3)] for _ in range(3)]
        self.current_player = "x"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", font=('Arial', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if issafe(self.board, row, col):
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if win(self.board, self.current_player, row, col):
                messagebox.showinfo("Game Over", f"Congrats, player {self.current_player} wins!")
                self.master.quit()
            elif isfull(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.master.quit()
            else:
                self.current_player = "o" if self.current_player == "x" else "x"
        else:
            messagebox.showwarning("Invalid Move", "That cell is already occupied. Try again.")

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("_" * 10)

def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()