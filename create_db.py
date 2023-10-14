import mysql.connector

# Configure your MySQL database connection here
db_config = {
    'host': 'localhost',
    'user': 'sharo',
    'password': 'Jarvis@8956',
    'database': 'login_db',
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # Assuming 'users' is the name of your table
    result = cursor.fetchall()

    for row in result:
        print(row)  # Print each row of the table

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
