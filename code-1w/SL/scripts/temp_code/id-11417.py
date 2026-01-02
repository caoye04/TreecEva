from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental monitoring
def acquire_raw_readings():
    return [23.5, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9, 25.1, 24.4, 23.6]

def calibrate_sensor(input_val, factor=0.98, offset=0.3):
    # Real but irrelevant calibration function
    return input_val * factor + offset

def deprecated_normalization(data):
    # Dead code path - never called
    return [x / max(data) for x in data]

def accumulate_trends(readings):
    trend_map = defaultdict(int)
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend_map['increase'] += 1
        elif readings[i] < readings[i-1]:
            trend_map['decrease'] += 1
    return trend_map

def compute_entropy(data):
    # Misleading advanced computation
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def filter_outliers(data, threshold=1.5):
    # Irrelevant filtering logic that doesn't affect final result
    median = sorted(data)[len(data)//2]
    deviances = [abs(x - median) for x in data]
    mad = sorted(deviances)[len(deviances)//2]  # Median Absolute Deviation
    filtered = [x for x in data if abs(x - median) <= threshold * mad]
    return filtered  # Not used in critical path

def process_signal_noise_ratio(raw):
    # Distractor function with complex math
    signal = sum(x**2 for x in raw)
    noise = sum((raw[i+1] - raw[i])**2 for i in range(len(raw)-1))
    return math.sqrt(signal) / (math.sqrt(noise) + 1e-5)

def generate_synthetic_features(raw_readings):
    # Creates decoy variables
    features = {}
    features['peak_count'] = sum(1 for i in range(1, len(raw_readings)-1)
                             if raw_readings[i-1] < raw_readings[i] > raw_readings[i+1])
    features['valley_depth'] = min(raw_readings) - raw_readings[0]
    features['drift_rate'] = (raw_readings[-1] - raw_readings[0]) / len(raw_readings)
    return features

def main_pipeline():
    # Primary execution flow
    raw_data = acquire_raw_readings()
    
    # Irrelevant multi-step transformation chain
    calibrated = [calibrate_sensor(x) for x in raw_data]
    entropy_value = compute_entropy([int(x) for x in raw_data])  # Uses only integer parts
    snr = process_signal_noise_ratio(calibrated)
    
    # Critical path begins here — subtle and obscured
    base_values = [x for x in raw_data if x >= 24.0]  # Filter conditionally relevant data
    adjustment_factor = 0.85
    adjusted = [x * adjustment_factor for x in base_values]
    
    # Key intermediate: average of adjusted high readings
    avg_adjusted = sum(adjusted) / len(adjusted)
    
    # Secondary processing with dictionary operations
    stats = {}
    stats['count'] = len(base_values)
    stats['sum'] = sum(base_values)
    stats['avg_raw'] = stats['sum'] / stats['count']
    stats['avg_final'] = avg_adjusted
    
    # Data restructuring - core to actual answer
    processed_data = {
        'readings': base_values,
        'metrics': stats,
        'timestamp': 1712345678
    }
    
    # The real answer depends on this function
    final_diagnostic = analyze_readings(processed_data)
    
    # Print required output format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

def analyze_readings(data_dict):
    # Core logic hidden among distractions
    raw_list = data_dict['readings']
    metrics = data_dict['metrics']
    
    # Multiple red herring computations
    temp_debug = [math.sin(x) for x in raw_list]  # unused
    checksum = sum(int(math.cos(x) * 100) for x in raw_list)  # irrelevant
    
    # Actual key computation — 3-step derivation
    base_score = metrics['avg_raw'] * 10
    adjustment = len(raw_list) ** 2
    penalty = 0
    for val in raw_list:
        if val > 25:
            penalty += int(val - 25)
    
    # Final formula
    result = int(base_score + adjustment - (penalty * 5))
    
    # Early return masking complexity
    if result < 0:
        return 0
    
    return result

# Global decoy variables
system_status = {'initialized': True, 'version': '2.1.5', 'mode': 'diagnostic'}
calibration_cache = defaultdict(float)
error_log = []

# Execute main logic
if __name__ == '__main__':
    final_diagnostic = analyze_readings({
        'readings': [24.1, 25.3, 26.0, 24.8, 25.1, 24.4],
        'metrics': {
            'count': 6,
            'sum': 149.7,
            'avg_raw': 24.95,
            'avg_final': 21.2075
        },
        'timestamp': 1712345678
    })
    print(f"Result: {final_diagnostic}")