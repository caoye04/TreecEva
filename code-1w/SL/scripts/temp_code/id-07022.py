def analyze_signal(x, y):
    return (x ^ y) + (x >> 2)

# Irrelevant helper function (dead code path)
def unused_calibrate(data):
    return [d * 1.05 for d in data if d > 0]

# Another decoy: complex but unused transformation
def transform_readings(readings):
    adjusted = []
    for i, val in enumerate(readings):
        if i % 3 == 0:
            adjusted.append(val * 0.9)
        else:
            adjusted.append(val * 1.1)
    return sorted(adjusted, reverse=True)

# Distractor variables
temp_offset = 273.15
scaling_factor = 0.85
calibration_sequence = [1.1, 0.9, 1.2, 0.8]

# Real processing begins here
def compute_stability_index(seq):
    total = 0
    for i in range(1, len(seq)):
        total += abs(seq[i] - seq[i-1])
    return total / len(seq) if seq else 0

thresholds = {
    'normal': 3.5,
    'warning': 6.0,
    'critical': 9.0
}

health_data = [
    2.3, 4.1, 3.8, 5.6, 2.9, 4.4, 6.1, 3.7, 5.2, 4.8,
    3.9, 5.5, 4.3, 6.7, 5.1, 4.6, 3.4, 5.8, 4.9, 5.3
]

# Misleading intermediate computation (not used in final result)
avg_data = sum(health_data) / len(health_data)
std_dev = (sum((x - avg_data) ** 2 for x in health_data) / len(health_data)) ** 0.5

# Another red herring: frequency analysis on indices
index_pairs = list(zip(range(len(health_data)), health_data))
frequency_map = {}
for idx, val in index_pairs:
    category = 'even' if idx % 2 == 0 else 'odd'
    frequency_map[category] = frequency_map.get(category, 0) + 1

# Key processing function
def process_metrics(data, limits):
    # Step 1: Compute stability index
    stability = compute_stability_index(data)
    
    # Step 2: Count how many readings exceed warning threshold
    high_readings = [x for x in data if x > limits['warning']]
    
    # Step 3: Use enumerate to find first critical breach
    first_critical_index = None
    for i, reading in enumerate(data):
        if reading > limits['critical'] and first_critical_index is None:
            first_critical_index = i
    
    # Step 4: Compute diagnostic score using bitwise and arithmetic ops
    base_score = int(stability * 10)
    penalty = len(high_readings) << 1  # Left shift as multiplier
    
    # Step 5: Conditional adjustment based on presence of critical reading
    adjustment = -5 if first_critical_index is not None and first_critical_index < 10 else 3
    
    # Step 6: Composite metric with distractor operation (only half used)
    temp_metric = (base_score + penalty) ^ 7
    final_score = temp_metric + adjustment  # Only this part matters
    
    # Step 7: Final classification logic
    if final_score < 10:
        level = 1
    elif final_score < 20:
        level = 2
    else:
        level = 3
    
    # Step 8: Combine with stability via conditional expression
    final_diagnostic = level * 100 + (
        int(stability) if stability > 2.0 else 0
    )
    
    return final_diagnostic

# Execute main logic
interim_result = analyze_signal(23, 17)  # Distractor call
baseline = [x * scaling_factor for x in health_data]  # Unused transformed data

final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")