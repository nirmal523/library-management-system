import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON")

# Read and execute database.sql
with open('database.sql', 'r') as f:
    sql = f.read()
cursor.executescript(sql)



# Commit and close
conn.commit()
conn.close()

print("Database setup complete.")
