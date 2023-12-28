class Unique:
    def __init__(self, data, ignore_case=False):
        self.data = data
        self.ignore_case = ignore_case
        self.seen = set()
    def __iter__(self):
        return self
    def __next__(self):
        for item in self.data:
            if self.ignore_case and isinstance(item, str):
                item_key = item.lower()
            else:
                item_key = item
            if item_key not in self.seen:
                self.seen.add(item_key)
                return item
        raise StopIteration
data_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = Unique(data_list)
for item in unique_list:
    print(item)

data_generator = (x for x in range(5))
unique_generator = Unique(data_generator)
for item in unique_generator:
    print(item)

data_list = ['apple', 'banana', 'Apple', 'cherry']
unique_list_ignore_case = Unique(data_list, ignore_case=True)
for item in unique_list_ignore_case:
    print(item)