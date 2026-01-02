from collections import defaultdict, Counter
import math

# Simulated sensor readings over time (timestamp -> value)
readings = [
    (1001, 45.2), (1002, 46.1), (1003, 45.8), (1004, 44.9), (1005, 47.3),
    (1006, 120.5), (1007, 46.0), (1008, 45.6), (1009, 46.3), (1010, 118.9),
    (1011, 45.7), (1012, 46.2), (1013, 45.4), (1014, 46.1), (1015, 45.9)
]

# Irrelevant helper: computes average but on wrong data type
def compute_avg(data_map):
    total = 0
    for k in data_map:
        if isinstance(data_map[k], list):
            total += sum(data_map[k])
    return total / len(data_map) if data_map else 0

def detect_spikes(values, threshold=50.0):
    # Misleading function: detects high values but not used in final path
    spikes = []
    for ts, val in values:
        if val > threshold:
            spikes.append((ts, val))
    return spikes

def filter_anomalous(sensor_data):
    # Use Counter to count frequency of rounded values
    freq_counter = Counter(round(val) for _, val in sensor_data)
    
    # Compute baseline from most frequent values
    baseline_candidates = [val for val, cnt in freq_counter.items() if cnt > 1]
    if not baseline_candidates:
        baseline_candidates = [round(v) for _, v in sensor_data[:5]]
    
    avg_baseline = sum(baseline_candidates) / len(baseline_candidates)
    
    # Filter out anomalous points more than 30 away from baseline
    filtered = [(ts, val) for ts, val in sensor_data if abs(val - avg_baseline) < 30]
    
    # Dead code branch: never executed due to prior filtering
    if len(filtered) > 100:
        temp_store = {}
        for t, v in filtered:
            bucket = t // 100
            if bucket not in temp_store:
                temp_store[bucket] = []
            temp_store[bucket].append(v)
    
    return filtered

def rolling_window_smooth(data_list, window_size=3):
    # Unused smoothing function — red herring
    smoothed = []
    for i in range(len(data_list)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window_avg = sum(v for _, v in data_list[start:end]) / (end - start)
        smoothed.append(window_avg)
    return smoothed

def analyze_readings(cleaned_data):
    # Group by tens digit of timestamp using defaultdict
    grouped = defaultdict(list)
    for ts, val in cleaned_data:
        key = (ts // 10) * 10
        grouped[key].append(val)
    
    # Extract statistical features
    medians = []
    for key in sorted(grouped.keys()):
        vals = sorted(grouped[key])
        mid = len(vals) // 2
        median = (vals[mid] + vals[mid-1]) / 2 if len(vals) % 2 == 0 else vals[mid]
        medians.append(median)
    
    # Compute interquartile-like spread (not true IQR)
    sorted_medians = sorted(medians)
    q1 = sorted_medians[len(sorted_medians)//4]
    q3 = sorted_medians[3*len(sorted_medians)//4]
    iqr_like = q3 - q1
    
    # Secondary distraction: unused correlation attempt
    correlations = []
    for i in range(1, len(sorted_medians)):
        prod = sorted_medians[i] * sorted_medians[i-1]
        correlations.append(math.sin(prod % 10))  # Arbitrary transformation
    
    # Final diagnostic based on mean of medians and stability factor
    mean_median = sum(medians) / len(medians)
    stability_score = mean_median / (iqr_like + 1e-8)
    
    # Key computation: XOR of truncated mean and scaled stability
    hash_component = int(mean_median) ^ int(stability_score * 1000)
    
    # Final result
    final_diagnostic = hash_component + len(grouped) * 10
    
    # Dead assignment: doesn't affect output
    final_diagnostic = final_diagnostic | 0x0  # No-op bitwise or
    
    return final_diagnostic

# Irrelevant global variables
total_sensors = 7
sensor_specs = {'range': (0, 200), 'precision': 0.1}
last_calibration = "2023-09-15"

# Main execution path
spike_list = detect_spikes(readings, threshold=100)  # Computed but not used
anomalous_removed = filter_anomalous(readings)
diagnostic_snapshot = rolling_window_smooth(anomalous_removed)  # Unused
final_diagnostic = analyze_readings(filter_anomalous(readings))
print(f"Result: {final_diagnostic}")