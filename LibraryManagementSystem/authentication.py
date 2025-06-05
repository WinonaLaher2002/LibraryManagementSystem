import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="pma",  # Change this to your MySQL username
    password="@Winonalaher2002",  # Change this to your MySQL password
)

# Create a cursor object
cursor = conn.cursor()

# Create the database if it doesn't exist
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_management")
    print("Database created successfully!")
except Exception as e:
    print("Error creating database:", e)

# Connect to the library_management database
conn.database = "library_management"

# Create the books table
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            isbn VARCHAR(50) NOT NULL,
            quantity INT NOT NULL,
            borrowed_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            student_fullname VARCHAR(255),
            student_id VARCHAR(50)
        )
    """)
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:", e)

# Close the cursor and connection
cursor.close()
conn.close()
