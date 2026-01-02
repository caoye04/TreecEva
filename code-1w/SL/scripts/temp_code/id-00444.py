import itertools

# Simulated sensor data processing with performance evaluation
raw_readings = [145, 267, 98, 412, 331, 89, 256, 112]
threshold = 100
calibration_factor = 0.87

# Irrelevant transformation: normalize readings (not used in final logic)
normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 3) for x in raw_readings]

# Key filtered dataset based on threshold
valid_readings = [x for x in raw_readings if x > threshold]

# Decoy statistical calculation
mean_deviation = sum(abs(x - sum(raw_readings)/len(raw_readings)) for x in raw_readings) / len(raw_readings)

# Signal encoding using bit manipulation (mixed relevance)
encoded_signals = []
for val in valid_readings:
    encoded = (val << 2) ^ 0xA5  # Bit shift and XOR obfuscation
    if encoded % 3 == 0:
        encoded = (encoded >> 1) + 7
    encoded_signals.append(encoded)

# Dead-end function: looks important but unused
def analyze_trend(data):
    trend_vector = []
    for i in range(1, len(data)):
        trend_vector.append(1 if data[i] > data[i-1] else -1)
    return sum(trend_vector)

# Another red herring: complex string-based checksum
status_log = "SYS_OK, SENSOR_2HOT, SYS_OK, FAN_RISING"
log_codes = dict(zip(['SYS_OK', 'SENSOR_2HOT', 'FAN_RISING'], [1, -1, 2]))
checksum = sum(log_codes.get(token.strip(), 0) * (i + 1) for i, token in enumerate(status_log.split(',')))

# Generate combinatorial feature space (some elements are relevant)
feature_pairs = list(itertools.combinations([x % 50 for x in valid_readings], 2))
feature_scores = []
for a, b in feature_pairs:
    score = (a ** 2 - b) * calibration_factor
    if score > 200:
        score = 200  # cap
    feature_scores.append(int(score))

# Weight assignment with decoy structure
weights = {
    'amplitude': 0.4,
    'stability': 0.3,
    'rarity': 0.2,
    'legacy_boost': 0.1,  # deprecated weight
    'fallback_mode': 0.0   # dead weight
}

# Metric data construction — only 'amplitude', 'stability', 'rarity' matter
base_amplitude = sum(valid_readings) / 100
fluctuation_index = sum(1 for i in range(1, len(valid_readings)) if valid_readings[i] != valid_readings[i-1])
stability_metric = (len(valid_readings) - fluctuation_index) / len(valid_readings)
rare_count = len([x for x in valid_readings if x > 400])
rarity_metric = rare_count / len(valid_readings) if valid_readings else 0

metric_data = {
    'amplitude': base_amplitude,
    'stability': stability_metric,
    'rarity': rarity_metric,
    'debug_flag': False,
    'version': '2.1a'
}

# Unused lambda — distraction
diff_filter = lambda f_list: [f for f in f_list if f > 50]

# Core evaluation logic (uses only specific keys from weights)
def evaluate_performance(metrics, weight_map):
    total = 0.0
    effective_weights = {k: v for k, v in weight_map.items() if k in ['amplitude', 'stability', 'rarity']}
    weight_sum = sum(effective_weights.values())
    
    for key in effective_weights:
        if key == 'amplitude':
            total += metrics['amplitude'] * effective_weights[key]
        elif key == 'stability':
            total += (metrics['stability'] * 100) * effective_weights[key]
        elif key == 'rarity':
            bonus = 25 if metrics['rarity'] > 0 else 10
            total += bonus * effective_weights[key]
    
    # Apply non-linear adjustment based on encoded signal entropy
    unique_encoded = set(encoded_signals)
    entropy_factor = len(unique_encoded) / len(encoded_signals) if encoded_signals else 0
    total *= (1 + entropy_factor * 0.1)
    
    # Final clamping
    return int(max(0, min(total, 1000)))

# Critical execution point
final_score = evaluate_performance(metric_data, weights)

# Output result as required
print(f"Target result: {final_score}")