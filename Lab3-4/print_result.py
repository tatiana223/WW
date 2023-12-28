def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Выполнение функции {func.__name__}:")
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return wrapper

@print_result
def add(a, b):
    return a + b
@print_result
def multiply(a, b):
    return a * b
@print_result
def get_list():
    return ['a','c' ]
@print_result
def get_dict():
    return {'a': 1, 'b': 2, 'c': 3}
add(2, 3)
multiply(4, 5)
get_list()
get_dict()