from cli.product_cli import ProductCLI
from cli.inventory_cli import InventoryCLI

from database.init_db import create_table



def main():
    create_table()

    #CLI
    p_cli = ProductCLI()
    i_cli = InventoryCLI()

    while True:
        print("\n=== Main Menu ===")
        print("1. Product Management")
        print("2. Inventory Management")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            p_cli.product_menu()

        elif choice == "2":
            i_cli.inventory_menu()


        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
