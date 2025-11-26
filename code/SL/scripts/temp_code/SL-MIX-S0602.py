def process_data(data_items):
    text_data = '|'.join(data_items)
    segments = text_data.split('|')
    numeric_values = list(map(lambda x: len(x) * 2 if x.isalpha() else int(x), segments))
    return sum(numeric_values[:3])

items = ['abc', '12', 'def', '45', 'ghi']
processed_value = process_data(items)
print(f"Result: {processed_value}")