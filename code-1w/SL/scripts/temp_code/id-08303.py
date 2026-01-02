import itertools

# System telemetry processing simulation with diagnostic evaluation

def preprocess_signal(raw_data, threshold=0.75):
    filtered = [x for x in raw_data if abs(x) > threshold]
    return [round(x * 1.25, 6) for x in filtered]

def generate_combinations(elements, r=2):
    # Irrelevant utility: generates combinations but not used in final path
    return list(itertools.combinations(elements, r))

def detect_anomalies(signal_sequence):
    anomalies = []
    for i in range(1, len(signal_sequence)):
        if signal_sequence[i] < signal_sequence[i-1] and (signal_sequence[i] + signal_sequence[i-1]) % 2 == 1:
            anomalies.append(i)
    return anomalies

def calculate_entropy(values):
    # Distractor function: looks important but unused
    from math import log2
    frequency = {}
    for v in values:
        frequency[v] = frequency.get(v, 0) + 1
    total = len(values)
    entropy = -sum((freq/total) * log2(freq/total) for freq in frequency.values())
    return round(entropy, 6)

def normalize_vector(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [round(x / magnitude, 6) for x in vec] if magnitude else vec

def evaluate_stability(readings):
    # Complex but partially dead logic
    if len(readings) < 3:
        return 0.0
    trend_scores = []
    for i in range(2, len(readings)):
        score = (readings[i] - readings[i-1]) * (readings[i-1] - readings[i-2])
        trend_scores.append(score)
    stability = sum(1 for s in trend_scores if s <= 0) / len(trend_scores)
    return round(stability * 100, 4)

def aggregate_metrics(signals, flags):
    base_score = sum(abs(s) for s in signals)
    flag_penalty = 0
    
    # Multi-level conditional decoy
    if len(flags) > 5:
        flag_penalty += 10
    elif any(f == 'CRITICAL' for f in flags):
        flag_penalty += 25
    else:
        temp_sum = 0
        for f in flags:
            temp_sum += hash(f) % 7  # Red herring computation
        flag_penalty += temp_sum // 3
    
    # Real contribution to answer
    adjustment_factor = 0.87
    if 'CALIBRATED' in flags and len(signals) % 2 == 0:
        adjustment_factor *= 1.15
    
    intermediate = base_score * adjustment_factor - flag_penalty
    
    # Additional noise
    diagnostics = {
        'peak_count': len([s for s in signals if s > 1.0]),
        'inversion_rate': evaluate_stability(signals),
        'anomaly_trace': detect_anomalies(signals)
    }
    
    # Final result obscured by irrelevant dictionary entries
    final_value = int(round(intermediate + 42))
    return final_value

# Simulated sensor inputs and system state
raw_telemetry = [0.12, 0.81, -0.33, 1.05, 0.67, -1.42, 0.93, 0.08, -0.21, 1.11]
dummy_labels = ['A', 'B', 'C', 'D', 'E']

# Unused but plausible-looking preprocessing
combinations = generate_combinations(dummy_labels, 3)
entropy_metric = calculate_entropy([1, 2, 2, 3, 3, 3, 4, 4, 5])

# Actual signal pipeline
processed_signal = preprocess_signal(raw_telemetry)
normalized_signals = normalize_vector(processed_signal)

# System status flags with red herrings
system_flags = [
    'INIT_OK', 'SENSOR_WARM', 'CALIBRATED',
    'VOLTAGE_FLUX', 'CACHE_PRIMED', 'TASK_IDLE',
    'DEBUG_MODE'
]

# Dead code path: complex but unused stability analysis
stability_index = evaluate_stability([0.5, 0.7, 0.6, 0.8, 0.9, 0.7, 0.65])
anomaly_locations = detect_anomalies(processed_signal)

# Key statement — target of the question
final_diagnostic = aggregate_metrics(normalized_signals, system_flags)

# Output requirement
print(f"Result: {final_diagnostic}")