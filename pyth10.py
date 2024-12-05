import sqlite3


# Инициализация базы данных
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Пересоздание таблиц
cursor.execute("DROP TABLE IF EXISTS Books")
cursor.execute("DROP TABLE IF EXISTS Authors")

# Создание таблиц
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
)
""")

# Наполнение базы данных
cursor.execute("INSERT INTO Authors (name) VALUES (?)", ("Лев Толстой",))
cursor.execute("INSERT INTO Authors (name) VALUES (?)", ("Фёдр Достоевский",))
cursor.execute("INSERT INTO Books (title, author_id) VALUES (?, ?)", ("Война и мир", 1))
cursor.execute("INSERT INTO Books (title, author_id) VALUES (?, ?)", ("Преступление и наказание", 2))

connection.commit()

# Чтение и вывод информации
cursor.execute("""
SELECT Books.title, Authors.name
FROM Books
JOIN Authors ON Books.author_id = Authors.id
""")

for row in cursor.fetchall():
    print(f"Книга: {row[0]}, Автор: {row[1]}")

# Закрытие соединения
connection.close()
