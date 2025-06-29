import sqlite3
import bcrypt

# Hash a password
password = "SecurePass123".encode()
hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

# Connect to DB
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Insert test user
cursor.execute(
    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
    ("test_user", hashed_pw)
)

conn.commit()
conn.close()
print("Test user 'test_user' added with password 'SecurePass123'")