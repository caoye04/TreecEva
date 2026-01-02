def calculate_performance(base, data):
    adjusted = [abs(val - base) for val in data if isinstance(val, (int, float))]
    filtered = [v for v in adjusted if v > 0]
    normalized = sum(v ** 0.5 for v in filtered)
    bonus = 10 if len(data) > 5 else 5
    penalty = 2 * (len(filtered) % 3)
    return int(normalized) + bonus - penalty

baseline = 77.5
readings = [75, 80, 'N/A', 70.2, 78, None, 85.3]

# Preprocessing: clean non-numeric entries
clean_readings = [r for r in readings if isinstance(r, (int, float))]

# Secondary metric (distractor)
variance_estimate = sum((r - baseline) ** 2 for r in clean_readings) / len(clean_readings)

# Key computation
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")