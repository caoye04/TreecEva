def process_data():
    raw_values = [3, 8, 1, 12, 6, 4, 9, 11]
    offset = 2
    threshold = 5
    temp_result = [x + offset for x in raw_values]
    values = [x * 1 for x in temp_result]
    filtered_sum = sum(sorted(filter(lambda x: x > threshold, values)))
    debug_flag = False
    if debug_flag:
        print("Debug: ", values)
    return filtered_sum

result = process_data()
print("Result:", result)