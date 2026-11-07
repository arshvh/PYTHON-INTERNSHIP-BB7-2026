import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Timer Started.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()

        total = self.end - self.start

        print("Timer Stopped.")
        print("Time Taken:", round(total, 4), "seconds")


with Timer():
    for i in range(1000000):
        pass