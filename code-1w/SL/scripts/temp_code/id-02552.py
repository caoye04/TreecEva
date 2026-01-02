import math

# Simulated telemetry data from a distributed sensor network
def generate_telemetry(seed=42):
    return [(i * seed + hash(str(i)) % 100) % 800 for i in range(30)]

# Irrelevant utility: converts numeric level to categorical label (never used)
def level_to_category(level):
    if level < 200:
        return 'LOW'
    elif level < 500:
        return 'MEDIUM'
    else:
        return 'HIGH'

# Decoy function: appears useful but unused in critical path
def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

# Core processing pipeline

def analyze_anomalies(raw_readings):
    anomalies = []
    baseline = sum(raw_readings[:10]) // 10
    
    # Misleading intermediate calculation (partial and unused)
    temp_offset = 0
    for val in raw_readings[:5]:
        temp_offset += (val % 17) * 2
    temp_offset = temp_offset // 5 if temp_offset > 100 else baseline
    
    # Actual anomaly detection
    for i, reading in enumerate(raw_readings):
        if i == 0:
            continue
        diff = abs(reading - raw_readings[i-1])
        if diff > 50 and reading > 300:
            anomalies.append(diff * 1.1)
    
    # Dead code path - unreachable due to prior logic
    if len(anomalies) > 100:
        anomalies = anomalies[:50]
    
    return anomalies


def extract_features(signal_data):
    # Signal windowing with slicing
    window_size = 6
    windows = [signal_data[i:i+window_size] for i in range(0, len(signal_data), window_size)]
    
    # Extract peak-to-peak amplitude per window
    features = []
    for win in windows:
        if len(win) < 3:
            continue
        peak_high = max(win)
        peak_low = min(win)
        swing = peak_high - peak_low
        if swing > 400:  # Filter significant oscillations
            features.append(swing * 0.85)
    
    # Distractor: complex but unused transformation
    transformed = [math.cos(math.radians(x % 90)) for x in signal_data]
    avg_transform = sum(transformed) / len(transformed)
    
    return features


def validate_integrity(check_sequence, threshold=0.75):
    # Compute running checksums using modular arithmetic
    checksums = []
    running_sum = 0
    
    for i, val in enumerate(check_sequence):
        running_sum = (running_sum + val * (i + 1)) % 1024
        if i % 4 == 0:
            checksums.append(running_sum)
    
    # Determine integrity score
    valid_checks = sum(1 for c in checksums if c > 200)
    score = valid_checks / len(checksums) if checksums else 0
    
    return score >= threshold


def aggregate_diagnostics(feature_set, anomaly_set):
    # Initialize diagnostic dictionary with red herrings
    diagnostics = {
        'baseline_stability': True,
        'noise_floor': 42.0,
        'spike_count': len(anomaly_set),
        'total_energy': 0,
        'distortion_index': 0.0
    }
    
    energy = 0
    for f in feature_set:
        energy += f ** 0.5
    
    diagnostics['total_energy'] = int(energy)
    
    # Conditional early return that is never triggered due to data properties
    if len(feature_set) == 0 and len(anomaly_set) == 0:
        diagnostics['distortion_index'] = -1
        return diagnostics
    
    # Real distortion calculation
    if len(anomaly_set) > 0:
        avg_anomaly = sum(anomaly_set) / len(anomaly_set)
        diagnostics['distortion_index'] = round(avg_anomaly * 0.37, 4)
    else:
        diagnostics['distortion_index'] = 0.12
    
    return diagnostics


def process_metrics(snapshot, load_profile):
    # Complex control flow with nested conditions
    if not snapshot or len(snapshot) < 15:
        return -999
    
    # Primary analysis branches
    anomalies = analyze_anomalies(snapshot)
    features = extract_features(snapshot)
    
    # Validate only if system load permits
    if load_profile.get('cpu_peak', 0) > 90:
        if not validate_integrity(snapshot[::2]):  # Use every other reading
            return -888
    
    # Aggregation with dictionary unpacking distraction
    raw_diagnostics = aggregate_diagnostics(features, anomalies)
    
    # Final computation chain
    base_score = raw_diagnostics['distortion_index'] * 100
    adjustment = len(features) * 3
    if raw_diagnostics['spike_count'] > 2:
        adjustment += 5
    
    # Critical execution point
    final_diagnostic = int(base_score) + adjustment
    
    # Dead code - result already computed
    if final_diagnostic > 500:
        final_diagnostic = 500 + (final_diagnostic % 100)
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Generate realistic input data
    data_snapshot = generate_telemetry()
    
    # System load profile with irrelevant fields
    system_load = {
        'cpu_avg': 76.2,
        'cpu_peak': 94,
        'memory_usage': 81,
        'disk_io': 120,
        'network_latency': 45
    }
    
    # Unused data structures to increase interference
    historical_stats = {
        'previous_cycles': [67, 89, 91, 77],
        'error_counts': {k: 0 for k in ['A', 'B', 'C']},
        'last_reset': '2023-11-05'
    }
    
    # Key statement
    final_diagnostic = process_metrics(data_snapshot, system_load)
    
    # Output result
    print(f"Target result: {final_diagnostic}")