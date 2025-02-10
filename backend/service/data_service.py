from components.database import InventoryDB
import pandas as pd

inventory_db = InventoryDB()

def get_stats():
    items = inventory_db.get_all_items()
    df = pd.DataFrame(items)

    # Aggregate stock quantity per category (For Bar Chart)
    category_stock_data = df.groupby("category")["stock_quantity"].sum().reset_index().to_dict(orient="records")

    # Aggregate max and min price per category (For Bar Chart)
    category_price_data = df.groupby('category')['price'].agg(['max', 'min']).reset_index().to_dict(orient="records")

    # Aggregate total inventory value per category (For Pie Chart)
    df["inventory_value"] = df["stock_quantity"] * df["price"]
    value_data = df.groupby("category")["inventory_value"].sum().reset_index().to_dict(orient="records")

    # Insights
    max_stock_item = df.loc[df["stock_quantity"].idxmax(), ["item_name", "stock_quantity"]].to_dict()
    min_stock_item = df.loc[df["stock_quantity"].idxmin(), ["item_name", "stock_quantity"]].to_dict()
    max_price_item = df.loc[df["price"].idxmax(), ["item_name", "price"]].to_dict()
    min_price_item = df.loc[df["price"].idxmin(), ["item_name", "price"]].to_dict()

    return {
        "category_stock_data": category_stock_data,
        "category_price_data": category_price_data,
        "value_data": value_data,
        "insights": {
            "max_stock": max_stock_item,
            "min_stock": min_stock_item,
            "max_price": max_price_item,
            "min_price": min_price_item,
        },
    }

def get_inventory_categories():
    items = inventory_db.get_all_items()
    df = pd.DataFrame(items)
    categories = df["category"].unique()
    return categories.tolist()