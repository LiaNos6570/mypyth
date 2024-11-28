import tkinter as tk
from tkinter import filedialog, messagebox
import random
import os


# Функция для создания нового файла с числами
def create_file(filename):
    with open(filename, "w") as file:
        random_numbers = [str(random.randint(1, 100)) for _ in range(10)]
        file.write(" ".join(random_numbers))
    return random_numbers



def choose_file():
    filename = filedialog.asksaveasfilename(
        title="Выберите или создайте файл",
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)



def process_file():
    filename = file_entry.get()

    if not filename:
        messagebox.showerror("Ошибка", "Введите имя файла или выберите его.")
        return

    if not os.path.exists(filename):
        messagebox.showinfo("Информация", f"Файл {filename} не найден. Он будет создан.")
        numbers = create_file(filename)
    else:
        messagebox.showinfo("Информация", f"Файл {filename} найден.")
        with open(filename, "r") as file:
            content = file.read()
        numbers = list(map(int, content.split()))

    with open(filename, "r") as file:
        content = file.read()


    file_content_label.config(text=f"Содержимое файла:\n{content}")


    average = sum(numbers) / len(numbers)
    average_label.config(text=f"Среднее значение: {average:.2f}")



def calculate():
    try:
        expression = calc_entry.get()
        result = eval(expression)
        calc_result_label.config(text=f"Результат: {result}")
    except Exception as e:
        calc_result_label.config(text="Ошибка ввода")



root = tk.Tk()
root.title("Работа с файлами и калькулятор")


file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="Имя файла:")
file_label.pack(side=tk.LEFT, padx=5)

file_entry = tk.Entry(file_frame, width=40)
file_entry.pack(side=tk.LEFT, padx=5)

choose_button = tk.Button(file_frame, text="Выбрать файл", command=choose_file)
choose_button.pack(side=tk.LEFT, padx=5)

run_button = tk.Button(root, text="Запуск", command=process_file)
run_button.pack(pady=10)

file_content_label = tk.Label(root, text="Содержимое файла:", justify=tk.LEFT)
file_content_label.pack(pady=10)

average_label = tk.Label(root, text="Среднее значение:", justify=tk.LEFT)
average_label.pack(pady=10)


calc_frame = tk.Frame(root)
calc_frame.pack(pady=20)

calc_label = tk.Label(calc_frame, text="Калькулятор:")
calc_label.pack()

calc_entry = tk.Entry(calc_frame, width=30)
calc_entry.pack(pady=5)

calc_button = tk.Button(calc_frame, text="Вычислить", command=calculate)
calc_button.pack()

calc_result_label = tk.Label(calc_frame, text="Результат:")
calc_result_label.pack(pady=5)

root.mainloop()