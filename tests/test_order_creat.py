
import requests
import pytest
import allure
from Urls import BASE_URL
from helpers.generator import (
    generate_first_name,
    generate_last_name,
    generate_address,
    generate_metro_st,
    generate_phone_num,
    generate_rent_time,
    generate_delivery_date,
    generate_comment
)


@allure.title('Создание заказа с разными цветами')
@pytest.mark.parametrize('color',[ 
                         ['BLACK'],
                         ['GREY'],
                         ['BLACK', 'GREY'],
                         []
                         ])

def test_create_order_with_color(color):
    payload = {
        'first_name' : generate_first_name(),
        'last_name' : generate_last_name(),
        'address' : generate_address(),
        'metroSt' : generate_metro_st(),
        'phone' :  generate_phone_num(),
        'rentTime' : generate_rent_time(),
        'deliveryDate' : generate_delivery_date(),
        'comment' : generate_comment(),
        'color' : color
    }

    response = requests.post(f'{BASE_URL}/orders', json = payload)

    assert response.status_code == 201
    assert 'track' in response.json()
