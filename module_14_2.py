import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Добовляем записи.
#for i in range(1,11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                   (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))
#
## Обновляем баланс.
#for i in range(1,11,2):
#    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", ("500", f"User{i}"))
#
## Удаляем записи.
#for i in range(1,11,3):
#    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))
#
## Производим выборку.
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ("60",))
#users = cursor.fetchall()
#for user in users:
#    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# Удаление из базы данных.
cursor.execute("DELETE FROM Users WHERE id = ?", ("6",))

# Подсчёт кол-во записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]

# Подсчёт суммы всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
summa = cursor.fetchone()[0]

# Подсчёт среднего баланса
cursor.execute("SELECT AVG(balance) From Users")
avg = cursor.fetchone()[0]
print(avg)

connection.commit()
connection.close()