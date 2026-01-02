def calculate_performance(base, data):
    adjustment = 1.5 if base < 100 else 0.8
    filtered = [x for x in data if x > base * 0.7]
    avg = sum(filtered) / len(filtered) if filtered else 0
    return (avg - base) * adjustment

baseline = 95
readings = [88, 92, 96, 78, 105, 87]

# Irrelevant distraction: unused variable
temp_log = {'processed': len(readings), 'threshold': baseline * 0.7}

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")