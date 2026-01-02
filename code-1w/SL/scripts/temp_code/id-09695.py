from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation
def collect_sensor_data(nodes):
    readings = defaultdict(list)
    for node_id in range(nodes):
        for _ in range(5):
            readings[node_id].append((node_id * 2.5) + len(readings))
    return readings

def generate_baseline():
    base = {}
    for i in range(8):
        base[f'sensor_{i}'] = (i % 3 + 1) * 17.3
    return base

def compute_entropy(data_list):
    counts = Counter(data_list)
    total = len(data_list)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def analyze_pattern(sequence):
    # Irrelevant pattern matcher (dead-end logic)
    transitions = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i+1]:
            transitions += 1
    trend_score = sum(sequence) / (transitions + 1) if transitions else 0
    return trend_score  # Not used in final calculation

def evaluate_stability(metrics):
    stability = 0
    for val in metrics:
        if val > 20:
            stability += math.sqrt(val) * 0.8
        else:
            stability -= val * 0.1
    return stability

def extract_features(raw_data):
    features = []
    for key in sorted(raw_data.keys()):
        segment = raw_data[key]
        avg = sum(segment) / len(segment)
        peak = max(segment)
        entropy_val = compute_entropy([round(x) for x in segment])
        features.append((avg, peak, entropy_val))
    return features

def filter_outliers(data_tuples):
    cleaned = []
    for item in data_tuples:
        if item[0] > 5 and item[1] < 30:  # Arbitrary filtering (partially used)
            cleaned.append(item)
    return cleaned

def derive_health_index(feature_set):
    index = 0.0
    for i, (avg, peak, entropy_val) in enumerate(feature_set):
        contribution = avg * (1 + entropy_val / 10)
        if i % 2 == 0:
            index += contribution
        else:
            index -= contribution * 0.5
    return round(index, 3)

def validate_consistency(checksums):
    # Decoy validation function with no impact
    valid_count = 0
    for cs in checksums:
        temp = cs
        while temp > 1:
            temp /= 2
        if temp <= 1.5:
            valid_count += 1
    return valid_count > 3

def compile_diagnostics(feature_vec):
    report = defaultdict(float)
    magnitudes = [f[0] for f in feature_vec]
    total_mag = sum(magnitudes)
    report['total_power'] = total_mag
    report['complexity_factor'] = compute_entropy([int(x) for x in magnitudes])
    report['stability_metric'] = evaluate_stability(magnitudes)
    return report

def process_metrics(signature, baseline):
    # Core processing path
    fused_data = []
    for i, sig_val in enumerate(signature):
        key = f'sensor_{i % 8}'
        base_val = baseline[key]
        adjusted = (sig_val[0] * 1.2) - (base_val * 0.85)
        fused_data.append(adjusted)
    
    # Secondary transformations
    transformed = [math.log(abs(x) + 1) * 1.5 for x in fused_data]
    
    # Red herring: circular dependency check (unused)
    cyclic_sum = 0
    for j in range(len(transformed)):
        cyclic_sum += transformed[j] * transformed[(j+2) % len(transformed)]
    
    # Final integration
    aggregate = sum(transformed) * 0.75
    penalty = len([x for x in fused_data if x < 0]) * 2.3
    final_score = aggregate - penalty
    
    # Misleading intermediate
    diagnostic_flag = 'WARNING' if final_score < 10 else 'NORMAL'
    
    # Actual answer carrier
    final_diagnostic = int(round(final_score * 2.6))
    
    # Dead code branch (never executed)
    if False:
        backup_system = {"status": "inactive", "value": sum(fused_data) / len(fused_data)}
        return backup_system['value']
    
    return final_diagnostic

# Main execution flow
sensor_network = collect_sensor_data(8)
baseline_readings = generate_baseline()

# Extract time-series features
raw_features = extract_features(sensor_network)

# Filter spurious detections
filtered_features = filter_outliers(raw_features)

# Derive system health signature
health_signature = filtered_features  # Pass through after filtering

# Compute auxiliary metrics (distractors)
diag_report = compile_diagnostics(health_signature)
trend_analysis = analyze_pattern([f[0] for f in health_signature])
system_index = derive_health_index(health_signature)

# Validate dummy consistency (no effect)
consistency_check = validate_consistency([diag_report['stability_metric']])

# Critical statement
final_diagnostic = process_metrics(health_signature, baseline_readings)

print(f"Result: {final_diagnostic}")