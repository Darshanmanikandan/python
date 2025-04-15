from product_details.entry_display import product_list

def update_product(name, new_name=None, new_price=None, new_quantity=None): # update the product details 
    for product in product_list:
        if product["name"].lower() == name.lower():
            if new_name: product["name"] = new_name
            if new_price: product["price"] = new_price
            if new_quantity: product["quantity"] = new_quantity
            print(f"Product '{name}' updated successfully.")
            return
    print(f"Product '{name}' not found.")

def delete_product(name):  # delete the product using the name of the product 
    for product in product_list:
        if product["name"].lower() == name.lower():
            product_list.remove(product)
            print(f"Product '{name}' deleted successfully.")
            return
    print(f"Product '{name}' not found.")
