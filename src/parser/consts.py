VALIDATION_DICT = {
    "minute": {
        "required": True,
        "range": [0, 59],
        "special_chars": [",", "-", "*", "/"]
    },
    "hour": {
        "required": True,
        "range": [0, 23],
        "special_chars": [",", "-", "*", "/"]
    },
    "day_of_month": {
        "required": True,
        "range": [1, 31],
        "special_chars": [",", "-", "*", "/", "?"]
    },
    "month": {
        "required": True,
        "range": [0, 11],
        "special_chars": [",", "-", "*", "/"]
    },
    "day_of_week": {
        "required": True,
        "range": [1, 7],
        "special_chars": [",", "-", "*", "/", "?"]
    }
}

WEEK_DICT = {
    "SUN": 1,
    "MON": 2,
    "TUE": 3,
    "WED": 4,
    "THU": 5,
    "FRI": 6,
    "SAT": 7
}

MONTH_DICT = {
    "JAN": 0,
    "FEB": 1,
    "MAR": 2,
    "APR": 3,
    "MAY": 4,
    "JUN": 5,
    "JUL": 6,
    "AUG": 7,
    "SEP": 8,
    "OCT": 9,
    "NOV": 10,
    "DEC": 11
}