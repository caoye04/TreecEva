from collections import defaultdict, Counter
from itertools import zip_longest, cycle

# Simulated sensor fusion system with weighted reliability scoring
def analyze_sensor_data(logs):
    raw_readings = [x['value'] for x in logs if x['status'] == 'OK']
    error_count = sum(1 for x in logs if x['status'] != 'OK')
    
    # Irrelevant aggregation (distractor)
    status_freq = Counter(x['status'] for x in logs)
    avg_latency = sum(x.get('latency', 0) for x in logs) / len(logs) if logs else 0

    # Core processing: frequency of readings by source (red herring)
    source_data = defaultdict(list)
    for entry in logs:
        source_data[entry['source']].append(entry['value'])
    
    # Misleading statistical summary
    outlier_flags = {}
    for src, vals in source_data.items():
        mean_val = sum(vals) / len(vals)
        outlier_flags[src] = sum(1 for v in vals if abs(v - mean_val) > 30)

    # Actual signal extraction path
    filtered_readings = [v for v in raw_readings if 50 < v < 300]
    reading_bins = [0]*10
    for v in filtered_readings:
        bin_idx = (v - 51) // 25
        if 0 <= bin_idx < 10:
            reading_bins[bin_idx] += 1

    # Weight assignment based on bin density (core logic)
    weights = []
    for count in reading_bins:
        if count == 0:
            weights.append(0.1)
        elif count < 3:
            weights.append(0.5)
        else:
            weights.append(1.8 + count * 0.2)  # Increasing confidence

    # Dead code path - never used (decoy)
    def adjust_weights_dynamically(w):
        return [max(0.05, x * 0.9) for x in w]
    
    # Critical transformation: smooth and normalize
    smoothed = []
    for i in range(len(weights)):
        neighbor_avg = sum(
            weights[j] for j in range(max(0, i-1), min(len(weights), i+2))
        ) / (3 if 0 < i < len(weights)-1 else (2 if len(weights) > 1 else 1))
        smoothed.append(round(neighbor_avg * 0.85, 4))

    # Determine active regions using thresholding
    activation_threshold = 0.7
    active_mask = [1 if w > activation_threshold else 0 for w in smoothed]
    
    # Use enumerate to find active indices (key python idiom)
    active_indices = [i for i, is_active in enumerate(active_mask) if is_active]
    
    # Secondary filter: only trust alternating pattern compliance
    pattern_compliant = []
    for i in active_indices:
        neighbors_active = 0
        if i > 0 and active_mask[i-1]:
            neighbors_active += 1
        if i < len(active_mask)-1 and active_mask[i+1]:
            neighbors_active += 1
        pattern_compliant.append(neighbors_active % 2 == 0)  # Prefer isolated peaks
    
    final_candidates = [
        idx for idx, compliant in zip(active_indices, pattern_compliant) if compliant
    ]
    
    # Final weight selection uses only first compliant candidate
    final_weights = [smoothed[i] for i in final_candidates]
    
    # Decoy list comprehensions (irrelevant)
    magnitude_classes = ["low", "medium", "high"]
    class_map = {i: mag for i, mag in enumerate(cycle(magnitude_classes))}

    # Scaling factor computed from log metadata (partially relevant)
    valid_sources = set(entry['source'] for entry in logs if entry['status'] == 'OK')
    source_risk_score = defaultdict(int)
    for src in valid_sources:
        source_risk_score[src] = len(src) % 3  # Arbitrary risk heuristic
    
    base_factor = len(valid_sources) * 0.75
    adjustment = sum(source_risk_score.values()) * 0.1
    scaling_factor = round(base_factor - adjustment, 3)
    
    # TRIGGER STATEMENT: this is the critical execution point
    if final_weights:
        threshold_balance = final_weights[active_indices[0]] * scaling_factor
    else:
        threshold_balance = -1
    
    # Unused debug print (dead code distractor)
    # print(f'Debug - Bins: {reading_bins}, Weights: {weights}')
    
    # Output required result
    print(f'Target result: {threshold_balance}')

# Input data setup
sensor_logs = [
    {'source': 'SRC_A1', 'value': 65, 'status': 'OK', 'latency': 12},
    {'source': 'SRC_B2', 'value': 78, 'status': 'OK', 'latency': 15},
    {'source': 'SRC_C3', 'value': 85, 'status': 'ERROR', 'latency': 20},
    {'source': 'SRC_A1', 'value': 92, 'status': 'OK', 'latency': 10},
    {'source': 'SRC_B2', 'value': 110, 'status': 'OK', 'latency': 14},
    {'source': 'SRC_C3', 'value': 125, 'status': 'OK', 'latency': 18},
    {'source': 'SRC_A1', 'value': 130, 'status': 'OK', 'latency': 11},
    {'source': 'SRC_B2', 'value': 145, 'status': 'OK', 'latency': 16},
    {'source': 'SRC_C3', 'value': 160, 'status': 'OK', 'latency': 19},
    {'source': 'SRC_A1', 'value': 175, 'status': 'OK', 'latency': 13},
    {'source': 'SRC_B2', 'value': 190, 'status': 'OK', 'latency': 17},
    {'source': 'SRC_C3', 'value': 205, 'status': 'OK', 'latency': 21},
    {'source': 'SRC_A1', 'value': 220, 'status': 'OK', 'latency': 14},
    {'source': 'SRC_B2', 'value': 240, 'status': 'OK', 'latency': 18},
    {'source': 'SRC_C3', 'value': 260, 'status': 'OK', 'latency': 22},
    {'source': 'SRC_A1', 'value': 280, 'status': 'OK', 'latency': 16},
    {'source': 'SRC_B2', 'value': 295, 'status': 'OK', 'latency': 20},
    {'source': 'SRC_C3', 'value': 310, 'status': 'OK', 'latency': 24},
    {'source': 'SRC_A1', 'value': 330, 'status': 'OK', 'latency': 18},
]

# Execute
analyze_sensor_data(sensor_logs)