import json
import os
import datetime
from SRC.PRODUCT import Product
from SRC.COLORS import Colors

PRODUCTS_FILE = os.path.join('database', 'products.json')
HISTORY_FILE = os.path.join('database', 'history.json')

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.history = {}

    def load_products(self):
        if os.path.exists(PRODUCTS_FILE):
            with open(PRODUCTS_FILE, "r") as file:
                self.products = json.load(file)
        return self.products

    def save_products(self):
        with open(PRODUCTS_FILE, "w") as file:
            json.dump(self.products, file, indent=4)

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                self.history = json.load(file)
        return self.history

    def save_history(self):
        with open(HISTORY_FILE, "w") as file:
            json.dump(self.history, file, indent=4)

    def add_product(self, user, product_id, name, price, quantity):
        if product_id in self.products:
            print(Colors.FAIL + "Product ID already exists." + Colors.ENDC)
            return
        self.products[product_id] = Product(product_id, name, price, quantity, user.username).to_dict()
        self.save_products()
        print(Colors.OKGREEN + f"Product '{name}' added successfully!" + Colors.ENDC)

    def update_product(self, user, product_id, name=None, price=None, quantity=None):
        if product_id not in self.products:
            print(Colors.FAIL + "Product ID does not exist." + Colors.ENDC)
            return
        product = self.products[product_id]
        if name:
            product['name'] = name
        if price:
            product['price'] = price
        if quantity:
            product['quantity'] = quantity
        self.save_products()
        print(Colors.OKGREEN + f"Product '{product_id}' updated successfully!" + Colors.ENDC)

    def display_inventory(self):
        if not self.products:
            print(Colors.WARNING + "No products found." + Colors.ENDC)
        else:
            print(Colors.OKCYAN + "Current Inventory:" + Colors.ENDC)
            for product_id, product in self.products.items():
                print(f"{product_id}: {product['name']} - Price: {product['price']} - Quantity: {product['quantity']}")

    def sell_product(self, user, product_id, quantity):
        if product_id not in self.products:
            print(Colors.FAIL + "Product ID does not exist." + Colors.ENDC)
            return
        product = self.products[product_id]
        if product['quantity'] < int(quantity):
            print(Colors.FAIL + "Insufficient stock." + Colors.ENDC)
            return
        product['quantity'] -= int(quantity)
        self.save_products()
        self.record_history(user.username, product_id, 'sell', quantity)
        print(Colors.OKGREEN + f"Sold {quantity} of '{product['name']}'." + Colors.ENDC)

    def restock_product(self, user, product_id, quantity):
        if product_id not in self.products:
            print(Colors.FAIL + "Product ID does not exist." + Colors.ENDC)
            return
        product = self.products[product_id]
        product['quantity'] += int(quantity)
        self.save_products()
        self.record_history(user.username, product_id, 'restock', quantity)
        print(Colors.OKGREEN + f"Restocked {quantity} of '{product['name']}'." + Colors.ENDC)

    def search_product(self, user, search_term):
        results = [prod for prod in self.products.values() if search_term in prod['name'] or search_term in prod['product_id']]
        if results:
            print(Colors.OKCYAN + "Search Results:" + Colors.ENDC)
            for result in results:
                print(result)
        else:
            print(Colors.WARNING + "No products found matching that search." + Colors.ENDC)

    def view_history(self, user):
        if not self.history:
            print(Colors.WARNING + "No history found." + Colors.ENDC)
        else:
            print(Colors.OKCYAN + "History:" + Colors.ENDC)
            for record in self.history.get(user.username, []):
                print(record)

    def record_history(self, username, product_id, action, quantity):
        timestamp = datetime.datetime.now().isoformat()
        if username not in self.history:
            self.history[username] = []
        self.history[username].append({
            "timestamp": timestamp,
            "product_id": product_id,
            "action": action,
            "quantity": quantity
        })
        self.save_history()

    def delete_product(self, user, product_id):
        if product_id in self.products:
            del self.products[product_id]
            self.save_products()
            print(Colors.OKGREEN + f"Product '{product_id}' deleted." + Colors.ENDC)
        else:
            print(Colors.FAIL + "Product ID does not exist." + Colors.ENDC)
