# # from flask import Flask, render_template, request, redirect, url_for, flash, session
# # from werkzeug.security import generate_password_hash, check_password_hash
# # from database import db, User
# # import os
# # import subprocess
# # import threading

# # app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'your_secret_key'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # Initialize the database
# # db.init_app(app)

# # # SignUp Route
# # @app.route('/signup', methods=['GET', 'POST'])
# # def signup():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
        
# #         hashed_password = generate_password_hash(password, method='sha256')
        
# #         # Check if user already exists
# #         existing_user = User.query.filter_by(username=username).first()
# #         if existing_user:
# #             flash('Username already exists!', 'danger')
# #         else:
# #             new_user = User(username=username, password=hashed_password)
# #             db.session.add(new_user)
# #             db.session.commit()
# #             flash('Account created successfully!', 'success')
# #             return redirect(url_for('login'))
    
# #     return render_template('signup.html')

# # # Login Route
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
        
# #         user = User.query.filter_by(username=username).first()
# #         if user and check_password_hash(user.password, password):
# #             session['user_id'] = user.id
# #             return redirect(url_for('home'))
# #         else:
# #             flash('Invalid credentials!', 'danger')
    
# #     return render_template('login.html')

# # # Home Route (Runs the gesture control script)
# # @app.route('/home')
# # def home():
# #     if 'user_id' not in session:
# #         return redirect(url_for('login'))
    
# #     # Run the gesture control script in a separate thread
# #     threading.Thread(target=run_gesture_control).start()
    
# #     return render_template('home.html')

# # def run_gesture_control():
# #     # This will run your gcs.py script
# #     os.system('python gcs.py')

# # if __name__ == '__main__':
# #     app.run(debug=True)




# from flask import Flask, render_template, request, redirect
# import sqlite3

# app = Flask(__name__)

# # Home route - Login Page
# @app.route('/')
# def home():
#     return render_template('login.html')

# # Signup route - for new user registration
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Save the user to the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()

#         # Check if username already exists
#         cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
#         user = cursor.fetchone()

#         if user:
#             return "Username already exists, please choose a different username."

#         # Insert new user
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()

#         return redirect('/login')  # Redirect to login page after successful signup

#     return render_template('signup.html')

# # Login route - for existing users
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Check if user exists in the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             # Successful login, redirect to dashboard or the main page
#             return redirect('/dashboard')  # Or any page you want after login
#         else:
#             return "Invalid credentials, please try again."

#     return render_template('login.html')

# # Dashboard route (after successful login)
# @app.route('/dashboard')
# def dashboard():
#     return "Welcome to the Dashboard!"

# # Initialize the SQLite database
# def init_db():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()

#     # Create the users table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Run the app
# if __name__ == '__main__':
#     init_db()  # Initialize database when the app starts
#     app.run(debug=True)





# import subprocess
# from flask import Flask, render_template, request, redirect
# import sqlite3
# import threading

# app = Flask(__name__)

# # Home route - Login Page
# @app.route('/')
# def home():
#     return render_template('login.html')

# # Signup route - for new user registration
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Save the user to the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()

#         # Check if username already exists
#         cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
#         user = cursor.fetchone()

#         if user:
#             return "Username already exists, please choose a different username."

#         # Insert new user
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()

#         return redirect('/login')  # Redirect to login page after successful signup

#     return render_template('signup.html')

# # Login route - for existing users
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Check if user exists in the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             # Successful login, redirect to dashboard
#             return redirect('/dashboard')  # Or any page you want after login
#         else:
#             return "Invalid credentials, please try again."

#     return render_template('login.html')

# # Dashboard route (after successful login)
# @app.route('/dashboard')
# def dashboard():
#     # Start the gcs.py script in a separate thread so it doesn't block the web server
#     thread = threading.Thread(target=run_gcs_script)
#     thread.start()
    
#     return "Welcome, Gesture control is active now, Wait until light Camera turns on" 

# # Function to run the gcs.py script
# def run_gcs_script():
#     try:
#         # Ensure that the gcs.py script is in the same directory as this Flask app or provide the full path
#         subprocess.run(["python", "gcs.py"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running gcs.py: {e}")

