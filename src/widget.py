import src.masks


def mask_account_card(card_type_number: str) -> str:
    """Функция считывает тип номера - карта или счет, и маскирует номер в
    соответствии с типом"""
    card_type = []
    card_number = []
    for symbol in card_type_number:
        if symbol.isalpha():
            card_type.append(symbol)
        elif symbol.isdigit():
            card_number.append(symbol)
            if "".join(card_type) == "Счет":
                masked_number = src.masks.get_mask_account("".join(card_number))
            else:
                masked_number = src.masks.get_mask_card_number("".join(card_number))
    return f"{"".join(card_type)} {masked_number}"


def get_date(date: str) -> str:
    """Функция переделывает формат даты в стандартный"""
    clean_date = []
    for symbol in date:
        if symbol.isdigit():
            clean_date.append(symbol)
    year = "".join(clean_date[0:4])
    month = "".join(clean_date[4:6])
    day = "".join(clean_date[6:8])
    return f"{day}.{month}.{year}"


print(mask_account_card("Maestro 1596837868705199"))
print(get_date("2024-03-11T02:26:18.671407"))
