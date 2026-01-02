from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental monitoring
def acquire_raw_data():
    return [23.4, 19.5, 20.1, 24.0, 18.2, 22.8, 19.9, 25.3, 20.0, 18.9]

def apply_calibration(raw_values, factor=1.02, offset=0.5):
    # Real processing step: calibrate sensor readings
    return [(v * factor) + offset for v in raw_values]

def filter_outliers(data, threshold=1.5):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

def compute_rolling_average(values, window_size=3):
    rolling = []
    for i in range(len(values) - window_size + 1):
        rolling.append(sum(values[i:i+window_size]) / window_size)
    return rolling

def detect_peaks(series, min_threshold=None):
    if min_threshold is None:
        min_threshold = sum(series) / len(series)
    peaks = []
    for i in range(1, len(series)-1):
        if series[i] > series[i-1] and series[i] > series[i+1] and series[i] >= min_threshold:
            peaks.append(i)
    return peaks

def generate_metadata(timestamps=None):
    # Irrelevant metadata generation (distractor)
    if timestamps is None:
        timestamps = list(range(100, 200, 10))
    meta_map = defaultdict(int)
    for t in timestamps[:5]:
        meta_map[f'node_{t % 7}'] += (t * 0.3) % 5
    return dict(meta_map)

def calculate_entropy(data):
    # Misleading complexity: entropy calculation not used in final result
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def derive_trend_score(readings):
    # Unused trend analysis (dead code path)
    diffs = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    pos = sum(1 for d in diffs if d > 0)
    neg = sum(1 for d in diffs if d < 0)
    return (pos - neg) * 10

def slice_window(data, start=1, end=-1, step=1):
    # Slicing abstraction that's actually used
    return data[start:end:step]

def aggregate_zones(readings):
    # Group readings into zones based on ranges
    zones = defaultdict(list)
    for val in readings:
        if val < 20.5:
            zones['low'].append(val)
        elif val < 22.5:
            zones['medium'].append(val)
        else:
            zones['high'].append(val)
    return {k: round(sum(v)/len(v), 3) if v else 0 for k, v in zones.items()}

def analyze_readings(processed):
    # Core logic with nested dependencies
    segmented = slice_window(processed, start=1, end=7, step=2)  # [1], [3], [5] from processed
    rolled = compute_rolling_average(segmented, window_size=2)
    zone_stats = aggregate_zones(rolled)
    
    # Critical computation chain
    base = zone_stats['medium'] if 'medium' in zone_stats else 0
    modifier = len([x for x in rolled if x > 21.0])
    adjustment = math.sin(math.pi * modifier / 4)
    
    # Final diagnostic derived from filtered path
    intermediate = base * (modifier + 1)
    final_value = int(intermediate + adjustment)
    
    # Red herring: unused complex structure
    diagnostics = {
        'entropy': calculate_entropy(processed),
        'peaks': detect_peaks(processed),
        'trend_score': derive_trend_score(processed),
        'zone_summary': zone_stats
    }
    
    return final_value

# Execution flow with distractions
raw_sensor_data = acquire_raw_data()
processed_signals = apply_calibration(raw_sensor_data)
cleaned_signals = filter_outliers(processed_signals)

# Dead assignment: metadata not used
sensor_metadata = generate_metadata()

# Another red herring variable
system_diagnostics = {
    'calibration_factor': 1.02,
    'outlier_threshold': 1.5,
    'active_sensors': [f'S{idx}' for idx in range(len(raw_sensor_data)) if idx % 3 == 0]
}

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Print required output
print(f"Result: {final_diagnostic}")