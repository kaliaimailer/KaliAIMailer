import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data/example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert a row of data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")

# Save (commit) the changes
conn.commit()

# Query the database and return all entries
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close the connection when done
conn.close()
