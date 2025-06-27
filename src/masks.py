def get_mask_card_number(number: str) -> str:
    """Функция маскирует некоторые символы номера банковской карты
    :return: str"""
    masked_number = []
    for symbol in number:
        if not symbol.isdigit():
            continue
        else:
            masked_number.append(symbol)
        masked_number[6:-4] = "******"
        masked_number.insert(4, " ")
        masked_number.insert(9, " ")
        masked_number.insert(14, " ")
    user_msg = "Введите номер"
    if len(masked_number) < 19:
        print(user_msg)
    else:
        return "".join(masked_number)


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счёта
    :return: str"""
    last_numbers = "".join(account_number[-4:])
    masked_account = "**" + last_numbers
    return masked_account


print(get_mask_card_number(""))