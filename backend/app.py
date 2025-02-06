import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.request import UpdateStockPriceRequest, UpdateStockQuantityRequest
from components.database import InventoryDB


app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allows all headers
)

inventory_db = InventoryDB()

@app.get("/")
async def root():
    return {"Welcome to statworx interview for Mohit Gureja!"}


@app.get("/items")
def get_all_items():
    return {"items": inventory_db.get_all_items()}


@app.put("/update_stock_quantity")
def update_stock_quantity(request: UpdateStockQuantityRequest):
    inventory_db.update_item(request.item_id, "stock_quantity", request.new_quantity)
    return {"message": "Stock quantity updated successfully"}


@app.put("/update_stock_price_by_category")
def update_stock_price_by_category(request: UpdateStockPriceRequest):
    inventory_db.update_stock_price_by_category(request.category, request.new_price)
    return {"message": "Stock price updated successfully"}


@app.get("/inventory_stats")
def get_inventory_stats():
    return inventory_db.get_inventory_stats()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
