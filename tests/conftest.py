import pytest

#Фикстуры.
@pytest.fixture
def card_num():
    return "7000792289606361"


@pytest.fixture
def account_num():
    return "73654108430135874305"


@pytest.fixture
def num_empty():
    return " "


@pytest.fixture
def msg_to_user():
    return "Введите номер"

#Для всех тестов создайте фикстуры, которые предоставят тестовые данные
# для списков словарей, включая различные случаи и комбинации state и date.
#Покрытие тестами. Убедитесь, что все ветви кода и исключения,
# которые могут быть сгенерированы вашими функциями, тестируются.