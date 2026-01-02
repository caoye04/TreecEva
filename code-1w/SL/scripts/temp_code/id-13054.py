from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis

def collect_readings():
    # Real data source (simplified)
    raw_streams = {
        'sensor_a': [23.4, 25.1, 22.7, 24.8, 26.0, 23.9],
        'sensor_b': [19.5, 20.1, 18.9, 21.2, 20.8, 19.7],
        'sensor_c': [31.6, 33.2, 30.4, 32.1, 34.0, 31.8]
    }
    return raw_streams

def filter_outliers(data, limit=30.0):
    # Irrelevant filtering for high values (distractor)
    cleaned = {}
    for k, v in data.items():
        cleaned[k] = [x for x in v if x <= limit]
    return cleaned

def compute_rolling_average(values, window=2):
    # Used in processing path
    averages = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

def generate_checksum(label: str) -> int:
    # Dead function - never used in main logic (red herring)
    return sum(ord(c) * (i + 1) for i, c in enumerate(label)) % 1000

def decode_signal(sequence: list) -> dict:
    # Misleading signal decoding with bit manipulation (irrelevant)
    result = {}
    for idx, val in enumerate(sequence):
        shifted = int(val * 10) ^ 255  # XOR with magic number
        result[f'node_{idx}'] = shifted & 0xFF
    return result

def normalize_readings(streams):
    # Normalize each sensor to zero mean (partially relevant)
    normalized = {}
    for key, readings in streams.items():
        mean_val = sum(readings) / len(readings)
        norm_vals = [round(r - mean_val, 2) for r in readings]
        normalized[key] = norm_vals
    return normalized

def extract_features(data_map):
    # Extract statistical features (used)
    features = defaultdict(dict)
    for sensor, values in data_map.items():
        features[sensor]['mean'] = round(sum(values) / len(values), 3)
        features[sensor]['variance'] = round(sum((x - features[sensor]['mean'])**2 for x in values) / len(values), 3)
        features[sensor]['peak'] = max(values)
        features[sensor]['energy'] = sum(x**2 for x in values)
    return features

def evaluate_stability(metric_log):
    # Complex stability heuristic with decoy logic
    scores = {}
    for node, metrics in metric_log.items():
        base_score = 50
        if metrics['variance'] < 1.0:
            base_score += 20
        elif metrics['variance'] < 2.5:
            base_score += 10
        else:
            base_score -= 15

        if metrics['peak'] > 5.0:
            penalty = int(metrics['peak'])
            base_score -= min(penalty, 25)

        # Dead branch - never reached due to structure (distractor)
        if 'debug_flag' in globals() and debug_flag:
            base_score = apply_manual_override(base_score)

        scores[node] = max(base_score, 0)
    return scores

def apply_manual_override(value):  # Unused function
    return (value * 2) ^ 123

def build_threshold_map(criteria_set):
    # Create dynamic thresholds (actually used)
    t_map = defaultdict(float)
    t_map['critical'] = criteria_set['mean'] * 2.3
    t_map['warning'] = criteria_set['mean'] * 1.6
    t_map['decay_factor'] = 0.85 if criteria_set['energy'] > 100 else 0.65
    return t_map

def simulate_propagation(delays):
    # Irrelevant network delay simulation (distractor)
    total = 0.0
    for d in delays:
        total += math.sin(d) * math.cos(d + 1.5)
    return round(total * 1000, 4)

def analyze_readings(features, thresholds):
    # Core diagnostic logic
    diagnostics = []
    for sensor, feats in features.items():
        crit = thresholds['critical']
        warn = thresholds['warning']
        decay = thresholds['decay_factor']

        # Primary decision chain
        if feats['mean'] > crit:
            severity = 3
        elif feats['mean'] > warn:
            severity = 2
        else:
            severity = 1

        # Secondary condition with bitwise logic (relevant)
        energy_flag = int(feats['energy'] > 200)
        variance_flag = int(feats['variance'] > 2.0)
        combined_flag = energy_flag << 1 | variance_flag  # Bit packing

        # Tertiary adjustment
        adjusted_severity = severity
        if combined_flag == 3:  # Both flags set
            adjusted_severity += 1
        elif combined_flag == 1:
            adjusted_severity = max(adjusted_severity - 1, 1)

        # Mapping to diagnostic code
        code = (adjusted_severity * 100) + (combined_flag * 10) + len(sensor)
        diagnostics.append(code)

    # Final aggregation
    final_code = sum(diagnostics) * int(thresholds['decay_factor'] * 100)
    return final_code

# --- Execution Flow ---
if __name__ == "__main__":
    # Step 1: Collect raw data
    raw_data = collect_readings()

    # Step 2: Normalize readings (relevant)
    normalized_data = normalize_readings(raw_data)

    # Step 3: Extract statistical features (relevant)
    feature_set = extract_features(normalized_data)

    # Step 4: Evaluate stability (partially distractor - result unused)
    stability_scores = evaluate_stability(feature_set)

    # Step 5: Build threshold map using first sensor as reference (key)
    reference_sensor = feature_set['sensor_a']
    threshold_map = build_threshold_map(reference_sensor)

    # Step 6: Analyze all readings against thresholds (final step)
    final_diagnostic = analyze_readings(feature_set, threshold_map)

    # Step 7: Print result
    print(f"Result: {final_diagnostic}")

    # Irrelevant computations below (dead code paths)
    processed_data = {}
    for k, v in raw_data.items():
        processed_data[k] = compute_rolling_average(v)

    signal_codes = decode_signal([23.4, 19.5, 31.6])

    network_latency = simulate_propagation([1.2, 0.8, 1.5, 2.1])

    checksum_a = generate_checksum('sensor_a')
    checksum_b = generate_checksum('sensor_b')
