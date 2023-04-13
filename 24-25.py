
import tkinter as tk

# список вопросов и ответов
questions = [
    {"question": "Сколько будет 8*2?",
        "options": ["16", "18", "20", "22"], "answer": "16"},
    {"question": "Какая планета находится между Меркурием и Венерой?", "options": [
        "Марс", "Марс и Земля", "Земля", "Нет правильного ответа"], "answer": "Нет правильного ответа"},
    {"question": "Кто написал произведение \"Преступление и наказание\"?", "options": [
        "Достоевский", "Толстой", "Пушкин", "Гончаров"], "answer": "Достоевский"},
    {"question": "Как называется главный герой романа \"Мастер и Маргарита\"?",
        "options": ["Михаил", "Иван", "Воланд", "Макар"], "answer": "Воланд"},
    {"question": "Как звали создателя музыки к фильму \"Время\", режиссером которого является Кристофер Нолан?",
        "options": ["Джеймс Хорнер", "Ханс Циммер", "Йохан Йоханссон", "Макс Рихтер"], "answer": "Ханс Циммер"}
]

# функция для проверки ответов и вывода результатов


def check_answers():
    correct = 0
    for i in range(len(questions)):
        answer = answer_vars[i].get()
        if answer == questions[i]["answer"]:
            correct += 1
    total = len(questions)
    percent = correct/total * 100
    result_label.config(
        text=f"Правильных ответов: {correct}/{total} ({percent:.2f}%)")


# создание главного окна приложения
root = tk.Tk()
root.title("Тест")
root.geometry("600x680")

# список для хранения переменных выбранных ответов
answer_vars = []

# создание компонентов для каждого вопроса
for i, question in enumerate(questions):
    question_label = tk.Label(root, text=f"{i+1}. {question['question']}")
    question_label.pack()
    var = tk.StringVar(root, question["options"][0])
    answer_vars.append(var)
    for j, option in enumerate(question["options"]):
        option_radio = tk.Radiobutton(
            root, text=option, variable=var, value=option)
        option_radio.pack()

# создание кнопки для проверки ответов
check_button = tk.Button(root, text="Проверить", command=check_answers)
check_button.pack()

# создание метки для вывода результатов
result_label = tk.Label(root)
result_label.pack()

root.mainloop()
'''

1. Сколько будет 8*2?
(*) 16
( ) 18
( ) 20
( ) 22

2. Какая планета находится между Меркурием и Венерой?
( ) Марс
( ) Марс и Земля
( ) Земля
(*) Нет правильного ответа

3. Кто написал произведение "Преступление и наказание"?
( ) Достоевский
( ) Толстой
( ) Пушкин
( ) Гончаров

4. Как называется главный герой романа "Мастер и Маргарита"?
( ) Михаил
( ) Иван
(*) Воланд
( ) Макар

5. Как звали создателя музыки к фильму "Время", режиссером которого является Кристофер Нолан?
( ) Джеймс Хорнер
(*) Ханс Циммер
( ) Йохан Йоханссон
( ) Макс Рихтер

[Проверить]
------------
'''
