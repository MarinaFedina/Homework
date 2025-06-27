import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date


#Тестирование фильтрации списка словарей по заданному статусу state.
@pytest.mark.parametrize("original_list, new_list", [(
    [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
    [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]
)])
def filter_by_state(original_list, new_list):
    assert filter_by_state(original_list) == new_list
#Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
#Параметризация тестов для различных возможных значений статуса state.


# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
@pytest.mark.parametrize("not_sorted_list, sorted_list", [(
    [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2017-10-14T08:21:33.419441"}],
    [{"id": 615064591, "state": "CANCELED", "date": "2017-10-14T08:21:33.419441"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]
)])
def sort_by_date(not_sorted_list, sorted_list):
    assert sort_by_date(not_sorted_list) == sorted_list
#Проверка корректности сортировки при одинаковых датах.
#Тесты на работу функции с некорректными или нестандартными форматами дат.