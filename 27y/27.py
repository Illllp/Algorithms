from tkinter import *
import os

def program1():
    os.system('python "C:/Синергия колледж/2 курс/4-й семестр/Алгоритмы/Лабы/Algorithms/27y/24-25.py"')

def program2():
    os.system('python "C:/Синергия колледж/2 курс/4-й семестр/Алгоритмы/Лабы/Algorithms/27y/26.py"')

# создаем окно
root = Tk()

# создаем меню
menu = Menu(root)
root.config(menu=menu)

# создаем подменю "Программы"
program_menu = Menu(menu)
menu.add_cascade(label="Программы", menu=program_menu)

# добавляем пункты меню
program_menu.add_command(label="24-25", command=program1)
program_menu.add_command(label="26", command=program2)

# запускаем главный цикл окна
root.mainloop()