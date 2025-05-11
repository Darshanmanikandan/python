from product import * 

def handle_purchase(): 
    display_products() 
    cart = [] 
    total = 0 
 
    while True: 
        try: 
            pid = int(input("Enter Product ID (0 to finish): ")) 
            if pid == 0: 
                break 
            if pid not in products: 
                print("Invalid ID") 
                continue 
 
            qty = int(input("Enter Quantity: ")) 
            if qty > products[pid]['quantity']: 
                print("Not enough stock") 
                continue 
 
            cost = qty * products[pid]['price'] 
            cart.append((products[pid]['name'], qty, cost)) 
            total += cost 
 
            update_product(pid, quantity=products[pid]['quantity'] - qty) 
 
        except: 
            print("Invalid input") 
 
    discount = 0.1 * total if total > 1000 else 0 
    subtotal = total - discount 
    tax = subtotal * 0.18 
    final = subtotal + tax 
 
    print("\n------ BILL ------") 
    for name, qty, cost in cart: 
        print(f"{name} x {qty} = ₹{cost}") 
    print(f"Total: ₹{total}") 
    print(f"Discount: ₹{discount}") 
    print(f"Tax (18%): ₹{tax:.2f}") 
    print(f"Final Amount: ₹{final:.2f}") 