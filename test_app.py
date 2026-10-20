import unittest
from utils import format_response, validate_input

class TestAppUtils(unittest.TestCase):
    def test_format_response(self):
        res = format_response("OK", 200)
        self.assertTrue(res["success"])
        self.assertEqual(res["status"], 200)

    def test_validate_input_valid(self):
        self.assertTrue(validate_input("Hello"))

    def test_validate_input_invalid(self):
        self.assertFalse(validate_input(""))

if __name__ == "__main__":
    unittest.main()
