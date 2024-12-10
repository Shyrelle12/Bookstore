from flask import Flask, render_template, request, redirect, jsonify, flash, url_for, session
from datetime import datetime
from mysql.connector import connect
import random
app = Flask(__name__, template_folder='templates')
app.secret_key ='many random bytes'

def db_connect()->object:
    return connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="shyrelle"
    )

@app.route('/')
def index():
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', data=data)

@app.route('/admin_dashboard')
def admin_dashboard():
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('admin_dashboard.html', data=data)   

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        password = request.form['password']

        connection = db_connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM customer WHERE name = %s AND email = %s AND address = %s", (name, email, address))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Email already exists. Please choose another email.")
        else:
            role = 'user'
            cursor.execute("INSERT INTO customer (name, email, address, password, role) VALUES (%s, %s, %s, %s, %s)", (name, email, address, password, role))
            connection.commit()
            flash("Registration successful! You can now login.")

        cursor.close()
        connection.close()

        return redirect(url_for('index'))

    return render_template('register.html')

#index
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = db_connect()
        cursor = connection.cursor()
        query = "SELECT id, role FROM customer WHERE email = %s AND password = %s" 
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            id, role = user
            session['id'] = id

            if role == 'user':
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('customer_dashboard'))
            elif role == 'admin':
                session['admin_logged_in'] = True
                session['admin_username'] = username
                return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', category='error')

        cursor.close()
        connection.close()

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    flash("Logout successful!")
    return redirect(url_for('index'))


@app.route('/customerlist', methods=['POST', 'GET'])
def customerlist():
    data = []
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    
    if request.method == 'POST':
        search = request.form['search']
        cursor.execute("SELECT * FROM customer WHERE name LIKE %s OR email LIKE %s", ('%' + search + '%', '%' + search + '%'))
    else:
        cursor.execute("SELECT * FROM customer")

    data = cursor.fetchall()  
    print(data)
    
    cursor.close()
    connection.close()

    return render_template('customerlist.html', customer=data)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        flash("Data inserted successfully!")
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']

        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer (name, email, address) VALUES (%s, %s, %s)", (name, email, address))
        connection.commit()
        cursor.close()
        connection.close()
        new_user = {"name": name, "email": email, "address": address}
        return redirect(url_for('customerlist'))

@app.route('/deleteuser/<int:user_id>', methods=['GET'])
def delete(user_id):
    flash("Record Has Been Deleted successfully!")
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM customer WHERE id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('customerlist'))


@app.route('/edituser/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']

        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE customer SET name = %s, email = %s, address = %s WHERE id = %s", (name, email, address, user_id))
        connection.commit()
        cursor.close()
        connection.close()

        flash("Record Has Been Updated successfully!")
        return redirect(url_for('customerlist'))

    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('edit.html', user=user_data)


#------------------------------------------------------------------------------------------------------------------------------------

#ITEMLIST #admin_dashboard

@app.route('/itemlist', methods=['POST', 'GET'])
def itemlist():
    data = []
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)

    if request.method == 'POST':
        search = request.form['search']
        cursor.execute("SELECT * FROM itemlist WHERE title LIKE %s OR author LIKE %s", ('%' + search + '%', '%' + search + '%'))
    else:
        cursor.execute("SELECT * FROM itemlist")

    items = cursor.fetchall()
    
    cursor.close()
    connection.close()

    return render_template('itemlist.html', items=items)

@app.route('/edititem/<int:item_id>', methods=['GET', 'POST'])
def edititem(item_id):
    if request.method == 'POST':
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        price = request.form['price']
        type = request.form['type']

        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE itemlist SET isbn = %s, title = %s, author = %s, genre = %s, price = %s, type = %s WHERE id = %s",
                       (isbn, title, author, genre, price, type, item_id))
        connection.commit()
        cursor.close()
        connection.close()

        flash("Record Has Been Updated successfully!")
        return redirect(url_for('itemlist'))

    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM itemlist WHERE id = %s", (item_id,))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('itemlist.html', item=user_data)

@app.route('/deleteitem/<int:item_id>', methods=['GET'])
def deleteitem(item_id):
    flash("Record Has Been Deleted successfully!")
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM itemlist WHERE id = %s", (item_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('itemlist'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        flash("Data inserted successfully!")
        isbn = unique_id = ''.join(str(random.randint(0, 9)) for _ in range(10))
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        price = request.form['price']
        type = request.form['type']

        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO itemlist (isbn, title, author, genre, price, type) VALUES (%s, %s, %s, %s, %s, %s)", (isbn, title, author, genre, price, type))
        connection.commit()
        cursor.close()
        connection.close()
        new_user = {"isbn": isbn, "title": title, "author": author, "genre": genre, "price": price, "type": type}
        return redirect(url_for('itemlist'))



