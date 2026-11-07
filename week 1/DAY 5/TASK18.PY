class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)
        print(item, "pushed into stack.")

    def pop(self):
        if len(self.__items) > 0:
            return self.__items.pop()
        else:
            return "Stack is empty."

    def __str__(self):
        return str(self.__items)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s)

print("Popped Item:", s.pop())

print("Updated Stack:", s)