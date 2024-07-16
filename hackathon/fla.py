from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key = 'nishiitha'  # Change this to a secure key in a production environment

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/index')
def indexhtml():
    return render_template('index.html')
@app.route('/h2')
def index3():
    return render_template('h2.html')
@app.route('/kritunga')
def index4():
    return render_template('kritunga.html')
@app.route('/pista')
def index5():
    return render_template('pista.html')
@app.route('/paradise')
def index6():
    return render_template('paradise.html')
@app.route('/login')
def index7():
    return render_template('login.html')
@app.route('/signup')
def index8():
    return render_template('signup.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.form.get('item')
    quantity = int(request.form.get('quantity'))

    cart_items = session.get('cart', [])
    cart_items.append((item, quantity))
    session['cart'] = cart_items
    return redirect('/index')
@app.route('/back',methods=['POST'])
def back():
    return redirect('/index')
@app.route('/Submit', methods=['POST'])
def submit():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email_id = request.form.get('Email_id')
    password = request.form.get('newpassword')

    # Connect to the database
    conn = sqlite3.connect('data.db')
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
        return  render_template('index.html')
    else:
            # User does not exist or invalid credentials
            # Redirect to an error page or return an error message
        return "Invalid email or password!"

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_bill = calculate_total_bill(cart_items)
    return render_template('checkout.html', cart=cart_items, total_bill=total_bill,get_item_price=get_item_price)

def calculate_total_bill(cart_items):
    total = 0
    for item, quantity in cart_items:
        # Assuming there is a function to calculate the price for each item
        # Modify this based on your implementation
        price = get_item_price(item)
        total += price * quantity
    return total

def get_item_price(item):
    # Implement your logic to fetch the price of the item from a database or any other source
    # This is just a placeholder, replace it with your actual implementation
    return 10

if __name__ == '__main__':
    app.run(debug=True)
