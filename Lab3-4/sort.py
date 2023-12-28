data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
sorted_data = sorted(data, key=lambda x: abs(x), reverse=True)
print(sorted_data)

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
sorted_data = sorted(data, key=abs, reverse=True)
print(sorted_data)