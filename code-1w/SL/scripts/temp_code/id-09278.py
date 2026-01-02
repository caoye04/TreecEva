from collections import defaultdict
import math

# Simulated sensor fusion system for autonomous drone navigation
sensor_data = [
    {'id': 'alt1', 'reading': 145.6, 'confidence': 0.88},
    {'id': 'gps2', 'reading': 123.4, 'confidence': 0.91},
    {'id': 'bar3', 'reading': 132.1, 'confidence': 0.76},
    {'id': 'imu4', 'reading': 138.9, 'confidence': 0.82}
]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_X = 0.987
CALIBRATION_OFFSET_Y = -0.013
REFERENCE_BASELINE = 128.0
MAX_SENSITIVITY = 9.81

# Misleading intermediate processing (dead path)
def legacy_normalization(data):
    return [d['reading'] * 0.95 for d in data]

# Unused transformation (red herring)
transform_log = lambda x: math.log(x + 1) if x > 0 else 0

# Simulate historical averages (irrelevant)
historical_averages = defaultdict(float)
for entry in sensor_data:
    key = entry['id'][:3]
    historical_averages[key] += entry['reading'] / len(sensor_data)

# Fake fault detection (distraction)
fault_flags = {}
for i, s in enumerate(sensor_data):
    deviation = abs(s['reading'] - REFERENCE_BASELINE)
    fault_flags[s['id']] = deviation > 20

# Dummy ranking system (misleading side computation)
sorted_by_confidence = sorted(sensor_data, key=lambda x: x['confidence'], reverse=True)
ranks = {item['id']: idx + 1 for idx, item in enumerate(sorted_by_confidence)}

# Weight adjustment based on fake reliability tiers (decoy logic)
reliability_tier = lambda conf: 'A' if conf >= 0.9 else 'B' if conf >= 0.8 else 'C'
tier_multiplier = {'A': 1.05, 'B': 0.98, 'C': 0.92}

# Spurious normalization using unused method
legacy_vals = legacy_normalization(sensor_data)

# Real-time filtering (partially relevant but overcomplicated)
filtered_readings = []
for s in sensor_data:
    adjusted = s['reading']
    if 'gps' in s['id']:
        adjusted *= 1.01
    elif 'imu' in s['id']:
        adjusted *= 0.99
    filtered_readings.append(adjusted)

# Compute dynamic weights based on confidence and tier (actual relevance begins)
metric_weights = {}
for s in sensor_data:
    conf = s['confidence']
    tier = reliability_tier(conf)
    base_weight = conf * tier_multiplier[tier]
    metric_weights[s['id']] = round(base_weight, 4)

# Simulated raw results from different subsystems (mix of relevant/irrelevant)
raw_results = {
    'altitude': 135.2,
    'velocity': 46.7,
    'heading': 312.5,
    'stability': 0.87,
    'power_draw': 18.3
}

# Phantom correlation matrix (completely irrelevant)
correlation_matrix = defaultdict(lambda: defaultdict(float))
keys = list(raw_results.keys())
for i, k1 in enumerate(keys):
    for j, k2 in enumerate(keys):
        correlation_matrix[k1][k2] = round(math.sin(i + j + 1), 3)

# Fake entropy calculation (distraction)
entropy = 0.0
for val in raw_results.values():
    if val > 0:
        prob = val / sum(raw_results.values())
        entropy -= prob * math.log(prob)

# Actual performance evaluation logic (critical path)
def evaluate_performance(weights, results):
    # Extract altitude-related sensors only (key insight)
    alt_related = ['alt1', 'bar3']
    
    # Compute weighted average of corrected sensor readings
    total_weight = 0.0
    weighted_sum = 0.0
    
    for entry in sensor_data:
        sid = entry['id']
        if sid in alt_related:  # Only these contribute
            corr_reading = entry['reading']
            if sid == 'alt1':
                corr_reading *= 1.02  # Minor correction
            elif sid == 'bar3':
                corr_reading *= 0.98
            weight = weights[sid]
            weighted_sum += corr_reading * weight
            total_weight += weight
    
    estimated_altitude = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Compare with reported altitude from results
    reported_alt = results['altitude']
    error = abs(reported_alt - estimated_altitude)
    
    # Inverse error scoring with cap
    base_score = 1000.0 / (1 + error) if error < 100 else 0
    
    # Apply combinatorics-based precision bonus
    # Number of valid altitude sources used
    n_sources = len([s for s in sensor_data if s['id'] in alt_related and s['confidence'] > 0.75])
    bonus_factor = math.comb(4, n_sources) if n_sources <= 4 else 1  # max 4 choose n
    
    # Final nonlinear transformation
    final_score = int(base_score * bonus_factor * 0.75)  # Deterministic integer
    
    # Dead code branch (misdirection)
    if final_score > 5000:
        final_score = 5000  # Never reached
    
    return final_score

# Execute critical statement
final_score = evaluate_performance(metric_weights, raw_results)

# Print result as required
print(f"Target result: {final_score}")