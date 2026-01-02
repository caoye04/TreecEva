from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring system
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    normalized = [(x - 10) / (100 - 10) for x in filtered]
    return normalized

# Irrelevant helper - decoy function dealing with unrelated domain
def calculate_footprint(elements):
    total = 0
    for e in elements:
        if e % 3 == 0:
            total += e * 1.5
        elif e % 5 == 0:
            total += e * 0.7
    return total  # Never used in main logic

# Core transformation pipeline
def transform_sequence(seq):
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append(int(val * 100) ** 2)
        else:
            result.append(int(val * 50) + 10)
    return result

# Auxiliary analysis - looks important but feeds dead end
def analyze_distribution(values):
    freq = Counter(values)
    mode = max(freq, key=freq.get)
    spread = len([v for v in freq.values() if v > 1])
    return {'mode': mode, 'repeats': spread}

# Secondary path - unused but plausible sounding
def generate_baseline_ref(n, seed=42):
    math.sin(seed)  # dummy use
    ref = []
    for i in range(n):
        ref.append((i * seed) % 17)
    return ref  # Computed but not used

def detect_anomalies(data):
    anomalies = []
    for d in data:
        if d > 85 or d < 15:
            anomalies.append(d)
    return anomalies  # Looks critical but irrelevant

# Main evaluation logic - where actual answer originates
def compute_stability_index(vals):
    if not vals:
        return 0
    mean_val = sum(vals) / len(vals)
    variance = sum((x - mean_val) ** 2 for x in vals) / len(vals)
    return round(math.sqrt(variance), 6)

def evaluate_metric(chain, threshold=4500):
    tally = 0
    for item in chain:
        if isinstance(item, int) and item > threshold:
            tally += item // 100
    return tally + 3  # Key contribution to final result

# Real processing begins here
raw_sensor_data = [15, 95, 105, 5, 67, 88, 120, 44, 53, 9]  # Includes out-of-range values
processed = preprocess_readings(raw_sensor_data)

target_series = transform_sequence(processed)

# Dead-end analytics - distractors with plausible naming
usage_pattern = analyze_distribution(target_series)
detected_outliers = detect_anomalies([int(p*100) for p in processed])
baseline_grid = generate_baseline_ref(len(target_series), seed=12)

# Decoy metric computation
phantom_score = calculate_footprint(baseline_grid)
spike_count = len(detected_outliers)

# Actual relevant data structures
metric_data = defaultdict(float)
metric_data['readings'] = len(processed)
metric_data['amplitude'] = sum(target_series) // len(target_series)
metric_data['consistency'] = compute_stability_index(target_series[:5])

baseline = {
    'level': 42,
    'tolerance': 0.05,
    'reference_set': [4, 8, 15, 16, 23, 42]
}

# This function actually computes the answer
# Cross-concept: combines dict access, modular arithmetic, conditional expression, set ops
def evaluate_performance(metrics, base_config):
    readings_count = metrics['readings']
    avg_power = metrics['amplitude']
    stability = metrics['consistency']
    
    # Complex conditional with red herring variables
    reference_set = set(base_config['reference_set'])
    extended_check = reference_set | {avg_power % 100}  # Set union - one-time use
    
    adjustment_factor = 1
    if avg_power > 4000:
        adjustment_factor = 2
    elif stability < 10:
        adjustment_factor = 1.5
    
    # Core calculation buried among distractions
    base_component = (readings_count * avg_power) // 100
    stability_bonus = int(stability * 2)
    
    # Modular arithmetic combined with conditional
    modifier = (base_component + 13) % 19
    if modifier in extended_check:
        modifier *= 2
    
    # Critical line - this feeds into final result
    intermediate = base_component + stability_bonus - modifier
    
    # More distractions
    diagnostic_flag = False
    if intermediate > 100 and stability > 5:
        diagnostic_flag = True  # Unused boolean
    
    # Additional irrelevant transformation
    shadow_copy = [intermediate // 3 for _ in range(3)]  # Dead assignment
    
    # Final composition using decoy function
    external_weight = evaluate_metric(target_series)  # Returns 7
    final_value = intermediate + external_weight + adjustment_factor
    
    return int(final_value)

# Execution point of interest
final_score = evaluate_performance(metric_data, baseline)

# Output required format
print(f"Result: {final_score}")