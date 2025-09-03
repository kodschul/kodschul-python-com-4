from sql_db import conn, cursor

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT,
        age INTEGER
    )
""")

cursor.execute("""
    INSERT INTO customers (name, city, age) 
    VALUES 
    ('John Doe', 'New York', 30), 
    ('Eva Mustermann', 'Stuttgart', 40)
""")


conn.commit()