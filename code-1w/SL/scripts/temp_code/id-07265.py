from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor network diagnostics with noise filtering and pattern analysis
def generate_sensor_data():
    # Irrelevant synthetic data generation (distractor)
    base_signals = [12, 15, 14, 13, 16, 25, 18, 17, 19, 21]
    noise_pattern = cycle([0.1, -0.2, 0.3])
    return [round(sig + next(noise_pattern), 2) for sig in base_signals]

# Misleading preprocessing function (dead path)
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-2):i+3]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Decoy transformation (unused)
def frequency_analysis(seq):
    freq_pairs = list(combinations(seq, 2))
    return len(freq_pairs)

# Real processing begins here
def filter_anomalies(readings):
    threshold = 20.0
    filtered = []
    anomaly_flags = []
    
    for val in readings:
        is_anomalous = val > threshold
        anomaly_flags.append(is_anomalous)
        if not is_anomalous:
            filtered.append(val)
    
    # Secondary filter: remove values below 14.5 unless they follow an anomaly
    refined = []
    for i, val in enumerate(filtered):
        if val >= 14.5:
            refined.append(val)
        elif i > 0 and filtered[i-1] < 14.5:
            refined.append(val)
    
    return refined

def compute_entropy(values):
    # Irrelevant entropy calculation (distractor)
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return round(entropy, 4)

def detect_patterns(seq):
    # Unused pattern detection (misleading intermediate)
    patterns = []
    for i in range(len(seq) - 1):
        diff = seq[i+1] - seq[i]
        if abs(diff) < 1.0:
            patterns.append('stable')
        elif diff > 1.0:
            patterns.append('rising')
    return patterns

def process_readings(valid_readings):
    # Core aggregation logic
    stats_log = defaultdict(float)
    stats_log['count'] = len(valid_readings)
    stats_log['sum'] = sum(valid_readings)
    stats_log['base_index'] = 123
    
    # Transform through weighted phases
    phase_weights = [1.1, 0.9, 1.05, 0.95]
    weighted_sum = 0
    weight_cycle = cycle(phase_weights)
    
    for v in valid_readings:
        w = next(weight_cycle)
        weighted_sum += v * w
    
    stats_log['weighted_total'] = weighted_sum
    
    # Apply diagnostic formula
    raw_diagnostic = (stats_log['weighted_total'] * 1.75) - (stats_log['sum'] * 0.85)
    
    # Final adjustment based on count parity
    if stats_log['count'] % 2 == 0:
        final_diagnostic = raw_diagnostic + 100
    else:
        final_diagnostic = raw_diagnostic - 50
    
    # Key assignment point
    final_diagnostic = int(round(final_diagnostic))
    
    # Red herring: unrelated bit manipulation
    mask = 0b1101 ^ 0b1011
    shadow_flag = (final_diagnostic & mask) >> 1
    
    return final_diagnostic

# Orchestration with hidden signal chain
sensor_cluster = generate_sensor_data()
sensor_cluster.append(22.5)  # Inject borderline anomaly
sensor_cluster.append(11.2)  # Another low reading

# Dead call to decoy function
_ = frequency_analysis(sensor_cluster)

# Main execution path
filtered_data = filter_anomalies(sensor_cluster)
final_diagnostic = process_readings(filtered_data)

# Output result
print(f"Result: {final_diagnostic}")