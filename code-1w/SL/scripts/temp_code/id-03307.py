def analyze_performance(raw_data):
    processed = [x * 2 for x in raw_data if x > 15]
    filtered_set = {x for x in processed if x % 3 == 0}
    normalized_list = [round(x ** 0.5, 2) for x in filtered_set]
    normalized_set = set(normalized_list)
    extra_data = [1.41, 2.45, 3.87]
    temp_sum = sum(extra_data)
    final_score = max(normalized_set)
    return final_score

measurements = [10, 16, 18, 20, 24, 30]
result = analyze_performance(measurements)
print(f"Result: {result}")