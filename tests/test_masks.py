import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


# Тестирование правильности маскирования номера карты.
def test_get_mask_card_number(card_num: str):
    assert get_mask_card_number(card_num) == "7000 79** **** 6361"
    assert get_mask_card_number(" ") == "Введите номер"
    assert get_mask_card_number("") == "Введите номер"
    assert get_mask_card_number("asdfghjklzxcvbnm") == "Введите номер"
    assert get_mask_card_number("162734") == "Введите номер"


# Тестирование правильности маскирования номера счёта.
def test_get_mask_account(account_num: str):
    assert get_mask_account(account_num) == "**4305"
    assert get_mask_account(" ") == "Введите номер"
    assert get_mask_account("") == "Введите номер"
    assert get_mask_account("lnjvjqyjvthzujdj") == "Введите номер"
    assert get_mask_account("67564") == "Введите номер"
