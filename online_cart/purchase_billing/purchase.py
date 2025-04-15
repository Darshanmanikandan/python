from product_details.entry_display import display_products, product_list
def start_purchase():
    cart = []
    total = 0 

    display_products() # display the available products 

    while True:
        choice = input("\nEnter product name to buy (or 'done' to finish): ").strip()  # .strip() is a string method that removes any leading or trailing whitespace
        # input validation
        if choice.lower() == 'done':
            break
        for product in product_list:
            if product["name"].lower() == choice.lower():
                qty = int(input(f"Enter quantity for {choice}: "))
                if qty <= product["quantity"]:
                    item_total = product["price"] * qty
                    cart.append({"name": product["name"], "price": product["price"], "quantity": qty, "total": item_total})
                    total += item_total
                    product["quantity"] -= qty
                else:
                    print("Not enough stock.")
                break
        else:
            print("Product not found.")
    if not cart: # check for an empty cart 
        print("No items purchased.")
        return
    print("\n----- BILL -----")
    for item in cart:
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item['total']}")  # prints the items 
    print(f"\nSubtotal: ₹{total}")
#calculate discount 
    discount = 0
    if total > 1000:
        discount = total * 0.10
        print(f"Discount (10%): -₹{discount}")
#tax calculation 
    taxed_amount = (total - discount) * 1.18
    tax = taxed_amount - (total - discount)
    print(f"Tax (18%): ₹{round(tax, 2)}")
    print(f"Final Amount to Pay: ₹{round(taxed_amount, 2)}")
