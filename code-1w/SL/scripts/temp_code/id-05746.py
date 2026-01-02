def calculate_performance(base, data):
    adjusted = [x - base for x in data if x > base * 0.8]
    valid_count = len(adjusted)
    if valid_count == 0:
        return 0
    avg_adjusted = sum(adjusted) / valid_count
    bonus = 10 if avg_adjusted > 25 else 5
    return int(avg_adjusted) + bonus

baseline = 20
readings = [18, 22, 26, 15, 30, 28]
extra_offset = 3  # Irrelevant distractor variable
temp_result = [x * 0.95 for x in readings]  # Unused computation
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")