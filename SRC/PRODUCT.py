class Product:
    def __init__(self, product_id, name, price, quantity, added_by):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.added_by = added_by

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "added_by": self.added_by
        }

    def __repr__(self):
        return f"{self.name} (ID: {self.product_id}) - Price: {self.price}, Stock: {self.quantity}"
