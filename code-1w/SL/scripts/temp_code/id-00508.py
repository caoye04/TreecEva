def analyze_system_load(usage_log):
    peak_load = max(usage_log)
    avg_load = sum(usage_log) / len(usage_log)
    normalized = [(x - avg_load) / avg_load for x in usage_log]
    volatility = sum(abs(normalized[i] - normalized[i-1]) for i in range(1, len(normalized)))
    return {'peak': peak_load, 'average': avg_load, 'volatility': volatility}

# Irrelevant helper (decoy)
def calculate_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    return -sum((count/total) * log(count/total) for count in freq.values())

# Distractor function with unused logic
def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val * (i + 1)) % 256
    return checksum

# Simulated sensor readings (irrelevant to final result)
sensor_data = [14, 18, 22, 19, 25, 30, 28, 20, 17, 15]
load_profile = analyze_system_load(sensor_data)
entropy_value = calculate_entropy([1,2,2,3,3,3])  # Dead computation

# Core logic disguised among distractors
def process_metrics(raw):
    processed = {}
    for k, v in raw.items():
        if k == 'peak':
            processed['efficiency'] = 100 - v
        elif k == 'average':
            processed['stability'] = 50 + (30 - v)
        elif k == 'volatility':
            processed['consistency'] = 100 - int(v * 10)
    return processed

metrics = process_metrics(load_profile)

# Unused but misleading intermediate calculation
temp_analysis = [x * 0.85 for x in sensor_data if x > 20]
adjusted_total = sum(temp_analysis)  # Red herring

# Weight configuration (some weights are decoys)
weights = {
    'efficiency': 0.4,
    'stability': 0.3,
    'consistency': 0.3,
    'redundancy': 0.0,  # Dead weight
    'fallback_metric': 0.0   # Another red herring
}

# Main evaluation function
def evaluate_performance(met, wgt):
    score = 0.0
    for key in met:
        if key in wgt and wgt[key] > 0:  # Filter out zero-weighted keys
            score += met[key] * wgt[key]
    
    # Additional logic that seems important but isn't used
    if 'diagnostic' in met:
        score += 10  # Never executed
    
    # Final adjustment based on arbitrary threshold
    if score > 75:
        score *= 0.95  # Mild penalty
    else:
        score *= 1.05
    
    # This branch is unreachable due to data flow, but looks relevant
    for k in wgt:
        if 'backup' in k:
            score += 5  # Dead code path
    
    return round(score, 4)

# Execute main logic
evaluation_trace = []  # Unused logging structure
event_marker = 'PHASE_2'  # Misleading flag

final_score = evaluate_performance(metrics, weights)

# Print required output
print(f"Target result: {final_score}")