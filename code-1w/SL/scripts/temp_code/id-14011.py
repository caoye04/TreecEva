import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [23.4, 19.5, 20.1, 25.3, 18.7, 21.0, 22.8, 19.9]

def calibrate_sensor(value, factor=1.02):
    return value * factor

def is_stable(voltage):
    return 4.95 <= voltage <= 5.05

def generate_checksum(data_list):
    # Irrelevant checksum for distraction
    return sum(hash(str(x)) % 1000 for x in data_list) % 97

def deprecated_filter(data):
    # Dead code path - never called
    return [x for x in data if x > 20]

def parse_metadata():
    metadata_str = "DEVICE:X7|LOC:ZONE3|CAL:1.02|ACTIVE:YES|VERSION:2.1"
    items = metadata_str.split('|')
    meta = {}
    for item in items:
        k, v = item.split(':')
        meta[k.lower()] = v
    return meta

def transform_scale(val, mode='linear'):
    if mode == 'log':
        return math.log(val) if val > 0 else 0
    else:
        return val * 1.1  # Default linear scaling

def analyze_outlier(readings, limit=20.0):
    count = 0
    for r in readings:
        if r < limit:
            count += 1
    return count > 3  # More than 3 below limit is anomalous

def compute_entropy(data):
    # Distractor function - computes entropy but not used in final result
    from collections import Counter
    counts = Counter([round(x, 0) for x in data])
    total = len(data)
    entropy = 0
    for cnt in counts.values():
        p = cnt / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def main():
    raw_readings = fetch_raw_readings()
    
    # Irrelevant voltage check
    current_voltage = 5.02
    system_stable = is_stable(current_voltage)
    
    # Unused transformation mode
    scaling_mode = 'log' if len(raw_readings) % 2 == 0 else 'linear'
    
    # Calibrate all readings
    calibrated = [calibrate_sensor(r) for r in raw_readings]
    
    # Apply transform scale (but only store one value for distraction)
    scaled_single = transform_scale(calibrated[0], mode='linear')
    
    # Parse metadata (used later for threshold)
    device_meta = parse_metadata()
    
    # Compute checksum (irrelevant)
    chksum = generate_checksum(calibrated)
    
    # Entropy computation (red herring)
    entropy_value = compute_entropy(calibrated)
    
    # Filter valid zone (only Zone 3 is approved)
    if device_meta['loc'] != 'ZONE3':
        raise RuntimeError('Invalid location')
    
    # Determine dynamic threshold based on version and calibration factor
    cal_factor = float(device_meta['cal'])
    version = device_meta['version']
    base_threshold = 20.5
    if version == '2.1':
        adjustment = 0.8 if cal_factor > 1.0 else 0.5
        base_threshold += adjustment
    
    # Build threshold map per reading index
    threshold_map = {}
    for i in range(len(calibrated)):
        multiplier = 1.05 if i % 2 == 0 else 0.95
        threshold_map[i] = round(base_threshold * multiplier, 2)
    
    # Processed data: apply conditional offset based on position
    processed_data = []
    for idx, val in enumerate(calibrated):
        if idx == 0:
            processed_data.append(val + 0.5)
        elif idx == len(calibrated) - 1:
            processed_data.append(val - 0.3)
        else:
            processed_data.append(val)
    
    # Linear search for first reading below local threshold
    first_below_idx = -1
    for i in range(len(processed_data)):
        if processed_data[i] < threshold_map[i]:
            first_below_idx = i
            break
    
    # Diagnostic logic based on multiple factors
    def analyze_readings(data, thresholds):
        above_count = 0
        for i, val in enumerate(data):
            if val >= thresholds[i]:
                above_count += 1
        trend_stable = all(
            abs(data[i] - data[i-1]) < 1.0 for i in range(1, len(data))
        )
        outlier_flag = analyze_outlier(data, limit=20.0)
        # Final diagnostic: 100 * ratio of above-threshold points + bonus if stable
        base_score = 100 * (above_count / len(data))
        bonus = 15 if trend_stable and not outlier_flag else 0
        return int(base_score + bonus)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()