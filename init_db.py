import sqlite3

# Create database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table with hashed password column
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash BLOB NOT NULL
)
''')

# Commit and close
conn.commit()
conn.close()
print("Database initialized successfully!")