import sqlite3
import bcrypt

def login(username, password):
    # Input validation
    if len(username) < 3 or len(password) < 8:
        print("Invalid credentials")
        return
    
    try:
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT password_hash FROM users WHERE username = ?", 
                (username,)
            )
            result = cursor.fetchone()
            
            if result and bcrypt.checkpw(password.encode(), result[0]):
                print("Login successful!")
            else:
                print("Invalid credentials")  # Generic message
    
    except sqlite3.Error as e:  # ADDED MISSING EXCEPT BLOCK
        print(f"Database error: {str(e)}")

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)