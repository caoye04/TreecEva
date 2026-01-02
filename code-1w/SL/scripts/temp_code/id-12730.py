def calculate_performance(base, data):
    adjusted = [abs(val - base) for val in data if isinstance(val, (int, float))]
    filtered = [val for val in adjusted if val > 0]
    if len(filtered) == 0:
        return base % 7
    avg_deviation = sum(filtered) / len(filtered)
    penalty = avg_deviation * 0.8 if avg_deviation > 5 else avg_deviation * 0.3
    return int(base - penalty)

baseline = 42
readings = [40, 45, 'error', 38, 50, None, 41]

# Irrelevant auxiliary variable (minor distraction)
temp_log = "Processing completed successfully"

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")