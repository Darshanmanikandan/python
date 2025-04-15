product_list = []
def add_product(name, price, quantity):
    product = {"name": name, "price": price, "quantity": quantity}
    product_list.append(product)
    print(f"Product '{name}' added successfully!")

def display_products():
    if not product_list:
        print("No products available.")
    else:
        print("\nAvailable Products:")
        for idx, product in enumerate(product_list, start=1):
            print(f"{idx}. {product['name']} - ₹{product['price']} - Qty: {product['quantity']}")
