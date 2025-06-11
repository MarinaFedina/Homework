def get_date(date:str):
    clean_date = []
    for symbol in date:
        if symbol.isdigit():
            clean_date.append(symbol)
    year = "".join(clean_date[0:4])
    month = "".join(clean_date[4:6])
    day = "".join(clean_date[6:8])
    return f"{day}.{month}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))