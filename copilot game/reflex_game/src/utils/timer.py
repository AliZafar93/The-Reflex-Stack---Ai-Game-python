class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0

    def start(self):
        import time
        self.start_time = time.time()

    def stop(self):
        import time
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time

    def get_elapsed_time(self):
        return self.elapsed_time

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0