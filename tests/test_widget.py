import pytest
from src.widget import mask_account_card
from tests.conftest import num_empty


# Тест для проверки, что функция корректно распознает и применяет нужный тип маскировки
# в зависимости от типа входных данных.
@pytest.mark.parametrize("type_num, expected", [
    ("Maestro 1596837868705199", mask_account_card("Maestro 1596837868705199")),
    ("Счет 64686473678894779589", mask_account_card("Счет 64686473678894779589")),
    ("MasterCard 7158300734726758", mask_account_card("MasterCard 7158300734726758")),
    ("Счет 35383033474447895560", mask_account_card("Счет 35383033474447895560")),
    ("Visa Classic 6831982476737658", mask_account_card("Visa Classic 6831982476737658")),
    ("Visa Platinum 8990922113665229", mask_account_card("Visa Platinum 8990922113665229")),
    ("Visa Gold 5999414228426353", mask_account_card("Visa Gold 5999414228426353")),
    ("Счет 73654108430135874305", mask_account_card("Счет 73654108430135874305")),
    (" ", num_empty)
])
def mask_account_card(type_num, expected):
    assert mask_account_card(type_num) == expected



#Функция
#get_date:
#"2024-03-11T02:26:18.671407"
#"11.03.2024"
#Тестирование правильности преобразования даты.
#Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
#Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.