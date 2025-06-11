def get_mask_card_number(number: str) -> str:
    """Функция маскирует некоторые символы номера банковской карты
    :return: str"""
    masked_number = []
    for symbol in number:
        masked_number.append(symbol)
    masked_number[6:-4] = "******"
    masked_number.insert(4, " ")
    masked_number.insert(9, " ")
    masked_number.insert(14, " ")
    return "".join(masked_number)


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счёта
    :return: str"""
    last_numbers = "".join(account_number[-4:])
    masked_account = "**" + last_numbers
    return masked_account


print(get_mask_account("7000792289606361"))
