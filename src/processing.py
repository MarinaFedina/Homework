def filter_by_state(set_of_lists:list[dict], state: str ="EXECUTED") -> list:
    """Функция принимает на вход список словарей и возвращает новый список словарей,
    содержащий только те словари, которые соответствуют указанному значению."""
    new_list = []
    for one_list in set_of_lists:
        for key, value in one_list.items():
            if key == "state" and value == "EXECUTED":
                new_list.append(one_list)
    return new_list


test_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def sort_by_date(set_of_lists: list[dict], reverse: bool=True) -> list[dict]:
        """Функция принимает на вход список словарей и возвращает новый список словарей,
        который отсортирован по дате."""
        new_list = sorted(set_of_lists, key=lambda p: p["date"], reverse=True)
        return new_list


print(filter_by_state(test_list))
print(sort_by_date(test_list))