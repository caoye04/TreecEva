def analyze_readings(data, threshold=50):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    
    # Distractor: Irrelevant transformation
    transformed = list(map(lambda x: x * 1.5 + 2, data))
    avg_transformed = sum(transformed) / len(transformed)
    
    count_high = len(above_threshold)
    count_low = len(below_threshold)
    
    # Conditional expression used as per requirement
    status = 'stable' if count_high >= count_low else 'variable'
    
    return {'high': count_high, 'low': count_low, 'status': status}


def normalize_values(vals):
    # Dead function - never called but adds interference
    return [round((v - min(vals)) / (max(vals) - min(vals)), 3) for v in vals]


def calculate_performance(base, samples):
    results = []
    for sample_set in samples:
        analysis = analyze_readings(sample_set)
        if analysis['status'] == 'stable':
            impact = analysis['high'] * 2 - analysis['low']
        else:
            impact = analysis['high'] - analysis['low'] * 1.5
        results.append(impact)
    
    # Real computation path
    raw_total = sum(results)
    
    # Distractor: complex set operation with no effect
    unique_counts = set(results)
    temp_result = len(unique_counts.intersection({0, 1, 2})) * 10
    dummy_offset = temp_result - 5 if temp_result > 0 else 0
    
    # Actual logic that contributes to answer
    adjustment_factor = 1.2 if len(samples) > 3 else 0.8
    adjusted_total = raw_total * adjustment_factor
    
    # Final decision using conditional expression
    final_score = adjusted_total if base < 60 else adjusted_total * 0.9
    
    return int(final_score)

# Main execution
baseline = 45
readings = [
    [40, 55, 60, 70, 80],
    [30, 35, 50, 60],
    [55, 65, 75, 85, 90, 95],
    [20, 25, 30, 40, 45]
]

# Extraneous string processing for distraction
log_entry = "Performance report Q3"
sanitized = log_entry.lower().replace(" ", "_").strip()
dummy_checksum = sum([ord(c) for c in sanitized]) % 100

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")