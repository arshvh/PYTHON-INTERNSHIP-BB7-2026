class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies.")

        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies.")

        return self.amount > other.amount


m1 = Money(500, "INR")
m2 = Money(1000, "INR")

print("M1 < M2:", m1 < m2)
print("M1 > M2:", m1 > m2)

m3 = Money(500, "USD")

try:
    print(m1 > m3)
except ValueError as e:
    print("Error:", e)