#-----------------------------------------------------------------------------------------------------------------------------------

#CUSTOMER DASHBOARD

@app.route('/customer_dashboard', methods=['GET'])
def customer_dashboard():
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM itemlist ")
    items = cursor.fetchall()
    cursor.close()
    connection.close()
    print(items)
    return render_template('customer_dashboard.html', items=items)

@app.route('/add_to_cart/', methods=['POST'])
def add_to_cart():
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    qty = request.form.get('qty')
    item_id = int(request.form.get('id'))
    cursor.execute("SELECT * FROM itemlist WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    ok = int(request.form.get('qty'))
    if ok > item['qty']:
        flash('Quantity Exceeds')
    elif item['qty'] > 0:
        cursor.execute("SELECT * FROM cart WHERE i_id = %s AND c_id = %s", (item_id,session['id']))
        existing_item = cursor.fetchone()
        if existing_item:
            qty = existing_item['qty'] + int(qty)
            cursor.execute("UPDATE cart SET qty = %s  WHERE i_id = %s and c_id = %s",
                           (qty, item_id,session['id']))
        else:
            cursor.execute("INSERT INTO cart (i_id, c_id, qty) VALUES (%s, %s, %s)",
                           (item['id'],session['id'],qty))   
        new_qty = item['qty'] - ok
        cursor.execute("UPDATE itemlist SET qty = %s WHERE id = %s", (new_qty, item_id))
        connection.commit()
        #flash(f"{item['title']} added to cart successfully!", "success")
    else:
        flash(f"Sorry, {item['title']} is out of stock.", "error")

    cursor.close()
    connection.close()
    return redirect(url_for('customer_dashboard'))

@app.route('/remove_from_cart/<int:item_id>', methods=['GET'])
def remove_from_cart(item_id):
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM itemlist WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.execute("SELECT * FROM cart WHERE i_id = %s and c_id = %s", (item_id,session['id']))
    ok = cursor.fetchone()
    new_qty = item['qty'] + ok['qty']
    cursor.execute("UPDATE itemlist SET qty = %s WHERE id = %s", (new_qty, item_id))
    cursor.execute("DELETE FROM cart WHERE i_id = %s and c_id = %s", (item_id,session['id']))
    connection.commit()
    cursor.close()
    connection.close()

    flash("Item removed from the cart successfully!", "success")

    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT *, cart.qty as ok FROM cart INNER JOIN itemlist ON itemlist.id = cart.i_id WHERE  c_id = {session['id']}")
    cart_items = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('view_cart.html', cart_items=cart_items)

@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        connection = db_connect()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM cart WHERE c_id = {session['id']}")
        cart_items = cursor.fetchall()

        if not cart_items:
            flash("Your cart is empty. Add items before checking out.", "warning")
            return redirect(url_for('view_cart'))
        user_id = session.get('id')
        cursor.execute("SELECT name, address FROM customer WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()

        cursor.execute("INSERT INTO `orders` (c_id, address) VALUES (%s, %s)", (session['id'], user_data['address']))

        connection.commit()
        cursor.execute("SELECT * FROM `orders` WHERE o_id = LAST_INSERT_ID()")
        o_id = cursor.fetchone()
        o_id = o_id['o_id']
        for i in cart_items:
            cursor.execute("INSERT INTO `order_items` (o_id,i_id, qty) VALUES (%s,%s, %s)", (o_id,i['i_id'], i['qty']))
            connection.commit()
       

        cursor.execute(f"DELETE FROM cart WHERE c_id = {session['id']}")
        connection.commit()

        #flash("Checkout successful! Items have been checked out.", "success")

    except Exception as e:
        print(f"An error occurred during checkout: {str(e)}")
        flash("An error occurred during checkout. Please try again.", "error")

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('order_history'))

def save_checkout_items(cart_items, customer_name, customer_address):
    connection = db_connect()
    cursor = connection.cursor()

    for item in cart_items:
        cursor.execute(
            "INSERT INTO checkout_items (title, author, genre, price, type, qty, total_price, customer_name, customer_address, checkout_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (item['title'], item['author'], item['genre'], item['price'], item['type'], item['qty'], item['total_price'], customer_name, customer_address, datetime.now()))

    connection.commit()
    cursor.close()
    connection.close()

@app.route('/checkout_items/<o_id>')
def checkout_items(o_id):
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(f"SELECT itemlist.*, order_items.qty FROM order_items INNER JOIN itemlist ON itemlist.id = order_items.i_id WHERE order_items.o_id = {o_id}")
    checkout_items = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('checkout_items.html', checkout_items=checkout_items)



@app.route('/order_history')
def order_history():
    connection = db_connect()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM orders WHERE c_id = {session['id']}")
    order_history_items = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('order_history.html', checkout_items=order_history_items)
    



if __name__ == '__main__':
    app.run(debug=True)


