import unittest
from atm_system import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        """Set up an ATM instance before each test"""
        self.atm = ATM(pin="1234", balance=5000)

    def test_authentication_correct_pin(self):
        self.assertTrue(self.atm.authenticate("1234"))

    def test_authentication_wrong_pin(self):
        self.assertFalse(self.atm.authenticate("0000"))

    def test_check_balance(self):
        self.assertEqual(self.atm.check_balance(), 5000)

    def test_successful_withdrawal(self):
        result = self.atm.withdraw(1000)
        self.assertEqual(result, "Withdrawal successful! New balance: $4000")

    def test_insufficient_balance(self):
        result = self.atm.withdraw(6000)
        self.assertEqual(result, "Insufficient balance!")

    def test_invalid_withdrawal(self):
        result = self.atm.withdraw(-500)
        self.assertEqual(result, "Invalid amount!")

if __name__ == '__main__':
    unittest.main()
