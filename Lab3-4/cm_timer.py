import time

class cm_timer_1:
    def __enter__(self):     #менеджер контекст
        self.start_time = time.time()

    def __exit__(self, *args):
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f"time: {execution_time}")

import time
from contextlib import contextmanager
@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"time: {execution_time}")

with cm_timer_1():
    time.sleep(5.5)
with cm_timer_2():
    time.sleep(5.5)