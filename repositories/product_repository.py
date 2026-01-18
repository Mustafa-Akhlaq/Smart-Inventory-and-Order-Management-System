import sqlite3
from database.db_connection import get_connection
from models.product import Product


class ProductRepository:

    def add_product(self, product):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO products (name , category , price) 
            VALUES (?, ?, ?)
            """,
            (
                product.name,
                product.category,
                product.price,
            )
        )

        conn.commit()
        product_id = cursor.lastrowid
        conn.close()
        return product_id

    def get_all_products(self):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()

        return [
            Product(
                id=row["id"],
                name=row["name"],
                category=row["category"],
                price=row["price"]
            )   
            for row in rows
        ]



    def get_product_by_id(self, product_id):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Product(
                id=row["id"],
                name=row["name"],
                category=row["category"],
                price=row["price"]
            )
        return None
    
    def get_product_by_name(self, name):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Product(
                id=row["id"],
                name=row["name"],
                category=row["category"],
                price=row["price"]
            )
        return None


    def update_product(self, product_id, name , price):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE products SET name = ? , price = ? WHERE id = ?",
            (name, price , product_id)
        )

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        return updated > 0

    def delete_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM products WHERE id = ?",
            (product_id,)
        )

        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        return deleted > 0
