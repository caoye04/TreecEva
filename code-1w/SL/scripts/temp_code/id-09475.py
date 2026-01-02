def calculate_performance(base, data):
    adjustment_factor = 1.25
    threshold = base * 0.75
    filtered = [x for x in data if x > threshold]
    
    # Irrelevant transformation (distractor)
    transformed = list(map(lambda x: (x ** 0.5) * 1.5, data))
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0

    # Core logic
    valid_count = len(filtered)
    total = sum(filtered)
    raw_score = total / valid_count if valid_count > 0 else 0
    
    # Secondary distractor: unused complex computation
    outlier_detect = any(abs(x - raw_score) > 20 for x in data)
    safety_offset = -5 if outlier_detect else 0

    # Conditional expression influencing final result
    bonus = 10 if valid_count >= 4 else 5
    
    # Actual performance score calculation
    final_score = (raw_score * adjustment_factor) + bonus
    
    # Dead code path (never executed but adds noise)
    if False:
        fallback = base * 1.1
        final_score = max(final_score, fallback)

    return final_score

# Sensor baseline calibration
baseline = 40

# Simulated sensor readings (e.g., temperature in Fahrenheit)
readings = [35, 42, 48, 33, 55, 41]

# Auxiliary irrelevant variable
normal_range = [x for x in readings if 38 <= x <= 45]

# Key computation step
final_score = calculate_performance(baseline, readings)

# Output result
print(f"Result: {final_score}")