product_list = []
def add_product(name, price, quantity):  # add the product details as a dictionary and keeps within a list 
    product = {"name": name, "price": price, "quantity": quantity}  
    product_list.append(product)
    print(f"Product '{name}' added successfully!") 

def display_products():
    if not product_list: # check for a empty list 
        print("No products available.")
    else:
        print("\nAvailable Products:")
        for idx, product in enumerate(product_list, start=1):  #The enumerate is used to return the index of the product so it can be printed in the output screen 
            print(f"{idx}. {product['name']} - ₹{product['price']} - Qty: {product['quantity']}")
        