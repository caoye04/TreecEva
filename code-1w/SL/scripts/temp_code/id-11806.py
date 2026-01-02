import math

def sensor_calibrate(raw):
    # Irrelevant calibration function (dead code path)
    return [x * 1.05 for x in raw]

def transform_signal(signal):
    # Unused transformation (distractor)
    return [math.sin(x / 10) for x in signal]

def validate_range(values, low, high):
    # Misleading validation not used in main logic
    return all(low <= v <= high for v in values)

def accumulate_deltas(readings):
    # Red herring: computes deltas but not used in final result
    deltas = []
    for i in range(1, len(readings)):
        deltas.append(abs(readings[i] - readings[i-1]))
    return sum(deltas)

def filter_outliers(data, factor=1.5):
    # Heavily distracting but ultimately unused filtering
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def decode_pattern(sequence):
    # Decoy function with bit manipulation red herring
    pattern_value = 0
    for i, val in enumerate(sequence):
        if val > 50:
            pattern_value ^= (val << (i % 5)) & 0xFFFF
    return pattern_value

def analyze_readings(data, config):
    # Core logic buried in noise
    baseline = sum(data[:5]) / 5
    adjusted = [x - baseline for x in data]
    
    # Real processing begins here
    squared_devs = [(x ** 2) for x in adjusted]
    mean_square = sum(squared_devs) / len(squared_devs)
    rms = math.sqrt(mean_square)
    
    # Dictionary-based state tracking (required feature)
    status = {
        'baseline': baseline,
        'rms': rms,
        'count_above_threshold': 0,
        'peaks': [],
        'diagnostic_code': 0
    }
    
    threshold = config['critical_level']
    for i, x in enumerate(adjusted):
        if x > threshold:
            status['count_above_threshold'] += 1
            if i > 0 and adjusted[i-1] <= threshold:
                status['peaks'].append(i)
    
    # Critical branching logic
    if len(status['peaks']) >= 3:
        status['diagnostic_code'] = 776
    elif status['rms'] > 25:
        status['diagnostic_code'] = 889
    else:
        status['diagnostic_code'] = 412
    
    # Final computation
    peak_influence = len(status['peaks']) * status['rms']
    final_score = int(peak_influence + status['diagnostic_code'])
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated sensor inputs (real data)
    raw_input_stream = [102, 105, 98, 110, 100, 132, 95, 140, 108, 155, 90, 138, 115]
    
    # Irrelevant preprocessing steps (distractions)
    calibrated = sensor_calibrate(raw_input_stream)
    signal_transform = transform_signal(calibrated)
    delta_sum = accumulate_deltas(raw_input_stream)
    clean_data = filter_outliers(raw_input_stream, 2.0)
    pattern_key = decode_pattern(raw_input_stream)
    
    # Actual processing pipeline
    base_offset = 100
    processed_data = [x - base_offset for x in raw_input_stream]  # Center around zero
    
    # Threshold configuration (dictionary usage)
    thresholds = {
        'warning_level': 20,
        'critical_level': 30,
        'emergency': 50
    }
    
    # Introduce decoy variables with plausible but unused values
    temp_analysis = [x for x in processed_data if x > 25]
    rolling_avg = sum(processed_data[-3:]) / 3
    
    # Key statement
    final_diagnostic = analyze_readings(processed_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")