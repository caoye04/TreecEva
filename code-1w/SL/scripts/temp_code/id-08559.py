from itertools import combinations
from functools import reduce

# Simulated sensor data with noise and redundant metrics
data_set = [
    {'temp': 23.5, 'pressure': 1013.25, 'humidity': 45, 'altitude': 120, 'signal': 87},
    {'temp': 24.1, 'pressure': 1012.7, 'humidity': 47, 'altitude': 125, 'signal': 85},
    {'temp': 22.8, 'pressure': 1014.1, 'humidity': 43, 'altitude': 118, 'signal': 90},
    {'temp': 25.3, 'pressure': 1011.9, 'humidity': 50, 'altitude': 130, 'signal': 82}
]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.015
OFFSET_X = 3.14159
OFFSET_Y = 2.71828

# Weight configuration for relevant dimensions (only temp and humidity actually used)
weights = {
    'temp': 0.4,
    'humidity': 0.6,
    'pressure': 0.1,  # unused in final calculation
    'altitude': 0.05,  # unused
    'signal': 0.02    # unused
}

# Phantom transformation functions (some are dead code)
def transform_pressure(p):
    return p * 0.001 + OFFSET_X

def adjust_signal_strength(s):
    if s > 85:
        return s * CALIBRATION_FACTOR_A
    else:
        return s * CALIBRATION_FACTOR_B

# Real processing logic hidden among distractors
def extract_relevant_metrics(records):
    extracted = []
    for record in records:
        # Only temp and humidity contribute
        score = record['temp'] * weights['temp'] + record['humidity'] * weights['humidity']
        extracted.append(round(score, 4))
    return extracted

# Decoy function using set operations (irrelevant path)
def analyze_anomalies(records):
    high_temp = {i for i, r in enumerate(records) if r['temp'] > 24}
    low_signal = {i for i, r in enumerate(records) if r['signal'] < 85}
    cross_alert = high_temp & low_signal
    return len(cross_alert) > 0  # never used

# Lambda-based smoothing filter (unused but plausible)
smoothing_filter = lambda vals, factor=0.8: [vals[0]] + [
    factor * vals[i] + (1 - factor) * vals[i-1] for i in range(1, len(vals))
]

# Core computation with nested logic and distractions
def compute_composite_index(metrics):
    base = sum(metrics)
    adjustment = 0
    
    # Complex conditional adjustments (only one branch matters)
    if len(metrics) > 3:
        pairs = list(combinations(metrics, 2))
        diffs = [abs(a - b) for a, b in pairs]
        max_diff = max(diffs)
        
        if max_diff > 1.5:
            # Real adjustment used
            adjustment = -reduce(lambda acc, x: acc + (x * 0.1), diffs, 0.0)
        else:
            adjustment = 0.5 * min(metrics)
    else:
        adjustment = 0.2 * base
        
    return base + adjustment

# Unused bit manipulation red herring
def scramble_value(n):
    n = ((n << 3) & 0xff) | (n >> 5)
    n ^= 0b10101010
    n = (n + 17) % 256
    return n

# Main scoring function that integrates multiple concepts
def compute_final_score(dataset, weight_map):
    # Step 1: Extract only relevant features
    relevant_scores = extract_relevant_metrics(dataset)
    
    # Step 2: Apply composite index calculation
    composite = compute_composite_index(relevant_scores)
    
    # Step 3: Apply fake normalization (neutral effect)
    normalized = round(composite / len(relevant_scores), 4)
    
    # Step 4: Final scaling (this determines answer)
    scaling_factor = weights['temp'] + weights['humidity']  # 1.0
    final = normalized * (1 + scaling_factor)  # doubles it
    
    # Dead code branches with misleading prints
    if False:
        scrambled = [scramble_value(int(s)) for s in relevant_scores]
        print(f'Debug scrambled: {scrambled}')
    
    if any([r['pressure'] < 1012 for r in dataset]):
        pass  # do nothing, just mislead
    
    return int(round(final))

# Execution flow with irrelevant pre-checks
is_anomalous = analyze_anomalies(data_set)
analysis_log = f"Anomaly status: {is_anomalous}"

# Actual critical execution point
final_score = compute_final_score(data_set, weights)

# Print result as required
print(f"Target result: {final_score}")