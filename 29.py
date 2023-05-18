from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton


class Window(QWidget):
    def __init__(self, goods):
        super().__init__()
        self.goods = goods
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Магазины и товары')
        layout = QVBoxLayout()

        label = QLabel('Введите название магазина:')
        layout.addWidget(label)

        self.shopInput = QLineEdit()
        layout.addWidget(self.shopInput)

        button = QPushButton('Найти товары')
        button.clicked.connect(self.searchGoods)
        layout.addWidget(button)

        self.resultLabel = QLabel('')
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)
        self.show()

    def searchGoods(self):
        shop = self.shopInput.text().strip()
        found = False
        result = ''

        for item in self.goods:
            if item[1] == shop:
                result += f"{item[0]} продается за {item[2]} тенге\n"
                found = True

        if not found:
            result = f"Такого {shop} нет"

        self.resultLabel.setText(result)


if __name__ == '__main__':
    goods = [
        ['телевизор', 'МВидео', 50000],
        ['ноутбук', 'DNS', 80000],
        ['холодильник', 'Эльдорадо', 30000],
        ['планшет', 'МВидео', 25000],
        ['компьютер', 'DNS', 60000]
    ]
    app = QApplication([])
    window = Window(goods)
    app.exec_()
