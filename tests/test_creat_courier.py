import allure
from helpers.api_client import (create_courier)
from helpers.generator import (
    generate_login,
    generate_password,
    generate_first_name
)


@allure.title('Создание курьера')
def test_create_courier_trye():
    payload = {
        'login' : generate_login(),
        'password' : generate_password(),
        'first_name' : generate_first_name()
    }

    response = create_courier(payload)

    assert response.status_code == 201
    assert response.json() == {'ok' : True}

@allure.title('Нельзя создать двух одинаковых курьеров')
def test_create_dubl_courier_fail():
    login = generate_login
    password = generate_password
    first_name = generate_first_name
    payload = {'login' : login, 'password' : password, 'first_name' : first_name}

    create_courier(payload)
    response = create_courier(payload)

    assert response.status_code == 409
    assert 'Этот логин уже используется' in response.text

@allure.title('Нельзя создать курьера без логина')
def test_cteate_courier_not_login():
    payload = {
        'password' : generate_password(),
        'first_name' : generate_first_name()
    }
    
    response = create_courier(payload)

    assert response.status_code == 400
    assert 'Недостаточно данных для создания учетной записи' in response.text

@allure.title('Нельзя создать курьера без пароля')
def test_cteate_courier_not_pass():
    payload = {
        'login' : generate_login(),
        'first_name' : generate_first_name()
    }
    
    response = create_courier(payload)

    assert response.status_code == 400
    assert 'Недостаточно данных для создания учетной записи' in response.text
    