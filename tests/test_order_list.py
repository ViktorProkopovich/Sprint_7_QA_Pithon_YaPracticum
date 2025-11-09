import allure
from helpers.api_client import get_orders


allure.title('Возвращение списка заказов')
def test_get_orders_list():
    response = get_orders()
    assert response.status_code == 200
    data = response.json()
    assert 'orders' in data
    assert isinstance(data['orders'], list)