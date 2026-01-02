from collections import defaultdict, Counter
import math

# Simulated sensor array data processing for environmental anomaly detection
def collect_readings():
    raw_samples = [14, 19, 24, 17, 31, 29, 22, 33, 35, 26, 18, 20, 23, 27, 30]
    offset = 5
    adjusted = [x + offset for x in raw_samples]
    return adjusted

def filter_outliers(data, limit=25):
    upper_fence = limit
    filtered = [x for x in data if x <= upper_fence]
    excess = [x for x in data if x > upper_fence]  # distractor: unused
    return filtered

def compute_entropy(values):
    freqs = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_signature(vector):
    sig = 0
    for i, v in enumerate(vector):
        sig ^= (v * (i + 1))  # bit manipulation red herring
    return sig % 1000

def rolling_average(series, window=3):
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs  # decoy: not used later

def detect_spikes(readings, sensitivity=1.5):
    spikes = []
    baseline = sum(readings) // len(readings)
    for val in readings:
        if val > baseline * sensitivity:
            spikes.append(val)
    return spikes  # misleading path

def aggregate_metrics(log_buffer, threshold=20):
    metrics = defaultdict(float)
    high_activity = [x for x in log_buffer if x > threshold]
    low_activity = [x for x in log_buffer if x <= threshold]
    
    # Core calculation path
    avg_high = sum(high_activity) / len(high_activity) if high_activity else 0
    avg_low = sum(low_activity) / len(low_activity) if low_activity else 0
    
    # Irrelevant transformations
    squared_norm = sum(x**2 for x in log_buffer) ** 0.5
    peak = max(log_buffer)  # distractor
    duration = len(log_buffer) * 0.5  # fake time unit
    
    # Critical metric computation
    balance_score = abs(avg_high - avg_low) * len(high_activity)
    stability_index = compute_entropy(log_buffer)
    
    # Complex but irrelevant branching
    if balance_score > 30:
        adjustment = math.sin(stability_index)
    elif balance_score < 10:
        adjustment = math.cos(stability_index)
    else:
        adjustment = 0.75
    
    # Actual answer depends only on this
    diagnostic_weight = avg_high * 0.6 + avg_low * 0.4 + stability_index
    
    # Dead code branches with decoy outputs
    if len(log_buffer) % 2 == 0:
        dummy = generate_signature(log_buffer)
    else:
        temp_vec = rolling_average(log_buffer)

    final_diagnostic = int(round(diagnostic_weight))
    return final_diagnostic

# Main execution flow
sensor_data = collect_readings()
pruned_data = filter_outliers(sensor_data, limit=28)
detected_events = detect_spikes(pruned_data, sensitivity=1.2)

# Unused analysis branches
if len(detected_events) > 3:
    event_entropy = compute_entropy(detected_events)
else:
    event_profile = [x*2 for x in detected_events]  # dead code

report_buffer = pruned_data  # critical assignment
activation_threshold = 19

# Key statement
final_diagnostic = aggregate_metrics(report_buffer, activation_threshold)
print(f"Result: {final_diagnostic}")