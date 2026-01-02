import math

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    return [23.4, 19.5, 27.3, 21.0, 30.2, 18.7, 24.1]

# Irrelevant helper: converts temperature to nonsense categories
def categorize(value):
    if value < 20:
        return 'A'
    elif value < 25:
        return 'B'
    else:
        return 'C'

# Dead function – never called but looks important
def legacy_normalization(data):
    mean = sum(data) / len(data)
    return [(x - mean) / mean * 100 for x in data]

# Distractor: complex transformation with no impact on result
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Real computation begins here — meaningful logic buried in noise
def filter_outliers(readings, threshold=2.0):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return [x for x in readings if abs(x - mean) <= threshold * std_dev]

# Weighted scoring using lambda abstraction (required feature)
evaluate_dimension = lambda value, ref: math.exp(-(abs(value - ref)) / 10)

# Another distractor: computes correlation but unused
def compute_correlation(x_vals, y_vals):
    n = len(x_vals)
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))
    sum_x2 = sum(x ** 2 for x in x_vals)
    sum_y2 = sum(y ** 2 for y in y_vals)
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    return numerator / denominator if denominator != 0 else 0

# Core logic hidden among red herrings
def calculate_baseline(readings):
    return sum(readings) / len(readings)

# Set operation used as per requirement (sensor IDs that passed quality check)
valid_sensors = {101, 102, 105, 107, 110}
failed_sensors = {103, 106, 109}
active_sensors = valid_sensors - failed_sensors  # Red herring; not used later

# More misdirection: tuple unpacking and dummy assignment
device_info = ('ENV-SCANv4', '2023-10-05', 'Field Zone 5')
device_model, deploy_date, location = device_info

# Simulated metric sources — some are decoys
raw_metrics = {
    'temp_avg': 24.1,
    'fluctuation_index': 0.87,
    'peak_count': 3,
    'stability_ratio': 0.91,
    'noise_floor': 0.05
}

# Actual relevant metrics embedded within irrelevant ones
metrics = {
    'temp_avg': raw_metrics['temp_avg'],
    'stability_ratio': raw_metrics['stability_ratio'],
    'fluctuation_index': raw_metrics['fluctuation_index']
}

# Weights for evaluation — subtle adjustment in logic chain
weights = {
    'temp_avg': 0.4,
    'stability_ratio': 0.35,
    'fluctuation_index': 0.25
}

# Critical function containing key reasoning steps
def evaluate_performance(met, wts):
    # Step 1: Base reference from domain knowledge
    ideal_temp = 22.0
    
    # Step 2: Score temperature deviation
    temp_score = evaluate_dimension(met['temp_avg'], ideal_temp)
    
    # Step 3: Invert fluctuation index (lower is better)
    fluct_score = 1 - met['fluctuation_index'] * 0.5
    
    # Step 4: Stability bonus
    stab_score = met['stability_ratio'] * 0.9
    
    # Step 5: Normalize scores to range [0,1]
    normalized_scores = [
        temp_score,
        max(0.1, min(0.95, fluct_score)),
        max(0.1, min(0.95, stab_score))
    ]
    
    # Step 6: Weighted combination
    weighted_sum = (
        normalized_scores[0] * wts['temp_avg'] +
        normalized_scores[1] * wts['stability_ratio'] +
        normalized_scores[2] * wts['fluctuation_index']
    )
    
    # Step 7: Apply nonlinear final adjustment
    adjusted_score = int(weighted_sum * 1000) / 1000  # Round down to 3 decimals
    
    # Step 8: Final scaling to integer score range [0, 100]
    final = int(adjusted_score * 100)
    
    # Decoy mutation below (does not affect output due to reassignment later)
    final += 5  # Misleading increment
    final = int( (temp_score * 40) + (stab_score * 35) + ((1-fluct_score) * 25) )  # Correct path override
    
    return final

# Out-of-place list comprehension with side-effect-free mutation
_ = [math.sin(x / 10) for x in range(1, 10)]

# Unused statistical summary
summary_stats = {
    'range': max(collect_readings()) - min(collect_readings()),
    'median': sorted(collect_readings())[len(collect_readings())//2]
}

# Readings collected and filtered (relevant)
data = collect_readings()
clean_data = filter_outliers(data)
baseline = calculate_baseline(clean_data)

# Assign metrics with correct baseline
metrics['temp_avg'] = baseline

# Evaluate performance — this is where final_score is set
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")