# atm_system.py

class ATM:
    def __init__(self, balance=5000):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "❌ Invalid amount! Enter a positive number."
        if amount > self.balance:
            return "❌ Insufficient funds! Try a lower amount."
        
        self.balance -= amount
        return f"✅ Withdrawal successful! Remaining balance: ${self.balance}"
