class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, amount):
        if amount < 0 or self.size + amount > self.capacity:
            raise ValueError("Invalid deposit amount")
        self.size += amount

    def withdraw(self, amount):
        if amount < 0 or self.size - amount < 0:
            raise ValueError("Invalid withdraw amount")
        self.size -= amount