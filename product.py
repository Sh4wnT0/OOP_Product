class Product:
    price = 0.0
    quantity = 0
    inventory = []
    product_id = 0

    # Initializing the product objects
    def __init__(self, id, name, category, quantity, price, supplier):
        self.product_id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    # Methods for managing products
    def add_product(name, category, quantity, price, supplier):
        Product.product_id += 1
        new_product = Product(Product.product_id, name, category, quantity, price, supplier)
        Product.inventory.append(new_product)
        print("Product added successfully")

    def update_product(product_id, name=None, category=None, quantity=None, price=None, supplier=None):
        # Find the product by ID using a generator expression
        product = next((p for p in Product.inventory if p.product_id == product_id), None)
        if not product:
            print(f"Product with ID {product_id} not found.")
            return
        if name:
            product.name = name
        if category:
            product.category = category
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price
        if supplier:
            product.supplier = supplier
        print("Product information updated successfully.")

    #Extra method to display products
    def display_products():
        if not Product.inventory:
            print("No products in inventory.")
            return
        for product in Product.inventory:
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Quantity: {product.quantity}, Price: ${product.price}, Supplier: {product.supplier}")

    def delete_product(product_id):
        product = next((p for p in Product.inventory if p.product_id == product_id), None)
        if not product:
            print(f"Product with ID {product_id} not found.")
            return
        Product.inventory.remove(product)
        print("Product deleted successfully.")

class Order:
    def __init__(self, order_id, product_id, customer_info, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.customer_info = customer_info
        self.quantity = quantity

    def place_order(order_id, product_id, customer_info, quantity):
        product = next((p for p in Product.inventory if p.product_id == product_id), None)
        if not product:
            print(f"Product with ID {product_id} not found.")
            return
        if product.quantity < quantity:
            print(f"Insufficient stock for product ID {product_id}. Available: {product.quantity}, Requested: {quantity}")
            return
        product.quantity -= quantity
        new_order = Order(order_id, product_id, customer_info, quantity)
        print(f"Order placed successfully for {customer_info}. Order ID: {order_id}")
   


Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
Product.add_product("Smartphone", "Electronics", 100, 500, "Supplier B")
Product.display_products()

print("\nUpdated Info for product ID 2")
Product.update_product(2, price=950, quantity=45)
Product.display_products()

print("\nDeleting product ID 2")
Product.delete_product(2)
Product.display_products()

print("\nPlacing an order")
Order.place_order(1, 1, "Shawn", 2)
