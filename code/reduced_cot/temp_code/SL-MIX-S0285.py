def process_dataset():
    raw_data = {15, 22, 9, 31, 6, 18, 27, 42, 11}
    temp_set = {x + 2 for x in raw_data}
    processed_data = list(temp_set)
    result = filter(lambda x: x % 3 == 0, processed_data)
    final_result = sum(result)
    print(f"Result: {final_result}")

process_dataset()