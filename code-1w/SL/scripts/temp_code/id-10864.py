import itertools

def collect_sensor_data():
    # Simulated sensor array readings (real data)
    raw_readings = [107, 214, 198, 205, 99, 211, 103, 200, 195]
    timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
    labeled_readings = list(zip(timestamps, raw_readings))
    return labeled_readings

def apply_mask(data, mask):
    # Irrelevant masking function (dead path)
    return [x for i, x in enumerate(data) if mask[i]]

def analyze_pattern(seq):
    # Misleading pattern analyzer (unused)
    return sum(1 for a, b in zip(seq, seq[1:]) if b > a)

def legacy_checksum(arr):
    # Distractor: old system checksum (not used in final logic)
    chk = 0
    for val in arr:
        chk = (chk * 31 + val) % 10007
    return chk

def extract_values(labeled_data):
    # Extract numeric values from labeled tuples
    return [value for _, value in labeled_data]

def filter_outliers(values, threshold=100):
    # Filter values below threshold (relevant)
    return [v for v in values if v > threshold]

def compute_entropy(values):
    # Complex distractor: entropy calculation (not used)
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * log(p, 2) for p in probs if p > 0)

def calibrate_readings(vals, factor):
    # Apply calibration (relevant but indirect)
    return [round(v * factor) for v in vals]

def detect_peaks(seq):
    # Unused peak detection (red herring)
    peaks = []
    for i in range(1, len(seq)-1):
        if seq[i-1] < seq[i] > seq[i+1]:
            peaks.append(i)
    return peaks

def group_by_parity(vals):
    # Distractor: grouping by even/odd (not used)
    even = [v for v in vals if v % 2 == 0]
    odd = [v for v in vals if v % 2 == 1]
    return {'even': even, 'odd': odd}

def process_readings(data, adjustment):
    # Core processing chain
    base_sum = sum(data)
    squared_devs = [(x - base_sum/len(data))**2 for x in data]
    variance = sum(squared_devs) / len(squared_devs)
    std_dev = variance ** 0.5
    adjusted_vals = [x + adjustment for x in data]
    total_impulse = sum(itertools.accumulate(adjusted_vals))
    normalized = total_impulse / (std_dev + 1)
    return int(round(normalized))

def main():
    # --- Real Execution Path ---
    readings_with_time = collect_sensor_data()
    
    # Extract values for processing
    raw_values = extract_values(readings_with_time)  # [107, 214, ...]
    
    # Filter out low readings (critical step)
    filtered_data = filter_outliers(raw_values, threshold=100)  # removes 99 only
    
    # Irrelevant operations (distractors)
    parity_groups = group_by_parity(raw_values)
    legacy_chk = legacy_checksum(raw_values)
    entropy_score = compute_entropy(filtered_data)
    peak_locations = detect_peaks(raw_values)
    
    # Calibration factor derived from string analysis (real but non-obvious)
    diagnostic_key = 'CALIB_2025'
    version_str = ''.join([c for c in diagnostic_key if c.isdigit()])
    version_num = int(version_str)  # 2025
    checksum_digit = sum(int(d) for d in str(version_num))  # 2+0+2+5=9
    calibration_factor = 0.1 * checksum_digit  # 0.9
    
    # Main processing
    calibrated_filtered = calibrate_readings(filtered_data, calibration_factor)
    
    # Final diagnostic computation
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    # Dead code paths (misleading)
    if len(parity_groups['even']) > 10:
        fallback = apply_mask(calibrated_filtered, [True]*len(calibrated_filtered))
    else:
        temp_seq = [x*2 for x in filtered_data[:3]]
        pattern_score = analyze_pattern(temp_seq)

if __name__ == '__main__':
    main()