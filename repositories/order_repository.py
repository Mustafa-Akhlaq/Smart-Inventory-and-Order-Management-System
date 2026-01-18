from database.db_connection import get_connection
from models.order import Order
from models.order_item import OrderItem
from datetime import datetime

class OrderRepository:

    # -------------------------------
    # Create Order (returns order_id)
    # -------------------------------
    def create_order(self, total_amount: float):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO orders (created_at, total_amount)
            VALUES (?, ?)
            """,
            (datetime.now().isoformat(), total_amount)
        )

        conn.commit()
        order_id = cursor.lastrowid
        conn.close()

        return order_id

    # -------------------------------
    # Add Order Item
    # -------------------------------
    def add_order_item(self, order_id: int, product_id: int, quantity: int, price: float):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (?, ?, ?, ?)
            """,
            (order_id, product_id, quantity, price)
        )

        conn.commit()
        conn.close()

    # -------------------------------
    # Get Order by ID
    # -------------------------------
    def get_order_by_id(self, order_id):
        conn = get_connection()
        cursor = conn.cursor()

        # Get order
        cursor.execute(
            "SELECT id, created_at, total_amount FROM orders WHERE id = ?",
            (order_id,)
        )
        order = cursor.fetchone()

        if not order:
            conn.close()
            return None

        # Get order items
        cursor.execute("""
            SELECT oi.product_id, p.name, oi.quantity, oi.price
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            WHERE oi.order_id = ?
        """, (order_id,))

        items = cursor.fetchall()
        conn.close()

        return {
            "order": order,
            "items": items
        }



    # -------------------------------
    # Get Order Items
    # -------------------------------
    def get_order_items(self, order_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, order_id, product_id, quantity, price
            FROM order_items
            WHERE order_id = ?
            """,
            (order_id,)
        )

        rows = cursor.fetchall()
        conn.close()

        return [OrderItem(*row) for row in rows]

    # -------------------------------
    # List All Orders
    # -------------------------------
    def get_all_orders(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, created_at, total_amount
            FROM orders
            ORDER BY id DESC
        """)
        orders = cursor.fetchall()

        conn.close()
        return orders
