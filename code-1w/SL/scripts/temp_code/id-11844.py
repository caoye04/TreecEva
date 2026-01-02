def calculate_performance(base, data):
    adjusted = [abs(val - base) for val in data]
    filtered = adjusted[1:-1]  # Exclude first and last adjustments
    high_deviation = [val for val in filtered if val > 5]
    penalty = len(high_deviation) * 0.5
    bonus = 2.0 if all(d < 8 for d in filtered) else 0.0
    return len(filtered) + bonus - penalty

baseline = 10
readings = [12, 3, 9, 16, 7, 11, 4]
initial_check = readings[0] > 5  # Irrelevant logic (distractor)
temp_sum = sum(readings) / len(readings)  # Distractor variable
deviation_count = 0  # Unused variable for minor interference
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")