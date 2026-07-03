# Define a @dataclass called 'BankAccount'
# Attributes: owner (str), balance (float) = 0.0
# 
# Add methods:
# - deposit(amount) -> None
# - withdraw(amount) -> bool (returns False if insufficient funds)

from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> bool:
        """Withdraws an amount if funds are sufficient. Returns True if successful, False otherwise."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
            
        if amount > self.balance:
            return False
            
        self.balance -= amount
        return True

# Ensure the __repr__ looks like: "BankAccount(owner='Alice', balance=100.0)"
print(BankAccount("Alice", 100.0))  # Example usage