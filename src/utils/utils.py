import re


def is_valid_phone(phone: str) -> bool:
    pattern = r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
    if re.match(pattern, phone):
        return True
    return False
