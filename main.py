from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'this is your key'

# Configure your MySQL database connection here
db_config = {
    'host': 'localhost',
    'user': 'sharo',
    'password': 'Jarvis@8956',
    'database': 'login_db',
}

def sql_connect():
    global conn, cursor
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        ''')
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()



@app.route('/home')
def home():
    return 'Welcome to the Home Page'


@app.route('/', methods=['GET', 'POST'])
def login():
    sql_connect()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()

            if result:
                session['user'] = username
                flash('Login successful!', 'success')
            else:
                flash('Login unsuccessful. Please check your credentials.', 'danger')

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

        return redirect(url_for('home'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
