import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv("DATABASE_PATH")
print(db_path)


class InventoryDB:

    def __init__(self):
        self.db_path = db_path

    def create_connection(self):
        self.conn = sqlite3.connect(db_path)

    def get_all_items(self):
        """
        Fetches all items from the database.
        :return: list of items
        """
        self.create_connection()
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM items')
        items = cursor.fetchall()
        self.conn.close()
        return items

    def get_item(self, item_id):
        """
        Fetches a single item from the database.
        :param item_id: ID of the item
        :return: A representation of the item
        """
        self.create_connection()
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM items WHERE id=?', (item_id,))
        item = cursor.fetchone()
        self.conn.close()
        return item

    def update_item(self, item_id, column, new_data):
        """
        Updates a single item in the database.
        :param item_id: Item ID to be updated
        :param column: Column to be updated
        :param new_data: New value to be updated
        :return: Id of the updated item
        """
        valid_columns = {"stock_quantity", "price", "name"}  # Add valid column names here

        if column not in valid_columns:
            raise ValueError("Invalid column name")

        self.create_connection()
        cursor = self.conn.cursor()
        query = f"UPDATE items SET {column} = ? WHERE item_id = ?"
        cursor.execute(query, (new_data, item_id))
        self.conn.commit()
        self.conn.close()

    def update_stock_price_by_category(self, category, new_price):
        """
        Update the stock price for all items in a specific category.
        :param category: Category to be updated
        :param new_price: New price to be updated
        """
        self.create_connection()
        cursor = self.conn.cursor()
        cursor.execute("UPDATE items SET price = ? WHERE category = ?", (new_price, category))
        self.conn.commit()
        self.conn.close()
