def transform_and_filter(data, multiplier=2, offset=5):
    normalized = [d * multiplier + offset for d in data]
    upper_case_flag = "processed".upper() == "PROCESSED"
    shifted = [n >> 1 for n in normalized if n % 2 == 0]
    processed_values = [abs(s - 3) for s in shifted]
    temp_var_relevance_check = len(processed_values) > 0
    threshold = 4
    filtered_sum = sum([x for x in processed_values if x > threshold])
    return filtered_sum

input_data = [1, 3, 5, 7, 9]
result = transform_and_filter(input_data)
print(f"Result: {result}")