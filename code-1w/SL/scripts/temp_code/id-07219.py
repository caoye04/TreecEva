def calculate_efficiency(predicate, readings):
    valid = list(filter(predicate, readings))
    return len(valid) * 10 // len(readings) if readings else 0

# Airborne particle sensor readings in micrograms per cubic meter
test_readings = [35, 42, 58, 60, 20, 47, 55]
threshold = 50

# Irrelevant auxiliary variable (minimal distraction)
baseline_avg = sum(test_readings) / len(test_readings)

# Key computation step
dry_run = [x for x in test_readings if x < 60]
filtration_score = calculate_efficiency(lambda x: x > threshold, test_readings)

# Output result
print(f"Result: {filtration_score}")