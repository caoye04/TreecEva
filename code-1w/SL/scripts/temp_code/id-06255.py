import itertools

# Simulated sensor data processing pipeline for environmental monitoring system
def analyze_readings(raw_data):
    filtered = [x for x in raw_data if 10 <= x <= 100]
    smoothed = []
    for i in range(1, len(filtered) - 1):
        avg = (filtered[i-1] + filtered[i] + filtered[i+1]) / 3
        smoothed.append(round(avg, 2))
    return smoothed

# Irrelevant auxiliary function - dead code path
def legacy_compatibility_mode(data):
    result = 0
    for item in data:
        if item % 7 == 0:
            result += item // 7
    return result

# Core metric computation with distractors
def compute_metrics(readings):
    total_energy = sum(readings)
    peak_reading = max(readings) if readings else 0
    base_level = min(readings) if readings else 0
    
    # Distractor variables - not used in final calculation
    temp_offset = 0.0
    calibration_factor = 1.0
    noise_floor = sum(1 for r in readings if r < 20)
    stability_index = 0
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) > 5:
            stability_index += 1

    # Real metric computations
    variance = sum((r - sum(readings)/len(readings))**2 for r in readings) / len(readings) if readings else 0
    normalized_power = total_energy / 100.0
    efficiency_ratio = (peak_reading - base_level) / peak_reading if peak_reading != 0 else 0
    
    # Hidden intermediate - looks important but isn't final
    preliminary_score = (normalized_power * 0.3) + (efficiency_ratio * 0.7)
    
    return {
        'power': normalized_power,
        'efficiency': efficiency_ratio,
        'variance': variance,
        'stability': stability_index  # Red herring - looks like it should matter
    }

# Weighted evaluation with misleading components
def evaluate_performance(metrics, weights):
    # These weights appear to be used but are decoys
    default_weights = {'power': 0.4, 'efficiency': 0.4, 'variance': 0.1, 'stability': 0.1}
    debug_mode = False
    override_threshold = -1  # Unused override
    
    # Actual weight application
    score = 0.0
    for key in weights:
        if key in metrics:
            # Only power and efficiency actually contribute
            if key in ['power', 'efficiency']:
                score += metrics[key] * weights[key]
    
    # Critical nonlinear transformation
    if score > 0:
        score = (score ** 1.5) * 10
    
    # Additional distraction: conditional that never triggers
    if debug_mode and override_threshold > 0:
        score = override_threshold
    
    # Final adjustment based on hidden rule
    adjustment = 1.0
    if metrics['variance'] < 50 and metrics['efficiency'] > 0.5:
        adjustment = 1.2
    
    return int(score * adjustment)  # Discrete rounding effect

# Generate synthetic data using itertools - relevant
base_pattern = [23, 45, 67, 54, 32]
cyclic_data = list(itertools.islice(itertools.cycle(base_pattern), 20))
noise_component = [i % 3 * 2 for i in range(20)]
sensor_input = [a + b for a, b in zip(cyclic_data, noise_component)]

# Process data through pipeline
cleaned = analyze_readings(sensor_input)
metrics = compute_metrics(cleaned)

# Assign weights - only these two matter despite four being defined
weights = {
    'power': 0.65,
    'efficiency': 0.35,
    'variance': 0.2,   # Unused in logic
    'stability': 0.1   # Unused in logic
}

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")