def calculate_performance(base, data):
    filtered = list(filter(lambda x: x > base * 0.75, data))
    adjusted = [val % 100 for val in filtered]
    normalized = sum(adjusted) / len(adjusted) if adjusted else 0
    return int(normalized * 1.2)

baseline = 85
readings = [92, 67, 88, 74, 101, 55, 89]
temp_offset = 3.14
dummy_list = [x ** 0.5 for x in readings[:3]]
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")