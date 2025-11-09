from faker import Faker

fake_ru = Faker('ru_RU')
fake_en = Faker('en_US')

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

# Генерирует логин
def generate_login():
    return fake_en.user_name() + str(fake_en.random_number(digits = 4))

# Генерирует пароль
def generate_password():
    return fake_en.password(
        length = 10, # Количество символов
        special_chars = False, # Без спец символов
        digits = True, # С цифрами
        upper_case = False # Без заглавных
    )

# Генерирует имя
def generate_first_name():
    return fake_ru.first_name()

# Генерирует фамилию
def generate_last_name():
    return fake_ru.last_name()

# Генерирует адрес
def generate_address():
    return fake_ru.street_address()

# Генерирует станцию метро
def generate_metro_st():
    return fake_ru.random_int(min = 1, max = 100)

# Генерирует номер тел.
def generate_phone_num():
    return fake_ru.phone_number()

# Генерирует срок аренды
def generate_rent_time():
    return fake_ru.random_int(min = 1, max = 10)

# Генерирует дату доставки
def generate_delivery_date():
    return str(fake_ru.future_date(end_date = '+31d'))

# Генерирует комменарий
def generate_comment():
    return fake_ru.text(50)
