import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import QRectF, Qt

# Размер ячейки на доске
CELL_SIZE = 50

# Класс Шашка
class Checker(QGraphicsItem):
    def __init__(self, color, row, column):
        super().__init__()
        self.color = color
        self.row = row
        self.column = column
        self.is_king = False
        
    # Функция отрисовки шашки
    def paint(self, painter, option, widget):
        rect = QRectF(self.column * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(Qt.black, 2))
        painter.drawEllipse(rect)
        if self.is_king:
            painter.setBrush(QBrush(QColor(255, 255, 255)))
            painter.drawEllipse(rect.center(), CELL_SIZE/5, CELL_SIZE/5)
    
    # Функция возврата ограничивающего прямоугольника
    def boundingRect(self):
        return QRectF(self.column * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    
    # Функция перемещения шашки
    def move(self, row, column):
        self.row = row
        self.column = column
        self.setPos(column * CELL_SIZE, row * CELL_SIZE)
        
# Класс Игровое поле
class Board(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checkers = []
        self.selected_checker = None
        self.init_board()
        
    # Функция отрисовки доски
    def draw_board(self):
        for row in range(8):
            for column in range(8):
                rect = QRectF(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if (row + column) % 2 == 0:
                    self.addRect(rect, QPen(Qt.black), QBrush(QColor(255, 206, 158)))
                else:
                    self.addRect(rect, QPen(Qt.black), QBrush(QColor(209, 139, 71)))
                    
    # Функция создания шашек на доске
    def init_board(self):
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 0:
                    checker = Checker(QColor(255, 0, 0), i, j)
                    self.addItem(checker)
                    self.checkers.append(checker)
                    
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    checker = Checker(QColor(0, 0, 255), i, j)
                    self.addItem(checker)
                    self.checkers.append(checker)
                    
    # Функция выбора шашки для перемещения
    def select_checker(self, checker):
        if self.selected_checker:
            self.selected_checker.setBrush(QBrush(self.selected_checker.color))
        self.selected_checker = checker
        self.selected_checker.setBrush(QBrush(QColor(0, 255, 0)))
            
    # Функция перемещения шашки
    def move_checker(self, row, column):
        if self.selected_checker:
            self.selected_checker.move(row, column)
            if row in [0, 7]:
                self.selected_checker.is_king = True
            self.selected_checker.setBrush(QBrush(self.selected_checker.color))
            self.selected_checker = None
            
    # Функция клика мыши
    def mousePressEvent(self, event):
        pos = event.scenePos()
        items = self.items(pos.x(), pos.y(), CELL_SIZE, CELL_SIZE)
        if len(items) > 0 and isinstance(items[0], Checker):
            self.select_checker(items[0])
        else:
            row = int(pos.y() // CELL_SIZE)
            column = int(pos.x() // CELL_SIZE)
            self.move_checker(row, column)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Board()
    view = QGraphicsView(scene)
    view.setWindowTitle('Checkers')
    view.setFixedSize(CELL_SIZE * 8, CELL_SIZE *8)
    view.show()
    sys.exit(app.exec_())