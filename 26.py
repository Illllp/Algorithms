import tkinter as tk
import math

# Function to calculate the parameters of the triangle


def calculate_parameters():
    # Get the values of the angles and sides from the input fields
    side_a = float(side_a_input.get())
    side_b = float(side_b_input.get())
    side_c = float(side_c_input.get())
    angle_A = float(angle_A_input.get())
    angle_B = float(angle_B_input.get())
    angle_C = float(angle_C_input.get())

    # Calculate the parameters of the triangle
    perimeter = side_a + side_b + side_c
    semiperimeter = perimeter / 2
    area = math.sqrt(semiperimeter * (semiperimeter - side_a)
                     * (semiperimeter - side_b) * (semiperimeter - side_c))
    height_a = 2 * area / side_a
    height_b = 2 * area / side_b
    height_c = 2 * area / side_c
    radius = area / semiperimeter
    inradius = area / semiperimeter
    circumradius = side_a / (2 * math.sin(math.radians(angle_A)))

    # Display the results in the memo field
    memo_field.delete(1.0, tk.END)
    memo_field.insert(tk.END, f"Сторона a: {side_a}\n")
    memo_field.insert(tk.END, f"Сторона b: {side_b}\n")
    memo_field.insert(tk.END, f"Сторона c: {side_c}\n")
    memo_field.insert(tk.END, f"Угол A: {angle_A}\n")
    memo_field.insert(tk.END, f"Угол B: {angle_B}\n")
    memo_field.insert(tk.END, f"Угол C: {angle_C}\n")
    memo_field.insert(tk.END, f"Периметр: {perimeter}\n")
    memo_field.insert(tk.END, f"Область: {area}\n")
    memo_field.insert(tk.END, f"Высота a: {height_a}\n")
    memo_field.insert(tk.END, f"Высота b: {height_b}\n")
    memo_field.insert(tk.END, f"Высота c: {height_c}\n")
    memo_field.insert(tk.END, f"Радиус: {radius}\n")
    memo_field.insert(tk.END, f"В радиусе: {inradius}\n")
    memo_field.insert(tk.END, f"Радиус окружности: {circumradius}\n")

# Function to display the task condition in the memo field


def display_condition():
    memo_field.delete(1.0, tk.END)
    memo_field.insert(
        tk.END, "Условие задачи: Вычислите параметры треугольника.\n")


# Create the main window
root = tk.Tk()
root.title("Калькулятор треугольников")

# Create the input fields for the sides and angles
side_a_label = tk.Label(root, text="Сторона a:")
side_a_label.grid(row=0, column=0)
side_a_input = tk.Entry(root)
side_a_input.grid(row=0, column=1)

side_b_label = tk.Label(root, text="Сторона b:")
side_b_label.grid(row=1, column=0)
side_b_input = tk.Entry(root)
side_b_input.grid(row=1, column=1)

side_c_label = tk.Label(root, text="Сторона c:")
side_c_label.grid(row=2, column=0)
side_c_input = tk.Entry(root)
side_c_input.grid(row=2, column=1)

angle_A_label = tk.Label(root, text="Угол A:")
angle_A_label.grid(row=3, column=0)
angle_A_input = tk.Entry(root)
angle_A_input.grid(row=3, column=1)

angle_B_label = tk.Label(root, text="Угол B:")
angle_B_label.grid(row=4, column=0)
angle_B_input = tk.Entry(root)
angle_B_input.grid(row=4, column=1)

angle_C_label = tk.Label(root, text="Угол C:")
angle_C_label.grid(row=5, column=0)
angle_C_input = tk.Entry(root)
angle_C_input.grid(row=5, column=1)

# Create the memo field for displaying the results
memo_field = tk.Text(root)
memo_field.grid(row=6, column=0, columnspan=2)

# Create the buttons for calculating the parameters and displaying the task condition
calculate_button = tk.Button(
    root, text="Calculate", command=calculate_parameters)
calculate_button.grid(row=7, column=0)

condition_button = tk.Button(root, text="Condition", command=display_condition)
condition_button.grid(row=7, column=1)

# Start the main loop
root.mainloop()
