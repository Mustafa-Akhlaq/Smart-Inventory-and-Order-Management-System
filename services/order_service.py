from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.inventory_repository import InventoryRepository
from database.db_connection import get_connection

class OrderService:
    def __init__(self):
        self.order_repo = OrderRepository()
        self.product_repo = ProductRepository()
        self.inventory_repo = InventoryRepository()

    # ------------------------------------
    # Create Order
    # items = [
    #   {"product_id": 1, "quantity": 2},
    #   {"product_id": 3, "quantity": 1}
    # ]
    # ------------------------------------
    def create_order(self, items: list):
        if not items:
            raise ValueError("Order must contain at least one item")

        conn = get_connection()

        try:
            cursor = conn.cursor()
            total_amount = 0
            stock_updates = []

            # 1️⃣ Validate products & stock
            for item in items:
                product_id = item["product_id"]
                quantity = item["quantity"]

                if quantity <= 0:
                    raise ValueError("Quantity must be positive")

                product = self.product_repo.get_product_by_id(product_id)
                if not product:
                    raise ValueError(f"Product ID {product_id} not found")

                stock = self.inventory_repo.get_by_product_id(product_id)
                if not stock or stock.quantity < quantity:
                    raise ValueError(f"Insufficient stock for product ID {product_id}")

                total_amount += product.price * quantity
                stock_updates.append((product_id, stock.quantity - quantity))

            # 2️⃣ Create order
            cursor.execute(
                """
                INSERT INTO orders (created_at, total_amount)
                VALUES (datetime('now'), ?)
                """,
                (total_amount,)
            )
            order_id = cursor.lastrowid

            # 3️⃣ Create order items
            for item in items:
                product = self.product_repo.get_product_by_id(item["product_id"])

                cursor.execute(
                    """
                    INSERT INTO order_items (order_id, product_id, quantity, price)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        order_id,
                        product.id,
                        item["quantity"],
                        product.price
                    )
                )

            # 4️⃣ Deduct inventory
            for product_id, new_qty in stock_updates:
                cursor.execute(
                    """
                    UPDATE inventory
                    SET quantity = ?
                    WHERE product_id = ?
                    """,
                    (new_qty, product_id)
                )

            conn.commit()
            return order_id

        except Exception as e:
            conn.rollback()
            raise e

        finally:
            conn.close()

    # ------------------------------------
    # View Order
    # ------------------------------------
    def get_order(self, order_id: int):
        order = self.order_repo.get_order_by_id(order_id)
        if not order:
            raise ValueError("Order not found")

        items = self.order_repo.get_order_items(order_id)
        return order, items

    # ------------------------------------
    # List Orders
    # ------------------------------------
    def get_all_orders(self):
        return self.order_repo.get_all_orders()


    # ------------------------------------
    # Cancel Order
    # ------------------------------------


    def cancel_order(self, order_id: int):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            # 1️⃣ Check order
            cursor.execute(
                "SELECT status FROM orders WHERE id = ?",
                (order_id,)
            )
            row = cursor.fetchone()

            if not row:
                raise ValueError("Order not found")

            if row[0] == "CANCELLED":
                raise ValueError("Order already cancelled")

            # 2️⃣ Fetch order items
            cursor.execute(
                """
                SELECT product_id, quantity
                FROM order_items
                WHERE order_id = ?
                """,
                (order_id,)
            )
            items = cursor.fetchall()

            # 3️⃣ Restore inventory
            for product_id, quantity in items:
                cursor.execute(
                    """
                    UPDATE inventory
                    SET quantity = quantity + ?
                    WHERE product_id = ?
                    """,
                    (quantity, product_id)
                )

            # 4️⃣ Mark order as cancelled
            cursor.execute(
                """
                UPDATE orders
                SET status = 'CANCELLED'
                WHERE id = ?
                """,
                (order_id,)
            )

            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            raise e

        finally:
            conn.close()

    def get_order_by_id(self, order_id):
        return self.order_repo.get_order_by_id(order_id)
