usernames = ["Ali", "Arshil", "Ahmed", "John", "Mohammad"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print("Valid Usernames:", result)