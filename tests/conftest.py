import pytest


#Для тестов создаются фикстуры, которые предоставят тестовые данные.
@pytest.fixture
def card_num():
    return "7000792289606361"


@pytest.fixture
def account_num():
    return "73654108430135874305"


@pytest.fixture
def state_executed_1():
    return {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}


@pytest.fixture
def state_executed_2():
    return {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}


@pytest.fixture
def num_empty():
    return " "


@pytest.fixture
def msg_to_user():
    return "Введите номер"

# для списков словарей, включая различные случаи и комбинации state и date.
#Покрытие тестами. Убедитесь, что все ветви кода и исключения,
# которые могут быть сгенерированы вашими функциями, тестируются.