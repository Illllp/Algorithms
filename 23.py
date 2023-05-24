import tkinter as tk
import math

class Convertor:
    def __init__(self, master):
        self.master = master
        master.title("Конвертор радиан-градус")

        # Поле для ввода значения
        self.value_entry = tk.Entry(master)
        self.value_entry.pack()

        # Выбор перевода
        self.var = tk.StringVar(value="rad_to_deg")
        self.rad_to_deg = tk.Radiobutton(
            master, text="Радианы → Градусы",
            variable=self.var, value="rad_to_deg"
        )
        self.deg_to_rad = tk.Radiobutton(
            master, text="Градусы → Радианы",
            variable=self.var, value="deg_to_rad"
        )
        self.rad_to_deg.pack()
        self.deg_to_rad.pack()

        # Кнопка конвертирования
        self.convert_button = tk.Button(
            master, text="Конвертировать", command=self.convert
        )
        self.convert_button.pack()

        # Поле для вывода результата
        self.result_label = tk.Label(master)
        self.result_label.pack()

    def convert(self):
        value = float(self.value_entry.get())
        if self.var.get() == "rad_to_deg":
            result = math.degrees(value)
            self.result_label.config(
                text=f"{value:.2f} радиан = {result:.2f} градусов"
            )
        else:
            result = math.radians(value)
            self.result_label.config(
                text=f"{value:.2f} градусов = {result:.2f} радиан"
            )

# Создаем окно
root = tk.Tk()

# Запуск конвертора
convertor = Convertor(root)

# Запускаем главный цикл обработки событий
root.mainloop()
