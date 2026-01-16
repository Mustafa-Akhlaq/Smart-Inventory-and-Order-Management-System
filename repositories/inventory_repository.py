from models.inventory import Inventory
from database.db_connection import get_connection


class InventoryRepository:

    def create_stock(self, product_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO inventory (product_id, quantity)
            VALUES (?, 0)
            """,
            (product_id,)  
        )

        conn.commit()
        conn.close()

    def get_by_product_id(self, product_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT product_id, quantity
            FROM inventory
            WHERE product_id = ?
            """,
            (product_id,)
        )

        row = cursor.fetchone()
        conn.close()

        return Inventory(*row) if row else None
    
    def update_quantity(self, product_id: int, quantity: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE inventory
            SET quantity = ?
            WHERE product_id = ?
            """,
            (quantity, product_id)
        )

        conn.commit()
        conn.close()
