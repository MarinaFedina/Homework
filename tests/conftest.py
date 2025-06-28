import pytest


# Для тестов создаются фикстуры, которые предоставят тестовые данные.
@pytest.fixture
def card_num():
    return "7000792289606361"


@pytest.fixture
def account_num():
    return "73654108430135874305"
