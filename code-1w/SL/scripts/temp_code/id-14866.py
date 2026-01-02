import math

# Simulated sensor array diagnostics with redacted calibration logic
def calibrate_sensor(x, mode='legacy'):
    if mode == 'legacy':
        return (x * 0.87) + 3.2
    else:
        return (x * 1.05) - 1.7

def parse_timestamp(raw):
    # Irrelevant timestamp parser (dead function)
    return sum([int(d) for d in str(raw) if d.isdigit()]) % 60

def legacy_filter(stream):
    # Outdated noise filter, not used in main flow
    return [x for x in stream if x > -5 and x < 95]

def accumulate_moving_avg(data, window=3):
    # Unused moving average helper
    avg_list = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        avg_list.append(sum(data[start:i+1]) / (i - start + 1))
    return avg_list

def extract_peaks(signal):
    # Detect peaks but add decoy values
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks + [float('inf')]  # deliberate misleading value

def normalize_readings(raw_vals):
    # Normalize using a mix of scaling and offset
    calibrated = [calibrate_sensor(val) for val in raw_vals]
    baseline = sum(calibrated) / len(calibrated)
    adjusted = [val - baseline for val in calibrated]
    return adjusted

def classify_anomaly(severity):
    # Unused classification tier
    if severity < 10: return 'LOW'
    elif severity < 25: return 'MEDIUM'
    else: return 'HIGH'

def compute_entropy(values):
    # Distractor: computes entropy but not used in final result
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def detect_outliers(data, threshold=2):
    # Dead path: detects but doesn't affect final output
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data))**0.5
    return [x for x in data if abs(x - mean_val) > threshold * std_dev]

def transform_coordinates(indices):
    # Geospatial decoy transformation
    transformed = set()
    for idx in indices:
        lat = (idx * 1.7) % 90
        lon = (idx * 2.3) % 180
        transformed.add((round(lat, 3), round(lon, 3)))
    return transformed

def analyze_readings(logs):
    # Core analysis function
    filtered = [x for x in logs if x >= 0]  # remove negative calibrated noise
    
    # Apply nonlinear compression
    compressed = []
    for val in filtered:
        if val == 0:
            compressed.append(0)
        else:
            compressed.append(math.log(val ** 2 + 1))
    
    # Bucket into tiers
    tiers = {'A': 0, 'B': 0, 'C': 0}
    for c in compressed:
        if c < 2.0:
            tiers['A'] += 1
        elif c < 4.0:
            tiers['B'] += 1
        else:
            tiers['C'] += 1
    
    # Compute weighted diagnostic score
    weights = {'A': 1, 'B': 3, 'C': 7}
    score = 0
    for key in tiers:
        score += tiers[key] * weights[key]
    
    # Final adjustment using modular arithmetic
    prime_offset = 101
    score = (score * 13) % prime_offset
    
    # Introduce irrelevant secondary calculation (distractor)
    _ = compute_entropy(compressed)
    _ = detect_outliers(filtered)
    
    return int(score)

# Main execution flow
if __name__ == '__main__':
    # Raw sensor inputs (simulated)
    raw_sensor_data = [12, 15, 8, 23, 19, 7, 31, 25, 14, 18, 20, 9, 27, 22, 11]
    
    # Unused timestamp log (red herring)
    timestamps = [202310150001, 202310150002, 202310150003, 202310150004, 202310150005]
    parsed_times = [parse_timestamp(t) for t in timestamps]
    
    # Process logs through pipeline
    processed_logs = normalize_readings(raw_sensor_data)
    
    # Secondary unused transformation
    peak_values = extract_peaks(raw_sensor_data)
    geo_refs = transform_coordinates([1, 3, 5, 7])
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_logs)
    
    # Output target result
    print(f"Result: {final_diagnostic}")