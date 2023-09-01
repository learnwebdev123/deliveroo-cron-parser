import unittest
from src.parser.cron_parser import CronParser
from unittest.mock import patch

class TestCronParser(unittest.TestCase):

    def test_valid_cron_expression(self):
        # Valid expression
        cron_expression = "*/15 0 1,15 JAN-DEC MON /usr/bin/command"
        parser = CronParser(cron_expression)
        parser.parse()
        # No assertion here, just making sure it runs without errors

    def test_invalid_cron_expression(self):
        # Invalid expression (missing a field)
        cron_expression = "*/15 0 1,15 JAN-DEC MON"
        with self.assertRaises(ValueError):
            parser = CronParser(cron_expression)
            parser.parse()

    def test_invalid_field_value(self):
        # Invalid field value for "minute"
        cron_expression = "*/70 0 1,15 JAN-DEC MON /usr/bin/command"
        with self.assertRaises(ValueError):
            parser = CronParser(cron_expression)
            parser.parse()

    def test_alpha_field_values(self):
        # Alpha values for "month" and "day_of_week"
        with self.assertRaises(ValueError):
            cron_expression = "*/15 0 1,15 ALPHA-BRAVO CHARLIE /usr/bin/command"
            parser = CronParser(cron_expression)
            parser.parse()


    def test_invalid_alpha_values(self):
        # Invalid alpha value
        cron_expression = "*/15 0 1,15 XYZ JAN-DEC MON /usr/bin/command"
        with self.assertRaises(ValueError):
            parser = CronParser(cron_expression)
            parser.parse()

    def test_command_handling(self):
        # Command handling
        with self.assertRaises(ValueError):
            cron_expression = "*/15 0 1,15 JAN-DEC MON /usr/bin/command with arguments"
            parser = CronParser(cron_expression)
            parser.parse()

    def test_special_characters(self):
        # Test handling of special characters
        cron_expression = "#/15 0 1,15 JAN-DEC MON /usr/bin/command"
        with self.assertRaises(ValueError):
            parser = CronParser(cron_expression)
            parser.parse()

    @patch("builtins.input", side_effect=["*/15 0 1,15 * 1-5 /usr/bin/find"])
    def test_parse(self, mock_input):
        expected_output = [
            "minute         0 15 30 45",
            "hour           0",
            "day_of_month   1 15",
            "month          0 1 2 3 4 5 6 7 8 9 10 11",
            "day_of_week    1 2 3 4 5",
            "command        /usr/bin/find"
        ]
        
        with patch("builtins.print") as mock_print:
            parser = CronParser(input("Enter cron expression: "))
            parser.parse()
            
            for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                printed_line = call_args[0][0]
                self.assertEqual(printed_line, expected_output_line)


if __name__ == "__main__":
    unittest.main()
