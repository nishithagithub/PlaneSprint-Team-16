from flask import Flask, render_template, request, redirect, session

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

    return redirect('/')

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
