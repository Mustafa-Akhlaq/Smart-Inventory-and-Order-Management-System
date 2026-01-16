from services.inventory_service import InventoryService


class InventoryCLI:
    def __init__(self):
        self.service = InventoryService()

    def inventory_menu(self):
        while True:
            print("\n=== Inventory Menu ===")
            print("1. View Stock")
            print("2. Add Stock")
            print("3. Remove Stock")
            print("0. Back")

            choice = input("Choose option: ")

            try:
                if choice == "1":
                    product_id = int(input("Product ID: "))
                    stock = self.service.get_stock(product_id)
                    if stock:
                        print(f"Quantity: {stock.quantity}")
                    else:
                        print("No stock record found")

                elif choice == "2":
                    product_id = int(input("Product ID: "))
                    amount = int(input("Amount to add: "))
                    self.service.add_stock(product_id, amount)
                    print("Stock added successfully")

                elif choice == "3":
                    product_id = int(input("Product ID: "))
                    amount = int(input("Amount to remove: "))
                    self.service.remove_stock(product_id, amount)
                    print("Stock removed successfully")

                elif choice == "0":
                    break

                else:
                    print("Invalid option")

            except ValueError as e:
                print(f"Error: {e}")
