def calculate_filtered_weight(items, threshold):
    weights = [len(item) * 1.5 for item in items]
    filtered_weights = [w for w in weights if w > threshold]
    total_weight = sum(filtered_weights)
    return total_weight

items_list = ['apple', 'fig', 'banana', 'pear', 'kiwi']
threshold_value = 6.0
total_weight = calculate_filtered_weight(items_list, threshold_value)
print(f"Result: {total_weight}")