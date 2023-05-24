from tkinter import *
import os

root = Tk()
root.geometry("200x200")

# Функция для переключения между программами по щелчку на значке
def switch_program():
    os.system("taskkill /im notepad.exe") # закрытие запущенной программы
    
    # проверка, какая программа запущена, и запуск другой программы
    if btn.cget('text') == "Run Program 1":
        os.system("notepad")
        btn.config(text="Run Program 2")
    else:
        os.system("calc")
        btn.config(text="Run Program 1")

# Создаем кнопку-значок
btn = Button(root, text="Run Program 1", command=switch_program, padx=10, pady=10)
btn.pack(pady=50)

root.mainloop()