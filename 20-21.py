sum = 0 # переменная для подсчета суммы
while True:
    char = input("Введите символ или нажмите Esc для выхода: ")
    if char == '\x1b': # если нажата клавиша Esc, то выходим из цикла
        break
    sum += ord(char) # добавляем код символа к сумме
print(f"Сумма кодов всех символов: {sum}")
# Изменение со стороны Ксении Степановой
