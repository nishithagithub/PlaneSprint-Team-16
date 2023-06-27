from flask import Flask, request,render_template,redirect
import sqlite3

app = Flask(__name__)

@app.route('/Submit', methods=['POST'])
def submit():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email_id = request.form.get('Email_id')
    password = request.form.get('newpassword')

    # Connect to the database
    conn = sqlite3.connect('dat.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       firstname TEXT,
                       lastname TEXT,
                       email TEXT,
                       password TEXT)''')

    # Insert the data into the table
    cursor.execute('INSERT INTO users (firstname, lastname, email, password) VALUES (?, ?, ?, ?)',
                   (firstname, lastname, email_id, password))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return 'Data stored successfully!'
@app.route('/lsubmit',methods=['POST'])
def lsubmit():
    email = request.form['email']
    password = request.form['pwd']
        
        # Connect to the database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
        
        # Execute a SELECT query to check if the user exists
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        
        # Fetch the result
    result = cursor.fetchone()
    
     
    if result:
            # User exists, perform necessary actions
            # Redirect to another page or return a success message
        return  render_template('hackathon.html')
    else:
            # User does not exist or invalid credentials
            # Redirect to an error page or return an error message
        return "Invalid email or password!"


if __name__ == '__main__':
    app.run(debug=True)