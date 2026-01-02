from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation and anomaly detection system
def collect_sensor_readings():
    raw_readings = [
        (1007, 23.5), (1008, 24.1), (1009, 19.8), (1010, 25.6),
        (1011, 26.7), (1012, 22.4), (1013, 20.3), (1014, 27.8),
        (1015, 28.9), (1016, 29.4), (1017, 18.2), (1018, 30.1)
    ]
    return raw_readings

def filter_outliers(data, low_thresh=18.5, high_thresh=29.5):
    # Irrelevant filtering for distraction
    filtered = [x for x in data if low_thresh <= x[1] <= high_thresh]
    outlier_count = len(data) - len(filtered)  # Distractor variable
    return filtered

def compute_rolling_average(values, window=3):
    averages = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages  # Unused return in main logic

def transform_readings(readings):
    # Extract timestamps and normalize temperatures
    timestamps = [r[0] for r in readings]
    temps = [r[1] for r in readings]
    
    # Normalize timestamps to offset from first reading
    base_time = timestamps[0]
    time_offsets = [t - base_time for t in timestamps]
    
    # Apply misleading exponential smoothing (not used later)
    smoothed_temps = []
    alpha = 0.3
    smoothed = temps[0]
    for temp in temps:
        smoothed = alpha * temp + (1 - alpha) * smoothed
        smoothed_temps.append(round(smoothed, 2))
    
    # Actual transformation: pair offsets with original temps
    transformed = [(time_offsets[i], temps[i]) for i in range(len(temps))]
    return transformed

def generate_checksum(sequence):
    # Bit manipulation red herring
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 10)  # Scale to integer
        checksum = (checksum << 1) & 0xFFFF  # Left shift and mask
    return checksum  # Computed but unused

def detect_cycles(time_series, length=4):
    # Look for repeating patterns (distraction)
    cycles = []
    for i in range(len(time_series) - length + 1):
        segment = tuple(time_series[i:i+length])
        if time_series.count(time_series[i]) > 1:
            cycles.append(segment)
    return list(set(cycles))  # Dead code path

def analyze_patterns(data, threshold):
    # Core analysis: count how many temperature deviations exceed threshold
    deviations = []
    for offset, temp in data:
        expected = 22.0 + (offset * 0.2)  # Temp increases 0.2 per time unit
        dev = abs(temp - expected)
        deviations.append(dev)
    
    # Use Counter to classify deviation magnitude
    cat_devs = []
    for d in deviations:
        if d < 1.0:
            cat_devs.append('low')
        elif d < 3.0:
            cat_devs.append('moderate')
        else:
            cat_devs.append('high')
    
    dev_counter = Counter(cat_devs)
    high_count = dev_counter['high']
    moderate_count = dev_counter['moderate']
    
    # Secondary logic: use set operations on time offsets to create decoy metric
    offset_set_a = {d[0] for d in data if d[1] > 25.0}
    offset_set_b = {d[0] for d in data if d[0] % 2 == 0}
    intersection_size = len(offset_set_a & offset_set_b)  # Distractor
    union_size = len(offset_set_a | offset_set_b)  # Distractor
    jaccard = intersection_size / union_size if union_size > 0 else 0  # Misleading float
    
    # Real computation: weighted diagnostic score
    # Each 'high' deviation contributes 7, 'moderate' contributes 3
    diagnostic_score = (high_count * 7) + (moderate_count * 3)
    
    # Additional logic: apply modular correction based on sum of all offsets
    total_offset = sum(d[0] for d in data)
    mod_correction = (total_offset * 2) % 11  # 0-10 adjustment
    final_score = diagnostic_score - mod_correction
    
    return final_score

def auxiliary_debug_report(data):
    report = defaultdict(list)
    for i, (offset, temp) in enumerate(data):
        report['indices'].append(i)
        report['offsets'].append(offset)
        report['temps'].append(temp)
    return report  # Unused function - dead code path

def main():
    # Step 1: Collect raw data
    readings = collect_sensor_readings()
    
    # Step 2: Filter outliers (but we don't use filtered data directly)
    clean_readings = filter_outliers(readings, 18.5, 29.5)
    
    # Step 3: Transform the data using actual logic path
    transformed_data = transform_readings(readings)  # Uses full dataset
    
    # Step 4: Generate checksum (irrelevant)
    temp_sequence = [r[1] for r in readings]
    chksum = generate_checksum(temp_sequence)
    
    # Step 5: Detect cycles (never called)
    # cycles = detect_cycles(temp_sequence)  # Commented out - red herring
    
    # Step 6: Set key threshold based on rolling average (computed but unused)
    rolling_avgs = compute_rolling_average(temp_sequence)
    dynamic_threshold = sum(rolling_avgs) / len(rolling_avgs) if rolling_avgs else 25.0
    
    # Step 7: Define actual threshold for analysis (bypassing dynamic one)
    key_threshold = 2.0  # Hardcoded threshold
    
    # Step 8: Analyze patterns - this is where the answer is computed
    final_diagnostic = analyze_patterns(transformed_data, key_threshold)
    
    # Step 9: Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()