# # Initialize the SQLite database
# def init_db():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()

#     # Create the users table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Run the app
# if __name__ == '__main__':
#     init_db()  # Initialize database when the app starts
#     app.run(debug=True)








# import subprocess
# from flask import Flask, render_template, request, redirect
# import sqlite3
# import threading

# app = Flask(__name__)

# # Home route - Login Page
# @app.route('/')
# def home():
#     return render_template('login.html')

# # Signup route - for new user registration
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Save the user to the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()

#         # Check if username already exists
#         cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
#         user = cursor.fetchone()

#         if user:
#             return "<h2 style='color: red; text-align: center;'>Username already exists, please choose a different username.</h2>"

#         # Insert new user
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()

#         return redirect('/login')  # Redirect to login page after successful signup

#     return render_template('signup.html')

# # Login route - for existing users
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Check if user exists in the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             # Successful login, redirect to dashboard
#             return redirect('/dashboard')
#         else:
#             return "<h2 style='color: red; text-align: center;'>Invalid credentials, please try again.</h2>"

#     return render_template('login.html')

# # Dashboard route (after successful login)
# @app.route('/dashboard')
# def dashboard():
#     # Start the gcs.py script in a separate thread so it doesn't block the web server
#     thread = threading.Thread(target=run_gcs_script)
#     thread.start()

#     # Return a well-designed HTML message
#     html_content = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Dashboard</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background: linear-gradient(135deg, #74ebd5, #9face6);
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 height: 100vh;
#                 margin: 0;
#                 color: #333;
#             }
#             .message-container {
#                 background: white;
#                 padding: 20px 30px;
#                 border-radius: 10px;
#                 box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
#                 text-align: center;
#             }
#             h1 {
#                 color: #6c63ff;
#                 font-size: 24px;
#                 margin-bottom: 10px;
#             }
#             p {
#                 color: #333;
#                 font-size: 18px;
#                 margin-top: 0;
#             }
#             .highlight {
#                 color: #4caf50;
#                 font-weight: bold;
#             }
#         </style>
#     </head>
#     <body>
#         <div class="message-container">
#             <h1>Welcome to Gesture Control Dashboard</h1>
#             <p>
#                 Gesture control is now <span class="highlight">active</span>. <br>
#                 Please wait until the <span class="highlight">light at camera</span> turns on.
#             </p>
#         </div>
#     </body>
#     </html>
#     """
#     return html_content

# # Function to run the gcs.py script
# def run_gcs_script():
#     try:
#         # Ensure that the gcs.py script is in the same directory as this Flask app or provide the full path
#         subprocess.run(["python", "gcs.py"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running gcs.py: {e}")

# # Initialize the SQLite database
# def init_db():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()

#     # Create the users table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Run the app
# if __name__ == '__main__':
#     init_db()  # Initialize database when the app starts
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect
import sqlite3
import threading
import subprocess

app = Flask(__name__)

# Home route - Login Page
@app.route('/')
def home():
    return render_template('login.html')

# Signup route - for new user registration
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save the user to the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            return "Username already exists, please choose a different username."

        # Insert new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect('/login')  # Redirect to login page after successful signup

    return render_template('signup.html')

# Login route - for existing users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            # Successful login, redirect to dashboard
            return redirect('/dashboard')
        else:
            return "Invalid credentials, please try again."

    return render_template('login.html')

# Dashboard route (after successful login)
@app.route('/dashboard')
def dashboard():
    # Start the gcs.py script in a separate thread so it doesn't block the web server
    thread = threading.Thread(target=run_gcs_script)
    thread.start()
    
    # Render a custom Spiderman-themed dashboard
    return render_template('dashboard.html')

# Function to run the gcs.py script
def run_gcs_script():
    try:
        # Ensure that the gcs.py script is in the same directory as this Flask app or provide the full path
        subprocess.run(["python", "gcs.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running gcs.py: {e}")

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Run the app
if __name__ == '__main__':
    init_db()  # Initialize database when the app starts
    app.run(debug=True)
