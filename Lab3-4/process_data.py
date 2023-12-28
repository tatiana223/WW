import json
from datetime import datetime
from contextlib import contextmanager

def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@contextmanager
def cm_timer_1():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print("Выполнение заняло: {}".format(end_time - start_time))

def f1(data):
    return sorted(set(item['Профессия'] for item in data), key=lambda x: x.lower())

def f2(data):
    return list(filter(lambda x: x.startswith('программист'), data))

def f3(data):
    return list(map(lambda x: x + ', с опытом Python', data))

def f4(data):
    salaries = range(100000, 200001)
    return [f'{profession}, зарплата {salary} руб.' for profession, salary in zip(data, salaries)]

with open('data_light.json') as file:
    data = json.load(file)

with cm_timer_1():
    f4_result = f4(f3(f2(f1(data))))