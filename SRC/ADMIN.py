import json

PRODUCT_FILE = 'products.json'
USER_FILE = 'users.json'

def load_products():
    try:
        with open(PRODUCT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_products(products):
    with open(PRODUCT_FILE, 'w') as f:
        json.dump(products, f, indent=4)

# Admin actions: Add, Edit, Delete Products
def add_product(product_id, name, price, stock):
    products = load_products()
    products[product_id] = {'name': name, 'price': price, 'stock': stock}
    save_products(products)
    return f"Product {name} added successfully!"

def delete_product(product_id):
    products = load_products()
    if product_id in products:
        del products[product_id]
        save_products(products)
        return f"Product {product_id} deleted successfully!"
    return "Product not found."

def update_product(product_id, name=None, price=None, stock=None):
    products = load_products()
    if product_id in products:
        if name:
            products[product_id]['name'] = name
        if price:
            products[product_id]['price'] = price
        if stock:
            products[product_id]['stock'] = stock
        save_products(products)
        return f"Product {product_id} updated successfully!"
    return "Product not found."

# Admin actions: Manage Users
def delete_user(username):
    try:
        with open(USER_FILE, 'r') as f:
            users = json.load(f)
        if username in users:
            del users[username]
            with open(USER_FILE, 'w') as f:
                json.dump(users, f, indent=4)
            return f"User {username} deleted."
        else:
            return "User not found."
    except FileNotFoundError:
        return "No users to delete."