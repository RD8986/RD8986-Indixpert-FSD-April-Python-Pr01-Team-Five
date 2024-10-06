from SRC.AUTHENTICATION_SYSTEM import AuthenticationSystem
from SRC.INVENTORY_MANAGEMENT_SYSTEM import InventoryManagementSystem
from SRC.ADMIN_SYSTEM import AdminSystem
from SRC.COLORS import Colors


def display_menu(current_user=None):
    if current_user is None:
        print(Colors.HEADER + "=== Welcome to the Inventory Management System ===" + Colors.ENDC)
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
    else:
        print(Colors.HEADER + f"=== Welcome, {current_user.first_name} ===" + Colors.ENDC)
        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Inventory")
        print("4. Sell Product")
        print("5. Restock Product")
        print("6. Search Product")
        print("7. View History")
        if current_user.role == 'Admin':
            print("8. Delete Product")
            print("9. Delete User")
            print("10. Replace Admin")
            print("11. View Error Logs")
        print("12. Logout")

def main():
    auth_system = AuthenticationSystem()
    inventory_system = InventoryManagementSystem()
    admin_system = AdminSystem(auth_system)
    current_user = None

    while True:
        if current_user is None:
            display_menu()
            choice = input("Please Choose Any Option: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = auth_system.login(username, password)

            elif choice == '2':
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                username = input("Enter username: ")
                password = input("Enter password (min 7 characters): ")
                role = input("Enter role (User/Admin): ").capitalize()
                auth_system.signup(first_name, last_name, username, password, role)

            elif choice == '3':
                print("Exiting the system.")
                break

            else:
                print(Colors.FAIL + "Invalid choice. Please try again." + Colors.ENDC)
        else:
            display_menu(current_user)
            choice = input("Please Choose Any Option: ")

            if choice == '1':
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = input("Enter product price: ")
                quantity = input("Enter product quantity: ")
                inventory_system.add_product(current_user, product_id, name, price, quantity)

            elif choice == '2':
                product_id = input("Enter product ID: ")
                name = input("Enter new product name (leave blank to skip): ")
                price = input("Enter new product price (leave blank to skip): ")
                quantity = input("Enter new product quantity (leave blank to skip): ")
                inventory_system.update_product(current_user, product_id, name or None, price or None, quantity or None)

            elif choice == '3':
                inventory_system.display_inventory()

            elif choice == '4':
                product_id = input("Enter product ID to sell: ")
                quantity = input("Enter quantity to sell: ")
                inventory_system.sell_product(current_user, product_id, quantity)

            elif choice == '5':
                product_id = input("Enter product ID to restock: ")
                quantity = input("Enter quantity to restock: ")
                inventory_system.restock_product(current_user, product_id, quantity)

            elif choice == '6':
                search_term = input("Enter product ID or name to search: ")
                inventory_system.search_product(current_user, search_term)

            elif choice == '7':
                inventory_system.view_history(current_user)

            elif choice == '8' and current_user.role == 'Admin':
                product_id = input("Enter product ID to delete: ")
                inventory_system.delete_product(current_user, product_id)

            elif choice == '9' and current_user.role == 'Admin':
                username = input("Enter username to delete: ")
                admin_system.delete_user(current_user, username)

            elif choice == '10' and current_user.role == 'Admin':
                new_username = input("Enter new admin username: ")
                admin_system.replace_admin(current_user, new_username)

            elif choice == '11' and current_user.role == 'Admin':
                admin_system.view_error_logs()

            elif choice == '12':
                current_user = None

            else:
                print(Colors.FAIL + "Invalid choice. Please try again." + Colors.ENDC)

if __name__ == "__main__":
    main()
