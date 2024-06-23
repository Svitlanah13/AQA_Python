import sqlite3

connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    );
""")

cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Апельсин', 0.5, 100))
cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Яблуко', 0.3, 200))
cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Банан', 0.2, 150))

connection.commit()

print("All products:")
for row in cursor.execute("SELECT * FROM Products"):
    print(row)

print("\nProducts with price > 0.25:")
for row in cursor.execute("SELECT * FROM Products WHERE price > 0.25"):
    print(row)

cursor.execute("UPDATE Products SET price = 0.25 WHERE name = 'Банан'")
connection.commit()

print("\nUpdated products:")
for row in cursor.execute("SELECT * FROM Products"):
    print(row)

cursor.execute("DELETE FROM Products WHERE name = 'Яблуко'")
connection.commit()

print("\nAfter deletion:")
for row in cursor.execute("SELECT * FROM Products"):
    print(row)

connection.close()