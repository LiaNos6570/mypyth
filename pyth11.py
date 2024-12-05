import sqlite3
from flask import Flask, jsonify
import threading
import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Flask-сервер
app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect("example.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/books', methods=['GET'])
def get_books():
    connection = get_db_connection()
    books = connection.execute("""
        SELECT Books.title, Authors.name AS author 
        FROM Books
        JOIN Authors ON Books.author_id = Authors.id
    """).fetchall()
    connection.close()
    return jsonify([dict(book) for book in books])

# Функция для запуска Flask-сервера в отдельном потоке
def run_server():
    app.run(debug=False, use_reloader=False)

# Tkinter-программа
def load_books():
    try:
        response = requests.get("http://127.0.0.1:5000/books")
        response.raise_for_status()
        books = response.json()
        for row in books:
            tree.insert("", "end", values=(row["title"], row["author"]))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось подключиться к серверу:\n{e}")

# Инициализация Flask-сервера в фоновом потоке
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# Создание Tkinter-интерфейса
root = tk.Tk()
root.title("Книги и авторы")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

tree = ttk.Treeview(frame, columns=("Название книги", "Автор"), show="headings", height=10)
tree.heading("Название книги", text="Название книги")
tree.heading("Автор", text="Автор")
tree.pack()

load_button = ttk.Button(root, text="Загрузить книги", command=load_books)
load_button.pack(pady=10)

root.mainloop()
