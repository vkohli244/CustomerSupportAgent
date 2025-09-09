import requests
import json


def get_order_details(order_id:str):
    response =  requests.get(f"http://localhost:8000/get_order_details/{order_id}")

    if response.status_code  == 200:
        return response.json()
    else:
        return None
    

def get_shipping_status(tracking_number:str):
    response = requests.get(f"http://localhost:8000/shipping_status?tracking_number={tracking_number}")
    if response.status_code  == 200:
        return response.json()
    else:
        return None
    
