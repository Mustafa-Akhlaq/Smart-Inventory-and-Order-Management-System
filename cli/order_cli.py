from services.order_service import OrderService

class OrderCLI:
    def __init__(self):
        self.service = OrderService()

    def order_menu(self):
        while True:
            print("\n===== Order Menu =====")
            print("1. Place Order")
            print("2. View Order by ID")
            print("3. View All Orders")
            print("4. Cancel Order")
            print("0. Back")

            choice = input("Enter choice: ")

            if choice == "1":
                self.place_order()
            elif choice == "2":
                self.view_order_by_id()
            elif choice == "3":
                self.view_all_orders()
            elif choice == "4":
                self.cancel_order()
            elif choice == "0":
                break
            else:
                print("Invalid choice")

    # -------------------------
    # PLACE ORDER
    # -------------------------
    def place_order(self):
        items = []
        print("\nEnter order items (type 0 to finish)")

        while True:
            product_id = int(input("Product ID (0 to finish): "))
            if product_id == 0:
                break

            quantity = int(input("Quantity: "))
            items.append({
                "product_id": product_id,
                "quantity": quantity
            })

        if not items:
            print("No items added.")
            return

        try:
            order_id = self.service.create_order(items)
            print(f"Order placed successfully! Order ID: {order_id}")
        except Exception as e:
            print("Error placing order:", e)

    # -------------------------
    # VIEW ORDER BY ID
    # -------------------------
    def view_order_by_id(self):
        order_id = int(input("Enter Order ID: "))
        result = self.service.get_order_by_id(order_id)

        if not result:
            print("Order not found")
            return

        order = result["order"]
        items = result["items"]

        print("\nOrder ID:", order[0])
        print("Created At:", order[1])
        print("Total Amount:", order[2])
        print("\nItems:")
        print("Product | Quantity | Price")

        for item in items:
            print(f"{item[1]} | {item[2]} | {item[3]}")

    # -------------------------
    # VIEW ALL ORDERS
    # -------------------------
    def view_all_orders(self):
        orders = self.service.get_all_orders()

        if not orders:
            print("No orders found.")
            return

        print("\nID | Created At | Total Amount")
        print("----------------------------------")

        for order in orders:
            print(f"{order[0]} | {order[1]} | {order[2]}")


    # -------------------------
    # CANCEL ORDER
    # -------------------------
    def cancel_order(self):
        order_id = int(input("Enter Order ID to cancel: "))

        try:
            self.service.cancel_order(order_id)
            print("Order cancelled successfully.")
        except Exception as e:
            print("Error cancelling order:", e)
