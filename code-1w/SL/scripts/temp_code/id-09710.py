import itertools

def analyze_component_health(reading, threshold_map):
    # Irrelevant function - dead code path
    status = {}
    for k, v in threshold_map.items():
        status[k] = reading.get(k, 0) < v
    return status

def compute_signal_noise_ratio(signal, noise):
    # Distractor computation with misleading intermediate result
    snr_db = 10 * log_with_base(max(signal, 1e-6) / max(noise, 1e-6), 10)
    return snr_db if snr_db > 0 else 0

def log_with_base(value, base):
    # Used only once, subtly relevant but looks like general utility
    import math
    return math.log(value) / math.log(base)

def transform_dataset(data_matrix):
    # Unused transformation - red herring
    transposed = list(zip(*data_matrix))
    normalized = [[x / (sum(row) + 1e-8) for x in row] for row in transposed]
    return [list(col) for col in zip(*normalized)]

def filter_outliers(values, factor=1.5):
    # Seemingly important preprocessing, never actually used
    q1, q3 = sorted(values)[len(values)//4], sorted(values)[-len(values)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [v for v in values if lower <= v <= upper]

def evaluate_performance(metrics, weights):
    # Core logic buried in distractions
    adjusted = []
    temp_offsets = [0.1, -0.2, 0.3, -0.1, 0.0]  # Decoy adjustments
    
    # Real logic starts here — deeply nested and mixed with noise
    for idx, (metric, weight) in enumerate(itertools.zip_longest(metrics, weights, fillvalue=1.0)):
        if idx >= len(metrics):  # Safety break
            break
        
        # Simulated calibration offset (only one affects final result)
        calib = 0
        if idx == 2:
            calib = temp_offsets[4]  # Only temp_offsets[4] matters
        
        # Bit manipulation decoy
        raw_val = int((metric + calib) * 100)
        masked = raw_val & 0xFF  # Looks complex, but just bounds value
        
        # Conditional weighting with short-circuit red herring
        adj_weight = weight
        if idx == 1 and masked > 50:
            adj_weight *= 1.1
        elif idx == 3 or not (masked < 200):  # Always true due to mask
            adj_weight *= 0.9
        
        # Actual contribution
        contribution = (metric + calib) * adj_weight
        adjusted.append(contribution)
    
    # Aggregation hidden among unused transforms
    base_sum = sum(adjusted)
    penalty = 0
    for a in adjusted:
        if a > 10:  # This never triggers
            penalty += a * 0.05
    
    # Final nonlinear scaling that actually applies
    final_score = pow(base_sum, 1.1) - 15.0
    
    # Dead assignment - misleading
    final_score = round(final_score * 1.0001, 6)
    
    return final_score

# Unused data structures as distractors
dataset = [
    [1.2, 3.4, 2.1],
    [0.8, 2.9, 1.7],
    [1.5, 3.0, 2.5]
]

temp_thresholds = {
    'sensor_a': 75,
    'sensor_b': 80,
    'sensor_c': 90
}

# Seeded synthetic signal data — looks critical but only part is used
readings = [0.88, 0.91, 0.76, 0.82, 0.95]
signal_energy = sum(r**2 for r in readings)
noise_floor = 0.1 * sum(readings)

# Key variables embedded in noise
metrics = [0.85, 0.92, 0.78, 0.88]
weights = [1.0, 0.8, 1.2, 0.9]

# Unused intermediate calculations — heavy distraction
snr = compute_signal_noise_ratio(signal_energy, noise_floor)
filtered_metrics = [m for m in metrics if m > 0.75]  # Not actually used later
eval_data = transform_dataset(dataset)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Output requirement
print(f"Target result: {final_score}")