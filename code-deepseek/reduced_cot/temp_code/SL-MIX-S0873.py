def process_items(data):
    filter_condition = lambda x: x % 3 == 0 and x > 5
    items_dict = {'A': 12, 'B': 7, 'C': 9, 'D': 4, 'E': 15}
    filtered_values = [value for value in items_dict.values() if filter_condition(value)]
    final_count = len(filtered_values) * 2 if len(filtered_values) > 2 else len(filtered_values) + 1
    print(f"Target result: {final_count}")
    return final_count

items_dict = {'X': 6, 'Y': 8, 'Z': 3}
final_count = process_items(items_dict)