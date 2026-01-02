from itertools import combinations
from math import log, ceil

# Simulated system performance metrics (irrelevant in part)
sensor_data = [0.87, 0.93, 0.76, 0.88, 0.91]

def analyze_sensor_noise(data):
    noise_level = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            noise_level += (1 - val) * 0.5
        else:
            noise_level += (val - 0.5) * 0.3
    return round(noise_level, 4)

# Irrelevant helper: computes theoretical bandwidth (not used in final result)
def calc_bandwidth(channels, freq, mod_level=2):
    bw = channels * freq * log(mod_level, 2)
    adjustment = 0
    for c in range(1, channels+1):
        adjustment += bw / (c + 1)
    return bw + adjustment

# Real-time processing efficiency (some values are decoys)
efficiency_log = {
    't1': {'load': 78, 'cycles': 100, 'util': 0.78},
    't2': {'load': 85, 'cycles': 100, 'util': 0.85},
    't3': {'load': 64, 'cycles': 100, 'util': 0.64},
    't4': {'load': 92, 'cycles': 100, 'util': 0.92}
}

# Unused function - red herring
def detect_anomalies(logs):
    anomalies = []
    for t_id, data in logs.items():
        if data['util'] < 0.7 or data['load'] > 90:
            anomalies.append(t_id)
    return anomalies

# Core weight calibration (partially relevant)
basis_weights = [0.1, 0.2, 0.3, 0.25]
temp_offset = sum(basis_weights) * 0.15

# Introduce distraction via set operations (irrelevant to final path)
duplicate_indices = {1, 2, 3}
valid_indices = {0, 1, 2, 3, 4}
available_indices = valid_indices - duplicate_indices

# Auxiliary transformation (unused but plausible)
shifted_weights = [w + temp_offset for w in basis_weights]

# Primary metric evaluation with distractors
metrics = [
    len(efficiency_log),                    # count of tasks
    analyze_sensor_noise(sensor_data),      # noise score
    sum(d['load'] for d in efficiency_log.values()) / len(efficiency_log),  # avg load
    max(d['util'] for d in efficiency_log.values()),                      # peak utilization
    len(list(combinations(efficiency_log.keys(), 2)))                     # pair combinations
]

# Weights - only first four matter; fifth is a red herring
weights = [
    0.25,
    0.15,
    0.20,
    0.30,
    0.10  # This weight corresponds to unused combinatorial metric
]

# Distractor: normalize weights (but not actually used)
norm_factor = sum(weights)
normalized_weights = [w / norm_factor for w in weights]

# Actual scoring logic buried among distractions
def evaluate_performance(mets, wts):
    # Only use first 4 metrics and weights
    core_mets = mets[:4]
    core_wts = wts[:4]
    
    # Apply non-linear boost to high utilizations
    adjusted_mets = []
    for idx, val in enumerate(core_mets):
        if idx == 3 and val > 0.8:  # peak util condition
            adjusted_mets.append(val * 1.1)
        else:
            adjusted_mets.append(val)
    
    # Weighted sum
    score = sum(m * w for m, w in zip(adjusted_mets, core_wts))
    
    # Additional logic: bonus if avg load < 80 and noise < 0.2
    if core_mets[2] < 80 and core_mets[1] < 0.2:
        score += 0.05
    
    # Penalty if task count odd
    if int(core_mets[0]) % 2 == 1:
        score -= 0.02
    
    return round(score * 100, 6)  # scale to integer-like precision

# Dead code path - never called
if __name__ == "__main__":
    print("Debug mode inactive")

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Target result: {final_score}")