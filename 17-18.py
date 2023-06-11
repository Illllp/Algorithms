import tkinter as tk

class CheckersGUI:
    def __init__(self, checkers):
        self.checkers = checkers
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.draw_pieces()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.selected_piece = None
        self.window.mainloop()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_pieces(self):
        self.canvas.delete("piece")
        for row in self.checkers.board.grid:
            for piece in row:
                if piece is not None:
                    x, y = piece.col * 50 + 25, piece.row * 50 + 25
                    color = piece.color
                    if piece.is_king:
                        color = "gold"
                        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color, tags="piece")
                        self.canvas.create_text(x, y, text="K", fill="white", tags="piece")
                    else:
                        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color, tags="piece")

    def handle_click(self, event):
        row, col = event.y // 50, event.x // 50
        piece = self.checkers.board.grid[row][col]
        if piece is not None and piece.color == self.checkers.current_player:
            self.selected_piece = piece
        elif self.selected_piece is not None and (row, col) in self.checkers.get_valid_moves(self.selected_piece):
            self.checkers.make_move(self.selected_piece, row, col)
            self.draw_pieces()
            del self.selected_piece
        else:
            del self.selected_piece
        self.canvas.delete("highlight")



class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.is_alive = True
        self.is_king = False

    def move(self, row, col):
        self.row = row
        self.col = col
        if self.color == 'white' and self.row == 0:
            self.is_king = True
        elif self.color == 'black' and self.row == 7:
            self.is_king = True

    def capture(self):
        self.is_alive = False

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'white'

    def create_board(self):
        for row in range(8):
            for col in range(8):
                if row % 2 == col % 2:
                    if row < 3:
                        self.grid[row][col] = Piece('black', row, col)
                    elif row > 4:
                        self.grid[row][col] = Piece('white', row, col)

    def move_piece(self, piece, row, col):
        self.grid[piece.row][piece.col], self.grid[row][col] = self.grid[row][col], self.grid[piece.row][piece.col]
        piece.move(row, col)

    def capture_piece(self, piece):
        self.grid[piece.row][piece.col] = None
        piece.capture()

class Checkers:
    def __init__(self):
        self.board = Board()
        self.board.create_board()
        self.current_player = 'white'

    def switch_turn(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def make_move(self, piece, row, col):
        if (row, col) in self.get_valid_moves(piece):
            if abs(piece.row - row) == 2:
                captured_row = (piece.row + row) // 2
                captured_col = (piece.col + col) // 2
                captured_piece = self.board.grid[captured_row][captured_col]
                self.board.capture_piece(captured_piece)
            self.board.move_piece(piece, row, col)
            if not piece.is_king and ((piece.color == 'white' and row == 0) or (piece.color == 'black' and row == 7)):
                piece.is_king = True
            self.switch_turn()


    def get_valid_moves(self, piece):
        moves = []
        if piece.is_king:
            directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        elif piece.color == 'white':
            directions = ((-1, -1), (-1, 1))
        else:
            directions = ((1, -1), (1, 1))
        for r, c in directions:
            row, col = piece.row + r, piece.col + c
            if 0 <= row < 8 and 0 <= col < 8 and self.board.grid[row][col] is None:
                moves.append((row, col))
            elif 0 <= row < 8 and 0 <= col < 8 and self.board.grid[row][col].color != piece.color:
                row, col = row + r, col + c
                if 0 <= row < 8 and 0 <= col < 8 and self.board.grid[row][col] is None:
                    moves.append((row, col))
        jumps = []
        for r, c in directions:
            row, col = piece.row + r, piece.col + c
            if 0 <= row < 8 and 0 <= col < 8 and self.board.grid[row][col] is not None and self.board.grid[row][col].color != piece.color:
                row, col = row + r, col + c
                if 0 <= row < 8 and 0 <= col < 8 and self.board.grid[row][col] is None:
                    jumps.append((row, col))
        if jumps:
            return jumps
        return moves

if __name__ == '__main__':
    checkers = Checkers()
    gui = CheckersGUI(checkers)
