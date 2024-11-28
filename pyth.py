import tkinter
import random
import os

filename = input("Введите имя файла: ")
if not os.path.exists(filename):
    print(f"Файл {filename} не найден. Он будет создан.")

    with open(filename, "w") as file:
        random_numbers = [str(random.randint(1, 100)) for _ in range(10)]
        file.write(" ".join(random_numbers))
    print(f"Массив записан в файле {filename}")
else:
    print(f"Файл {filename} найден.")


with open(filename, "r") as file:
    content = file.read()

print(f"Содержимое файла {filename}:")
print(content)

numbers = list(map(int, content.split()))

average = sum(numbers) / len(numbers)
print(f"Среднее значение: {average:.2f}")