import allure
from helpers.generator import (
    generate_login,
    generate_password,
    generate_first_name
)
from helpers.api_client import (
    create_courier,
    login_courier
)


@allure.title('Автомризация курьера')
def test_login_true():
    login = generate_login
    password = generate_password
    first_name = generate_first_name

    create_courier({'login' : login, 'password' : password, 'first_name' : first_name})
    response = login_courier({'login' : login, 'password' : password})

    assert response.status_code == 200
    assert 'id' in response.json()

@allure.title('Ошибка при неверном пароле')
def test_login_fail_pass():
    login = generate_login()
    password = generate_password()
    first_name = generate_first_name()

    create_courier({'login' : login, 'password' : password, 'first_name' : first_name})
    response = login_courier({'login' : login, 'password' : 'qwerty'})

    assert response.status_code == 404
    assert 'Учетная запись не найдена' in response.text

@allure.title('Ошибка при отсутствии логина')
def test_login_without():
    response = login_courier({'password' : '123'})

    assert response.status_code == 400
    assert 'Недостаточно данных для входа' in response.text

@allure.title('Ошибка авторизации несуществующего пользователя')
def test_login_nonexistent():
    response = login_courier({'login' : 'qwerty', 'password' : '123456'})

    assert response.status_code == 404
