from cli.product_cli import ProductCLI
from cli.inventory_cli import InventoryCLI
from cli.order_cli import OrderCLI

from database.init_db import create_table



def main():
    create_table()

    #CLI
    product_cli = ProductCLI()
    inventory_cli = InventoryCLI()
    order_cli = OrderCLI()

    while True:
        print("\n=== Main Menu ===")
        print("1. Product Management")
        print("2. Inventory Management")
        print("3. Order Management")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            product_cli.product_menu()

        elif choice == "2":
            inventory_cli.inventory_menu()

        elif choice == "3":
            order_cli.order_menu()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
