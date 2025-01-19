import sqlite3

connection = sqlite3.connect("database_14_4.db")
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
        data_products += {f'Название: {i[0]} | Описание: {i[1]} | Цена: {i[2]}'}
    connection.commit()
    return data_products

#data = get_all_products()
#print(data)