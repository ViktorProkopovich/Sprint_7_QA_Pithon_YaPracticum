import requests
from Urls import BASE_URL


def create_courier(payload):
    return requests.post(f'{BASE_URL}/courier', data = payload)

def login_courier(payload):
    return requests.post(f'{BASE_URL}/courier/login', data = payload)

def create_order(payload):
    return requests.post(f'{BASE_URL}/orders', json = payload)

def get_orders():
    return requests.get(f'{BASE_URL}/orders')
