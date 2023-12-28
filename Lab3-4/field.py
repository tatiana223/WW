def field(items, *args):
    for item in items:
        if len(args) == 1:
            field_value = item.get(args[0])
            if field_value is not None:
                yield field_value
        else:
            filtered_item = {key: item.get(key) for key in args if item.get(key) is not None}
            if filtered_item:
                yield filtered_item


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]


for title in field(goods, 'title'):
    print(title)


for item in field(goods, 'title', 'price'):
    print(item)