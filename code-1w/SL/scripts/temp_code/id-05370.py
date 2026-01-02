from collections import defaultdict, Counter
import math

# Simulated sensor data processing for industrial equipment health monitoring
def analyze_vibration_patterns(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    squared = [x * x for x in filtered]
    return sum(squared) / len(squared) if squared else 0.0

# Irrelevant helper - distractor function (dead code path)
def thermal_compensation(temps):
    avg = sum(temps) / len(temps)
    adjusted = [t * 1.02 - 0.5 for t in temps]
    return sum(adjusted) / len(adjusted)

# Data normalization using z-score (used in main logic)
def z_score_normalize(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean) / std_dev for x in data] if std_dev != 0 else [0] * len(data)

# Bitmask-based fault classification (core logic component)
def classify_fault_modes(status_bits):
    critical_mask = 0b1010  # bits indicating severe issues
    warning_mask = 0b0101   # bits for warnings
    crit_count = bin(status_bits & critical_mask).count('1')
    warn_count = bin(status_bits & warning_mask).count('1')
    return crit_count * 4 + warn_count * 2

# Main evaluation pipeline
metric_data = [3.4, 2.8, 3.6, 4.1, 3.9]
baseline = [3.0, 3.0, 3.0, 3.0, 3.0]

# Distractor variables - irrelevant calculations
idle_consumption = 12.7
peak_load_ratio = 1.85
redundancy_factor = 0
for i in range(len(metric_data)):
    redundancy_factor += (i + 1) * 0.1  # Unused accumulation

# Multiple data structures with cross-references
event_log = defaultdict(list)
event_log['vibration'].append(analyze_vibration_patterns([-0.2, 0.5, -0.1, 0.3]))
event_log['vibration'].append(analyze_vibration_patterns([0.0, 0.0, 0.0]))  # Zero result

# Sensor fusion simulation (partially relevant)
signal_quality = {
    'ch1': 0.93, 'ch2': 0.87, 'ch3': 0.76
}
weights = z_score_normalize(list(signal_quality.values()))
weighted_sum = sum(w * q for w, q in zip(weights, signal_quality.values()))

# State tracking with bitwise operations
system_state = 0b1101
debug_mode = False
if system_state & 0b1000:
    debug_mode = True
    extra_diagnostic = classify_fault_modes(system_state)  # Used later

# Decoy data transformation chain
temp_history = [22.5, 23.1, 22.8, 24.0]
smoothed_temps = []
for t in temp_history:
    smoothed_temps.append(t * 0.9 + 0.5)  # Irrelevant transformation

# Core metric computation with distractors
aggregated_metrics = []
for val in metric_data:
    deviation = abs(val - baseline[metric_data.index(val)])
    penalty = 0
    if deviation > 0.5:
        penalty = deviation * 2
    elif deviation > 0.2:
        penalty = deviation * 1.2
    aggregated_metrics.append(deviation - penalty)

# Use of Counter for frequency analysis (distractor)
freq_analysis = Counter([round(x, 1) for x in metric_data])
mode_value = freq_analysis.most_common(1)[0][1] if freq_analysis else 0

# Final performance scoring logic
def evaluate_performance(metrics, base):
    norm_metrics = z_score_normalize(metrics)
    base_norm = z_score_normalize(base)
    
    # Composite score with multiple components
    coherence = sum(abs(m - b) for m, b in zip(norm_metrics, base_norm))
    stability = sum(1 for m in metrics if 2.5 < m < 4.5)  # Within operational range
    
    # Incorporate bit-classification result from earlier
    fault_penalty = extra_diagnostic if 'extra_diagnostic' in globals() else 0
    
    # Primary calculation
    raw_score = sum(norm_metrics) * 100
    adjustment = stability * 5 - coherence * 10 - fault_penalty * 3
    
    # Final non-linear transformation
    final = raw_score + adjustment
    return max(final, 0)

# Execution point of interest
final_score = evaluate_performance(metric_data, baseline)

# Output requirement
print(f"Target result: {final_score}")