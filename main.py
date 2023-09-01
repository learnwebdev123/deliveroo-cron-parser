from src.parser.cron_parser import CronParser
RED_COLOR = "\033[91m"
RESET_COLOR = "\033[0m"

if __name__ == "__main__":
    try:
        cron_expression = input("Enter cron expression: ")
        parser = CronParser(cron_expression)
        parser.parse()
    except Exception as e:
        print(f"{RED_COLOR}{e.args[0]}{RESET_COLOR}")