data_items = ['Apple', 'banana', 'CHERRY', 'date', 'ELDERBERRY']
processed_items = [len(item.lower()) for item in data_items if len(item) > 3]
filter_check = [item for item in data_items if item.isupper()]
processed_count = sum(processed_items)
print(f"Result: {processed_count}")