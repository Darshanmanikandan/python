from product import * 
from sales import * 

def seed_products(): 
    add_product(1, "Laptop", 50000, 5) 
    add_product(2, "Mouse", 500, 20) 
    add_product(3, "Phone", 20000, 10) 

seed_products() 
 
while True: 
    print("\n1. View Products\n2. Purchase\n3. Exit") 
    choice = input("Enter choice: ") 
 
    if choice == '1': 
        display_products() 
    elif choice == '2': 
        handle_purchase() 
    elif choice == '3': 
        print("Thank you for shopping!") 
        break 
    else: 
        print("Invalid option.") 