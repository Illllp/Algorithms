from tkinter import *
import random

class Checker:
    def __init__(self, color, position, isKing=False):
        self.color = color
        self.position = position
        self.isKing = isKing

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class Game:
    def __init__(self):
        self.active_player = Color(255, 0, 0)
        self.inactive_player = Color(0, 0, 0)
        self.board_size = 8
        self.checker_size = 40
        self.selected_checker = None
        self.checkers = {}
        self.canvas = None
        self.setup()
    
    def setup(self):
        self.canvas = Canvas(width=self.board_size * self.checker_size, height=self.board_size * self.checker_size)
        self.canvas.pack()
        
        for x in range(self.board_size):
            for y in range(self.board_size):
                if (x + y) % 2 == 0:
                    continue
                if y < 3:
                    color = self.inactive_player
                elif y > 4:
                    color = self.active_player
                else:
                    continue
                checker = Checker(color, (x, y))
                self.checkers[(x, y)] = checker
        
        self.draw_board()
        self.draw_checkers()
    
    def draw_board(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                x0 = x * self.checker_size
                y0 = (7 - y) * self.checker_size
                x1 = x0 + self.checker_size
                y1 = y0 + self.checker_size
                color = "#e6e6e6" if (x + y) % 2 == 0 else "#333333"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    
    def draw_checkers(self):
        for position, checker in self.checkers.items():
            x0 = position[0] * self.checker_size
            y0 = (7 - position[1]) * self.checker_size
            x1 = x0 + self.checker_size
            y1 = y0 + self.checker_size
            color = "#{:02x}{:02x}{:02x}".format(checker.color.red, checker.color.green, checker.color.blue)
            outline = "black" if checker == self.selected_checker else color
            self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline=outline)
            if checker.isKing:
                self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="K")
    
    def move(self, checker, position):
        self.checkers[position] = checker
        del self.checkers[checker.position]
        checker.position = position
        if position[1] == 0 and checker.color == self.inactive_player:
            checker.isKing = True
        elif position[1] == 7 and checker.color == self.active_player:
            checker.isKing = True
        
    def get_valid_moves(self, checker):
        x, y = checker.position
        moves = []
        jumps = []
        if checker.isKing or checker.color == self.active_player:
            for dx in (-1, 1):
                for dy in (-1, 1):
                    for dist in range(1, self.board_size):
                        if x + dx * dist < 0 or x + dx * dist >= self.board_size or y + dy * dist < 0 or y + dy * dist >= self.board_size:
                            break
                        position = (x + dx * dist, y + dy * dist)
                        if position in self.checkers:
                            break
                        if self.selected_checker is None or abs(x + dx * dist - self.selected_checker.position[0]) != 2:
                            moves.append(position)
                        else:
                            jumps.append(position)
                            break
        if checker.isKing or checker.color == self.inactive_player:
            for dx in (-1, 1):
                for dy in (-1, 1):
                    for dist in range(1, self.board_size):
                        if x + dx * dist < 0 or x + dx * dist >= self.board_size or y + dy * dist < 0 or y + dy * dist >=self.board_size:
                            break
                        position = (x + dx * dist, y + dy * dist)
                        if position not in self.checkers:
                            continue
                        if self.checkers[position].color == checker.color:
                            break
                        jump_position = (x + dx * (dist + 1), y + dy * (dist + 1))
                        if jump_position in self.checkers:
                            break
                        jumps.append(jump_position)
        return jumps if jumps else moves
    
    def select(self, position):
        if position in self.checkers and self.checkers[position].color == self.active_player:
            self.selected_checker = self.checkers[position]
        elif position in self.get_valid_moves(self.selected_checker):
            self.move(self.selected_checker, position)
            self.selected_checker = None
            self.active_player, self.inactive_player = self.inactive_player, self.active_player
        else:
            self.selected_checker = None
        self.canvas.delete("all")
        self.draw_board()
        self.draw_checkers()
    
    def run(self):
        self.canvas.bind("<Button-1>", lambda event: self.select((event.x // self.checker_size, 7 - event.y // self.checker_size)))
        mainloop()

game = Game()
game.run()