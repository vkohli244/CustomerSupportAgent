from pydantic import BaseModel



class OrderResponse(BaseModel):
    order_id: str
    customer_email: str
    products: list[dict]
    tracking_number: str
    shipping_status: str

