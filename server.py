from fastapi import FastAPI, HTTPException
from database import SessionLocal, Order
from schemas import OrderResponse, StatusResponse
import random

statusList:list[str] = ["In transit", "Delivered", "Delayed","Pending"]

app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get('/get_order_details/{order_id}', response_model=OrderResponse)
def get_order_details(order_id: str):
    db = SessionLocal()
    try:  
      order = db.query(Order).filter(Order.order_id == order_id).first()
      if order is None:
         raise HTTPException(status_code=404, detail="Order not found")

      return order
    finally:
       db.close()

@app.get('/shipping_status', response_model=StatusResponse)
def get_shipping_status(tracking_number: str):
    status = random.choice(statusList)
    return {"shipping_status":status}
# return randoming shipping status to simulate a different shipping API that keeps track of status using tracking number 



'''
Notes: 
- Map HTTP Methods and Paths to Functions: They associate a specific HTTP method (like GET, POST, PUT, DELETE) and a URL path with a Python function. 
  When FastAPI receives a request matching that method and path, it executes the decorated function

'''