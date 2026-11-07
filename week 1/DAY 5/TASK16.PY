class Inventory:
    def __init__(self):
        self.items = ["Laptop", "Mobile", "Keyboard", "Mouse"]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


inv = Inventory()

print("Total Items:", len(inv))

print("First Item:", inv[0])
print("Second Item:", inv[1])
print("Third Item:", inv[2])