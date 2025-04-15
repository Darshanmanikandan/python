from product_details.entry_display import add_product, display_products
from product_details.update_delete import update_product, delete_product
from purchase_billing.purchase import start_purchase

def menu():
    while True:
        print("\n--- Online Cart Menu ---")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Start Purchase")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            qty = int(input("Enter quantity: "))
            add_product(name, price, qty)
        elif choice == '2':
            display_products()
        elif choice == '3':
            name = input("Enter product name to update: ")
            new_name = input("New name (or press Enter to skip): ") or None
            new_price = input("New price (or press Enter to skip): ")
            new_qty = input("New quantity (or press Enter to skip): ")
            update_product(
                name,
                new_name=new_name,
                new_price=float(new_price) if new_price else None,
                new_quantity=int(new_qty) if new_qty else None
            )
        elif choice == '4':
            name = input("Enter product name to delete: ")
            delete_product(name)
        elif choice == '5':
            start_purchase()
        elif choice == '6':
            print("Thank you for using Online Cart!")
            break
        else:
            print("Invalid choice! Please try again.")
            
if __name__ == "__main__":
    menu()
