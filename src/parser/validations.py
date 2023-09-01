import re
from src.parser.consts import VALIDATION_DICT, MONTH_DICT, WEEK_DICT


def field_name_validation(field_name: str) -> None:
    valid_field_names = list(VALIDATION_DICT.keys())
    if field_name not in VALIDATION_DICT:
        raise ValueError(f"Invalid field {field_name} fields should be in the following: {valid_field_names}.")


def special_char_validation(field_name: str, field_value: str) -> None:
    allowed_specials = VALIDATION_DICT[field_name]["special_chars"]
    for char in field_value:
        if char.isdigit():
            continue
        if char.isalpha():
            continue
        if char not in allowed_specials:
            raise ValueError(f"Invalid special character {char} in field {field_value}. Allowed values are: {allowed_specials}.")

def range_validations(field_name: str, field_value: str) -> None:
    try:
        if field_value == "*" or field_value == "?":
            return
        if field_name == "month":
            range_validations_month(field_name, field_value)
        elif field_name == "day_of_week":
            range_validations_day_of_week(field_name, field_value)
        else:
            general_range_validation(field_name, field_value)
    except Exception as e:
        raise e



def general_range_validation(field_name: str, field_value: str) -> None:
    allowed_range = VALIDATION_DICT[field_name]["range"]
    extracted_numbers = re.findall(r'\d+', field_value)
    if extracted_numbers:
        extracted_numbers = sorted(map(int, extracted_numbers))
        if extracted_numbers[0] < allowed_range[0] or extracted_numbers[-1] > allowed_range[-1]:
            raise ValueError(f"Invalid range for field, value: {field_name, field_value}, must be in range of: {allowed_range}.")
    else:
        raise ValueError(f"Invalid value for field, value: {field_name, field_value}, no numbers found, must be in range of: {allowed_range}.")


def range_validations_month(field_name: str,field_value: str) -> None:
    extracted_numbers = re.findall(r'\d+', field_value)
    if extracted_numbers:
        extracted_numbers = list(map(int, extracted_numbers))
        return
    allowed_specials = VALIDATION_DICT[field_name]["special_chars"]
    month_strings = list(MONTH_DICT.keys())
    for char in allowed_specials:
        field_value = field_value.replace(char, " ")
    months = field_value.split()
    for month in months:
        if month not in month_strings:
            raise ValueError(f"Invalid value for field, value: {field_name, month}, must be in of: {month_strings}.")

def range_validations_day_of_week(field_name: str,field_value: str) -> None:
    extracted_numbers = re.findall(r'\d+', field_value)
    if extracted_numbers:
        extracted_numbers = list(map(int, extracted_numbers))
        return
    allowed_specials = VALIDATION_DICT[field_name]["special_chars"]
    weekday_strings = list(WEEK_DICT.keys())
    for char in allowed_specials:
        field_value = field_value.replace(char, " ")
    weekdays = field_value.split()
    for weekday in weekdays:
        if weekday not in weekday_strings:
            raise ValueError(f"Invalid value for field, value: {field_name, weekday}, must be in of: {weekday_strings}.")


def validate_field(field_name: str, field_value: str) -> None:
    try:
        field_name_validation(field_name)
        special_char_validation(field_name, field_value)
        range_validations(field_name, field_value)
    except Exception as e:
        raise e
