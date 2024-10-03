# from AUTHENTICATION import signup, login
# from PRODUCTS import display_products
# from ADMIN import add_product, delete_product, update_product, delete_user

def main():
    print("Welcome to Inventory Management System")
    
    while True:
        print("\n1. Sign Up\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/user): ")
            print(signup(username, password, role))
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = login(username, password)
            if role:
                print(f"Welcome {username} ({role})")
                if role == 'admin':
                    while True:
                        print("\nAdmin Menu")
                        print("1. Add Product\n2. Delete Product\n3. Update Product\n4. Delete User\n5. View Products\n6. Logout")
                        admin_choice = input("Enter your choice: ")
                        if admin_choice == '1':
                            pid = input("Enter Product ID: ")
                            name = input("Enter Product Name: ")
                            price = input("Enter Product Price: ")
                            stock = input("Enter Stock Quantity: ")
                            print(add_product(pid, name, price, stock))
                        elif admin_choice == '2':
                            pid = input("Enter Product ID to delete: ")
                            print(delete_product(pid))
                        elif admin_choice == '3':
                            pid = input("Enter Product ID to update: ")
                            name = input("Enter new name (or leave blank): ")
                            price = input("Enter new price (or leave blank): ")
                            stock = input("Enter new stock (or leave blank): ")
                            print(update_product(pid, name, price, stock))
                        elif admin_choice == '4':
                            user = input("Enter username to delete: ")
                            print(delete_user(user))
                        elif admin_choice == '5':
                            display_products()
                        elif admin_choice == '6':
                            break
                        else:
                            print("Invalid choice!")
                else:
                    display_products()
            else:
                print("Invalid login credentials!")

        elif choice == '3':
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
