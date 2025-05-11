products = {} 
def add_product(pid, name, price, qty): 
    products[pid] = {'name': name, 'price': price, 'quantity': qty} 
def display_products(): 
    print("\nAvailable Products:") 
    for pid, p in products.items(): 
        print(f"ID: {pid}, Name: {p['name']}, Price: ₹{p['price']}, Qty: {p['quantity']}")  
def update_product(pid, name=None, price=None, quantity=None): 
    if pid in products: 
        if name: products[pid]['name'] = name 
        if price: products[pid]['price'] = price 
        if quantity is not None: products[pid]['quantity'] = quantity 
    else: 
        print("Product not found.") 
def delete_product(pid): 
    if pid in products: 
        del products[pid] 
    else: 
        print("Product not found.") 