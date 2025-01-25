import sqlite3

connection = sqlite3.connect("database_14_5.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    #for i in range(1,11):
    #    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                   (f"Продукт {i}", f"Описание {i}", f"{i}00"))

    connection.commit()
    connection.close()

#initiate_db()

def get_all_products():
    products = cursor.execute("SELECT title, description, price FROM Products")
    data_products = []
    for i in products:
        data_products += {f"Название: {i[0]} | Описание: {i[1]} | Цена: {i[2]}"}
    connection.commit()
    return data_products

def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()

def is_included(username):
    check_user = cursor.execute(f"SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False