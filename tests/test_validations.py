import unittest
from src.parser.validations import (
    field_name_validation,
    special_char_validation,
    range_validations,
    validate_field
)

class TestValidationFunctions(unittest.TestCase):

    def test_field_name_validation_valid(self):
        # Valid field name
        valid_field_name = "minute"
        self.assertIsNone(field_name_validation(valid_field_name))

    def test_field_name_validation_invalid(self):
        # Invalid field name
        invalid_field_name = "invalid_field"
        with self.assertRaises(ValueError):
            field_name_validation(invalid_field_name)

    def test_special_char_validation_valid(self):
        # Valid special characters
        valid_field_name = "minute"
        valid_field_value = "*/-,"
        self.assertIsNone(special_char_validation(valid_field_name, valid_field_value))

    def test_special_char_validation_invalid(self):
        # Invalid special characters
        invalid_field_name = "minute"
        invalid_field_value = "*/+,"
        with self.assertRaises(ValueError):
            special_char_validation(invalid_field_name, invalid_field_value)

    def test_range_validations_valid(self):
        # Valid range
        valid_field_name = "minute"
        valid_field_value = "0-59"
        self.assertIsNone(range_validations(valid_field_name, valid_field_value))

    def test_range_validations_invalid(self):
        # Invalid range
        invalid_field_name = "minute"
        invalid_field_value = "60-70"
        with self.assertRaises(ValueError):
            range_validations(invalid_field_name, invalid_field_value)

    def test_validate_field_valid(self):
        # Valid field
        valid_field_name = "minute"
        valid_field_value = "0-59"
        self.assertIsNone(validate_field(valid_field_name, valid_field_value))

    def test_validate_field_invalid(self):
        # Invalid field
        invalid_field_name = "minute"
        invalid_field_value = "60-70"
        with self.assertRaises(ValueError):
            validate_field(invalid_field_name, invalid_field_value)

if __name__ == "__main__":
    unittest.main()
