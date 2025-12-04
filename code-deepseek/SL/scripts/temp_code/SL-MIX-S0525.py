def process_data(data_list):
    filtered = list(filter(lambda x: x % 3 == 0, data_list))
    processed = [item * 2 + 1 for item in filtered]
    return sum(processed) // len(processed) if processed else 0

items = [7, 12, 5, 18, 21, 9, 14, 6]
secondary_list = [2, 4, 8, 10]
final_result = process_data(items)
print(f"Result: {final_result}")