def calculate_performance(base, data):
    adjusted = [x - base for x in data if x > base * 0.9]
    valid_count = len(adjusted) if len(adjusted) > 0 else 1
    avg_adjusted = sum(adjusted) / valid_count
    penalty = 5 if any(x < base * 0.95 for x in data) else 0
    return int(avg_adjusted) - penalty

baseline = 87.5
readings = [92, 88, 95, 84, 90]
initial_check = True if readings[0] > baseline else False
temp_offset = 3.2  # unused variable (minor interference)
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")