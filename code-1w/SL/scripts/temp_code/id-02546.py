import math

# Simulated sensor fusion system for environmental monitoring

def collect_data():
    raw_entries = [
        'temp:23.5,hum:45,co2:415',
        'temp:24.1,hum:47,co2:422',
        'temp:22.8,hum:44,co2:409'
    ]
    return raw_entries

def parse_entry(entry):
    parsed = {}
    parts = entry.split(',')
    for part in parts:
        k, v = part.split(':')
        parsed[k] = float(v)
    return parsed

def extract_temperatures(data_list):
    temps = []
    for record in data_list:
        reading = parse_entry(record)
        temps.append(reading['temp'])
    return temps

def compute_variance(values):
    mean = sum(values) / len(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

def normalize_signal(value, min_val, max_val):
    # Irrelevant normalization function (dead path)
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def encrypt_key(sequence):  # Distractor function - looks important but unused
    key = 0
    for i, val in enumerate(sequence):
        key ^= int(val * 17) & 0xFF
    return key

def filter_outliers(data, threshold=1.5):
    # Simple outlier filtering using IQR concept
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def aggregate_metrics(valid_readings):
    metrics = {
        'avg': sum(valid_readings) / len(valid_readings),
        'min': min(valid_readings),
        'max': max(valid_readings),
        'range': max(valid_readings) - min(valid_readings)
    }
    # Decoy calculation with misleading intermediate
    phantom_score = (metrics['avg'] * 1.07 + metrics['range'] * 0.3) % 97
    metrics['phantom'] = phantom_score  # Red herring
    return metrics

def apply_calibration(readings, factor=1.02):
    return [r * factor for r in readings]

def detect_anomaly_pattern(signal):
    # Bitwise pattern analysis on integer parts
    integers = [int(x) for x in signal]
    pattern_flag = 0
    for val in integers:
        pattern_flag ^= (val & 0b1100) >> 2  # Extract bits
    return pattern_flag

def analyze_readings(signal_sequence):
    calibrated = apply_calibration(signal_sequence)
    filtered = filter_outliers(calibrated)
    aggregated = aggregate_metrics(filtered)
    
    # Core logic disguised among distractions
    base_index = int(aggregated['avg'])
    fluctuation = aggregated['range']
    peak = aggregated['max']
    
    # Irrelevant string transformation chain (distractor)
    tag = f"sensor_{base_index}_{peak:.0f}"
    checksum = sum(ord(c) for c in tag) % 100
    temp_str = tag + str(checksum)
    temp_str = temp_str.replace('_', '').upper()
    
    # Real computation hidden in middle
    magic_offset = 89
    diagnostic_code = (base_index * 31) ^ int(fluctuation * 100)  # XOR operation
    final_diagnostic = (diagnostic_code + magic_offset) % 10000
    
    # More red herrings
    decoy_map = {i: math.sin(i * 0.1) for i in range(10)}
    shadow_value = sum(decoy_map.values()) * aggregated['phantom']
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Collect and parse raw sensor logs
    entries = collect_data()
    temperatures = extract_temperatures(entries)
    
    # Apply irrelevant preprocessing
    dummy_keys = [encrypt_key(temperatures)] * 3
    normalized_temps = [normalize_signal(t, 20, 30) for t in temperatures]
    
    # Process actual signal
    processed_signals = apply_calibration(temperatures)
    anomaly_flag = detect_anomaly_pattern(processed_signals)
    
    # Compute variance (unused metric - distraction)
    variance = compute_variance(processed_signals)
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output result
    print(f"Result: {final_diagnostic}")