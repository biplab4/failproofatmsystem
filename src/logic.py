class ATM:
    def __init__(self, pin, balance):
        self.correct_pin = pin
        self.balance = balance

    def authenticate(self, entered_pin):
        """Check if the entered PIN is correct"""
        return entered_pin == self.correct_pin

    def check_balance(self):
        """Return current balance"""
        return self.balance

    def withdraw(self, amount):
        """Withdraw money if sufficient balance"""
        if amount > self.balance:
            return "Insufficient balance!"
        elif amount <= 0:
            return "Invalid amount!"
        else:
            self.balance -= amount
            return f"Withdrawal successful! New balance: ${self.balance}"
