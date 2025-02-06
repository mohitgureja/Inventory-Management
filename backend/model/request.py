from pydantic import BaseModel

class UpdateStockQuantityRequest(BaseModel):
    item_id: int
    new_quantity: int

class UpdateStockPriceRequest(BaseModel):
    category: str
    new_price: float