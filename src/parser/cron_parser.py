import re
from src.parser.consts import VALIDATION_DICT, MONTH_DICT, WEEK_DICT
from src.parser.validations import validate_field

class CronParser:
    def __init__(self, cron_expression):
        self.cron_expression = cron_expression
        self.field_names = ["minute", "hour", "day_of_month", "month", "day_of_week"]
        self.result_dict = {}

    def split(self):
        field_values = self.cron_expression.split()
        if len(field_values)!=6:
            raise ValueError(f"Invalid cron Expression must contain 6 fields got {len(field_values)} fields.")
        self.command = field_values[-1]
        field_values.pop(-1)
        self.cron_dict = dict(zip(self.field_names, field_values))

    def validate(self, field_name, field_value):
        try:
            validate_field(field_name, field_value)
        except Exception as e:
            raise e

    def parse_field_day_of_week(self, field_value):
        values = []
        for part in field_value.split(","):
            if "-" in part:
                start, end = part.split("-")
                start = int(start) if start.isdigit() else WEEK_DICT[start]
                end = int(end) if end.isdigit() else WEEK_DICT[end]
                values.extend(range(start, end+1))
            else:
                values.append(WEEK_DICT[part]) if part.isalpha() else values.append(int(part))
        return values

    def parse_field_month(self, field_value):
        values = []
        for part in field_value.split(","):
            if "-" in part:
                start, end = part.split("-")
                start = int(start) if start.isdigit() else MONTH_DICT[start]
                end = int(end) if end.isdigit() else MONTH_DICT[end]
                values.extend(range(start, end+1))
            else:
                values.append(MONTH_DICT[part]) if part.isalpha() else values.append(int(part))
        return values


    def parse_field_generic(self, field_value) -> list:
        values = []
        for part in field_value.split(","):
            if "-" in part:
                start, end = part.split("-")
                values.extend(range(start, end))
            else:
                values.append(int(part))
        return values


    def parse_field(self, field_name, field_value, field_range):
        values = []
        lower_limit, upper_limit = field_range[0], field_range[1]+1

        if field_value == "*":
            values = range(lower_limit, upper_limit)
        elif "/" in field_value:
            start, step = field_value.split("/")
            if start == "*":
                start = lower_limit
            else:
                start = int(start)
            step = int(step)
            values.extend(range(start, upper_limit, step))
        else:
            if field_name == "month":
                values = self.parse_field_month(field_value)
            elif field_name == "day_of_week":
                values =  self.parse_field_day_of_week(field_value)
            else:
                values =  self.parse_field_generic(field_value)
        return sorted(set(values))

    def expand(self):
        for field_name, field_value in self.cron_dict.items():
            self.validate(field_name, field_value)
            field_range = VALIDATION_DICT[field_name]["range"]
            self.result_dict[field_name] = self.parse_field(field_name, field_value, field_range)

    def parse_print(self):
        for field_name, values in self.result_dict.items():
            print(f"{field_name:<14} {' '.join(map(str, values))}")
        input_key = "command"
        print(f"{input_key:14} {self.command}")

    def parse(self):
        self.split()
        self.expand()
        self.parse_print()


if __name__ == "__main__":
    cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
    command = "/usr/bin/command"
    parser = CronParser(cron_expression)
    parser.parse()
