from collections import defaultdict, Counter
import math

# Simulated sensor data processing system with red herrings
def analyze_signal_strength(signal_log):
    strength_map = defaultdict(int)
    for entry in signal_log:
        node_id, strength = entry
        strength_map[node_id] += strength
    return strength_map

def compute_phase_shift(frequency, time_delay):
    # Irrelevant computation - not used in final result
    return (2 * math.pi * frequency * time_delay) % (2 * math.pi)

def evaluate_redundancy(nodes):
    # Dead code path - never called
    redundancy_score = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if nodes[i][1] == nodes[j][1]:
                redundancy_score += 1
    return redundancy_score

def generate_checksum(data_sequence):
    # Distractor function: looks important but unused
    checksum = 0
    for i, val in enumerate(data_sequence):
        checksum ^= (val * (i + 1)) % 256
    return checksum

def filter_anomalies(records, threshold=3.5):
    anomalies = []
    normal_values = []
    avg = sum(records) / len(records)
    std_dev = (sum((x - avg) ** 2 for x in records) / len(records)) ** 0.5
    
    for val in records:
        if abs(val - avg) > threshold * std_dev:
            anomalies.append(val)
        else:
            normal_values.append(val)
    
    # Misleading intermediate: looks like it might be used
    anomaly_ratio = len(anomalies) / len(records) if records else 0
    return normal_values

def extract_timing_segments(raw_intervals):
    segments = []    
    for interval in raw_intervals:
        start, end = interval
        duration = end - start
        if duration > 0:
            segments.append(round(duration * 1000, 3))  # Convert to milliseconds
    return segments

def merge_overlap_ranges(ranges):
    # Unused complex logic
    if not ranges:
        return []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def calculate_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def validate_synchronization(timestamps):
    # Another decoy function
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    ideal_interval = sum(diffs) / len(diffs)
    variance = sum((d - ideal_interval) ** 2 for d in diffs) / len(diffs)
    return variance < 0.05

def aggregate_metrics(timing_data, flags):
    base_score = 0
    
    # Key relevant operations
    for i, (t_val, flag) in enumerate(zip(timing_data, flags)):
        if flag:
            base_score += t_val * (i + 1)
        else:
            base_score -= t_val // (i + 2)
    
    # Introduce distractor variable that looks critical
    adjustment_factor = calculate_entropy(flags) * 100
    temp_offset = sum(1 for f in flags if f) * 0.25
    
    # Final computation - only base_score is actually used
    final_value = int(base_score - adjustment_factor + temp_offset)
    return final_value

# Main execution block
if __name__ == "__main__":
    # Simulated input data
    raw_sensor_log = [("A1", 5), ("B2", 3), ("A1", 7), ("C3", 8), ("B2", 2)]
    frequency_bands = [440, 880, 1760]
    timing_intervals = [(1.23, 1.87), (2.05, 3.12), (3.45, 4.67), (5.10, 6.22)]
    node_configurations = [("N1", "alpha"), ("N2", "beta"), ("N3", "alpha"), ("N4", "gamma")]
    diagnostic_flags = [True, False, True, True, False, True]
    
    # Irrelevant transformations
    signal_map = analyze_signal_strength(raw_sensor_log)
    phase_shifts = [compute_phase_shift(fb, 0.01) for fb in frequency_bands]
    cleaned_diagnostics = filter_anomalies([1.2, 1.5, 1.3, 1.4, 10.8, 1.6, 1.7])
    
    # Key data preparation
    timing_milliseconds = extract_timing_segments(timing_intervals)
    # Truncate to match flag length
    truncated_timings = [int(t) for t in timing_milliseconds[:6]]  # [640, 1070, 1220, 1120, 0, 0] -> take first 6
    extended_flags = diagnostic_flags  # Length 6
    
    # Dead operation on irrelevant data
    overlap_regions = merge_overlap_ranges([(1, 5), (3, 8), (10, 12)])
    sync_valid = validate_synchronization([1.0, 2.05, 3.01, 4.02])
    
    # Core computation path
    final_diagnostic = aggregate_metrics(truncated_timings, extended_flags)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")