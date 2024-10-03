import json
import numpy as np

PRODUCT_FILE = 'products.json'

def load_products():
    try:
        with open(PRODUCT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def display_products():
    products = load_products()
    if not products:
        print("No products available.")
        return
    
    product_list = [[pid, data['name'], data['price'], data['stock']] for pid, data in products.items()]
    
    np_products = np.array(product_list)
    print("\nProducts List:")
    print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Stock':<10}")
    for row in np_products:
        print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {row[3]:<10}")
