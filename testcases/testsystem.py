import unittest
from src.logic import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        """Create an ATM instance before each test"""
        self.atm = ATM(5000)

    def test_valid_withdrawal(self):
        """Test withdrawing a valid amount"""
        self.assertEqual(self.atm.withdraw(1000), "✅ Withdrawal successful! Remaining balance: $4000")

    def test_insufficient_funds(self):
        """Test withdrawing more than available balance"""
        self.assertEqual(self.atm.withdraw(6000), "❌ Insufficient funds! Try a lower amount.")

    def test_negative_or_zero_withdrawal(self):
        """Test withdrawing a negative or zero amount"""
        self.assertEqual(self.atm.withdraw(0), "❌ Invalid amount! Enter a positive number.")
        self.assertEqual(self.atm.withdraw(-500), "❌ Invalid amount! Enter a positive number.")

if __name__ == "__main__":
    unittest.main()
