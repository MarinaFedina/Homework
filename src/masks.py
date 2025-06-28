def get_mask_card_number(number: str) -> str:
    """Функция маскирует некоторые символы номера банковской карты
    :return: str"""
    masked_number = []
    for symbol in number:
        if not symbol.isdigit():
            continue
        else:
            masked_number.append(symbol)
    if len(masked_number) == 16:
        masked_number[6:-4] = "******"
        masked_number.insert(4, " ")
        masked_number.insert(9, " ")
        masked_number.insert(14, " ")
        return "".join(masked_number)
    else:
        return "-введите верный номер"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счёта
    :return: str"""
    if len(account_number) == 20 and account_number.isdigit():
        last_numbers = "".join(account_number[-4:])
        masked_account = "**" + last_numbers
        return masked_account
    else:
        return "-введите верный номер"


print(get_mask_card_number("1234567891234567"))
print(get_mask_account("12345678912345678978"))
