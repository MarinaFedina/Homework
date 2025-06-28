import pytest
from src.widget import mask_account_card
from src.widget import get_date


# Тест для проверки, что функция корректно распознает и применяет нужный
# тип маскировки в зависимости от типа входных данных.
@pytest.mark.parametrize(
    "type_num, expected",
    [
        ("Maestro 1596837868705199", mask_account_card("Maestro 1596837868705199")),
        ("Счет 64686473678894779589", mask_account_card("Счет 64686473678894779589")),
        ("MasterCard 7158300734726758", mask_account_card("MasterCard 7158300734726758")),
        ("Счет 35383033474447895560", mask_account_card("Счет 35383033474447895560")),
        ("Visa Classic 6831982476737658", mask_account_card("Visa Classic 6831982476737658")),
        ("Visa Platinum 8990922113665229", mask_account_card("Visa Platinum 8990922113665229")),
        ("Visa Gold 5999414228426353", mask_account_card("Visa Gold 5999414228426353")),
        ("Счет 73654108430135874305", mask_account_card("Счет 73654108430135874305")),
    ],
)
def test_mask_account_card(type_num: str, expected: str):
    assert mask_account_card(type_num) == expected
    assert mask_account_card("Visa 12345678912345678912") == "Visa -введите верный номер"
    assert mask_account_card("Счет 5678912345678912") == "Счет -введите верный номер"
    assert mask_account_card("Visa Gold") == "Неверный формат номера"
    assert mask_account_card("2345678475636453") == "Неверный формат номера"
    assert mask_account_card("56473827465839564756") == "Неверный формат номера"
    assert mask_account_card("1234") == "Неверный формат номера"
    assert mask_account_card("Счет") == "Неверный формат номера"
    assert mask_account_card("") == "Неверный формат номера"
    assert mask_account_card(" ") == "Неверный формат номера"


# Тестирование правильности преобразования даты.
@pytest.mark.parametrize(
    "original_date, new_date",
    [
        ("2023-03-11T02:26:18.671407", "11.03.2023"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2020-10-14T08:21:33.419441", "14.10.2020"),
        ("2022-09-12T21:27:25.241689", "12.09.2022"),
        ("2021-06-30T02:08:58.425572", "30.06.2021"),
    ],
)
def test_get_date(original_date: str, new_date: str):
    assert get_date(original_date) == new_date
    assert get_date("") == "Введите дату в нужном формате"
    assert get_date(" ") == "Введите дату в нужном формате"
    assert get_date("17082025") == "Введите дату в нужном формате"
    assert get_date("17august1989") == "Введите дату в нужном формате"
    assert get_date("2021-06-30T02:08:58") == "Введите дату в нужном формате"
