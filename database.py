import sqlite3

def connect():
    """
    Connect to the SQLite database and return the connection object.
    """
    conn = sqlite3.connect('passwords.db')
    return conn

def create_table():
    """
    Create a 'passwords' table in the database if it doesn't already exist.
    """
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  website TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL);''')
    conn.commit()
    conn.close()

def save_password(website, username, password):
    """
    Save a new password to the database.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
              (website, username, password))
    conn.commit()
    conn.close()

def get_passwords():
    """
    Retrieve all saved passwords from the database.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_password(id):
    """
    Delete a password with the specified ID from the database.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE id=?", (id,))
    conn.commit()
    conn.close()
