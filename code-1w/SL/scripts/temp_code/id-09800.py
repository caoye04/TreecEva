from collections import defaultdict, Counter
import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(100):
        raw_val = (i * 7 + 13) % 89
        normalized = (raw_val / 89.0) * 100
        category = 'temp' if i % 3 == 0 else 'voltage' if i % 3 == 1 else 'current'
        signals.append({'id': i, 'value': normalized, 'type': category, 'timestamp': 1623456000 + i * 10})
    return signals

# Irrelevant auxiliary function – distractor
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def analyze_pattern(seq):
    # Unused pattern analyzer – dead code path
    counts = Counter(seq)
    entropy = 0
    total = len(seq)
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core processing pipeline
def extract_signal_windows(data, window_size=5):
    windows = []
    for i in range(0, len(data) - window_size + 1, window_size):
        window = data[i:i+window_size]
        avg_val = sum(item['value'] for item in window) / window_size
        dominant_type = Counter(item['type'] for item in window).most_common(1)[0][0]
        stability_score = 100 - abs(avg_val - 50)  # Centered around 50
        windows.append({
            'center_id': data[i + window_size // 2]['id'],
            'average': avg_val,
            'stability': stability_score,
            'type': dominant_type
        })
    return windows

def filter_anomalies(windows, threshold=75):
    anomalies = []
    high_risk_ids = []  # Distractor: collected but unused later
    for w in windows:
        if w['stability'] < threshold:
            anomalies.append(w)
            if w['average'] > 60:
                high_risk_ids.append(w['center_id'])  # Dead assignment
    # Additional distraction: bitwise manipulation with no impact
    masked_count = len(anomalies) ^ 15 & 255
    return anomalies

# Misleading diagnostic chain
def compute_health_factor(anomalies):
    base_score = 1000
    adjustment = 0
    for a in anomalies:
        if a['type'] == 'temp':
            adjustment += 5
        elif a['type'] == 'voltage':
            adjustment -= 3
        else:
            adjustment += 2
    # Complex-looking but irrelevant transformation
    transformed = int((base_score - adjustment) * 0.95) | 1024
    checksum = sum(transformed.to_bytes(2, 'little'))
    return base_score - adjustment  # Only this matters

# Real processing logic buried under distractions
def aggregate_diagnostics(telemetry):
    # Step 1: Extract temporal windows
    windows = extract_signal_windows(telemetry)
    
    # Step 2: Filter unstable segments
    unstable = filter_anomalies(windows, threshold=70)
    
    # Step 3: Compute health metric
    health = compute_health_factor(unstable)
    
    # Step 4: Generate frequency stats – looks important but not used in final result
    type_sequence = [w['type'] for w in windows]
    freq_map = defaultdict(int)
    for t in type_sequence:
        freq_map[t] += 1
    
    # Step 5: Apply decay model on unused data
    decayed_weights = [freq_map[t] * 0.9 ** i for i, t in enumerate(type_sequence[:10])]
    
    # Step 6: Final aggregation using only health score and window average
    reference_avg = sum(w['average'] for w in windows) / len(windows)
    scaled_health = health * (reference_avg / 100.0)
    
    # Hidden dependency: modify based on slice symmetry
    first_half_types = type_sequence[:len(type_sequence)//2]
    second_half_types = type_sequence[len(type_sequence)//2:]
    if first_half_types[::-1] != second_half_types:  # Asymmetry check
        scaled_health -= 15.5
    
    return scaled_health

# Decoy configuration block
default_configs = {
    'mode': 'aggressive',
    'timeout': 30,
    'retries': 3,
    'backoff': 2
}
system_thresholds = {
    'critical_stability': 65,
    'max_window_skew': 10.5,
    'health_floor': 800
}

# Main entry point
telemetry_log = generate_telemetry()

# Fake preprocessing chain – creates illusion of complexity
preprocessed = [x for x in telemetry_log if x['value'] > 10]
sorted_preprocessed = sorted(preprocessed, key=lambda x: x['value'])
mapped_values = list(map(lambda x: {**x, 'flagged': x['value'] > 75}, sorted_preprocessed))

# Critical execution point buried in noise
interim_result = extract_signal_windows(mapped_values, 4)
decoy_aggregation = [w for w in interim_result if w['type'] == 'voltage']

# Actual relevant call
processed_metrics = aggregate_diagnostics(telemetry_log)

# Final computation combining multiple layers
final_diagnostic = int(processed_metrics + len(decoy_aggregation) * 0.0)  # Neutral addition

# Print result as required
print(f"Result: {final_diagnostic}")