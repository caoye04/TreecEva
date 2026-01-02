def calculate_performance(base, data):
    adjusted = [abs(val - base) for val in data]
    filtered = [val for val in adjusted if val > 0.5]
    normalized = sum(filtered) / len(filtered) if filtered else 0.0
    return round(normalized * 100, 2)

baseline = 7.2
readings = [6.8, 7.5, 7.1, 6.9, 8.0, 7.0, 6.7]

# String manipulation for logging (irrelevant to computation)
timestamp = "2023-11-05T14:30:00"
date_part = timestamp.split('T')[0]
time_part = timestamp.split('T')[1]
log_entry = f"Processing session {date_part.replace('-', '')}_{time_part.replace(':', '')}"

# Core computation
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")