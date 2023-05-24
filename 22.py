from tkinter import *
from tkinter import messagebox

password = "12345" # задаем пароль для переписывания списка

def reverse_list():
    # функция для переписывания списка в обратном порядке
    if password_entry.get() != password:
        # проверяем правильность введенного пароля
        messagebox.showerror("Ошибка", "Неправильный пароль!")
        return
        
    # переписываем список в обратном порядке
    listbox2.delete(0, END)
    for item in reversed(listbox1.get(0, END)):
        listbox2.insert(END, item)
        
def insert_item():
    # функция для добавления элемента в список
    if len(listbox1.get(0, END)) >= 10:
        # проверяем, что в списке не больше 10 элементов
        messagebox.showerror("Ошибка", "Список может содержать максимум 10 элементов!")
        return
        
    item = item_entry.get()
    if item == "":
        # элемент не может быть пустым
        messagebox.showerror("Ошибка", "Элемент не может быть пустым!")
        return
        
    # добавляем элемент в список
    listbox1.insert(END, item)
    item_entry.delete(0, END)
    
# создаем окно приложения
root = Tk()
root.title("Список")

# создаем компоненты для добавления элемента в список
item_label = Label(root, text="Добавить элемент:")
item_label.grid(row=0, column=0)
item_entry = Entry(root)
item_entry.grid(row=0, column=1)
insert_button = Button(root, text="Добавить", command=insert_item)
insert_button.grid(row=0, column=2)

# создаем компоненты для отображения списка
listbox1_label = Label(root, text="Список:")
listbox1_label.grid(row=1, column=0)
listbox1 = Listbox(root)
listbox1.grid(row=2, column=0, rowspan=2)
listbox2_label = Label(root, text="Переписанный список:")
listbox2_label.grid(row=1, column=2)
listbox2 = Listbox(root)
listbox2.grid(row=2, column=2, rowspan=2)

# создаем компоненты для переписывания списка
password_label = Label(root, text="Введите пароль для переписывания списка:")
password_label.grid(row=4, column=0, columnspan=2)
password_entry = Entry(root, show="*")
password_entry.grid(row=5, column=0, columnspan=2)
reverse_button = Button(root, text="Переписать список в обратном порядке", command=reverse_list)
reverse_button.grid(row=6, column=0, columnspan=2)

root.mainloop()