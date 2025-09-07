from fastapi import FastAPI, HTTPException
from database import SessionLocal, Order
from schemas import OrderResponse

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
      

    # Your function logic here
    # so inside this function I have to load and store mock_db.json, retrieve the correct order_id and then return it
    return {"message": f"Fetching details for order {order_id}"}

'''
Notes: 
- Map HTTP Methods and Paths to Functions: They associate a specific HTTP method (like GET, POST, PUT, DELETE) and a URL path with a Python function. 
  When FastAPI receives a request matching that method and path, it executes the decorated function

'''