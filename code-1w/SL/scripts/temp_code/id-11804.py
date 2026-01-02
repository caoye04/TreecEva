from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor data stream (real-world context: health monitoring system)
def generate_telemetry():
    return [102, 95, 110, 98, 105, 103, 97, 100, 101, 99]

# Irrelevant helper - distractor function
def analyze_rhythm(pattern):
    rhythm_score = 0
    for i in range(len(pattern) - 1):
        if pattern[i] < pattern[i+1]:
            rhythm_score += 2
        else:
            rhythm_score -= 1
    return rhythm_score * 0.5  # Never actually used

# Decoy transformation - looks important but unused
def normalize_signal(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Misleading aggregation path
def compute_baseline(samples):
    total = sum(samples)
    count = len(samples)
    average = total / count if count > 0 else 0
    baseline_flag = average > 100
    return average * 1.0, baseline_flag

# Core logic disguised among distractions
def evaluate_stability(readings, config):
    window_size = config.get('window', 3)
    tolerance = config.get('tolerance', 5)
    
    # Real computation begins
    deviations = []
    for i in range(len(readings) - window_size + 1):
        window = readings[i:i+window_size]
        window_avg = sum(window) / len(window)
        center_val = window[window_size // 2]
        dev = abs(center_val - window_avg)
        deviations.append(dev)
    
    # Actual key metric
    instability_index = sum(d > tolerance for d in deviations)
    return instability_index  # Used later

# Main processing with red herrings
def process_metrics(sensors, limits):
    # Irrelevant counters
    stats = defaultdict(int)
    event_log = []
    
    # Dead code path - looks like error handling
    if not sensors:
        return -999
    
    # Meaningless categorization
    classification = Counter()
    for val in sensors:
        if val < 98:
            classification['low'] += 1
        elif val > 102:
            classification['high'] += 1
        else:
            classification['normal'] += 1
    
    # Unused smoothing
    smoothed = []
    for a, b in zip_longest(sensors, sensors[1:], fillvalue=0):
        smoothed.append((a + b) / 2.0)
    
    # Real work hidden here
    threshold_value = limits['critical']
    extreme_count = sum(1 for x in sensors if x > threshold_value)
    
    # Secondary real computation
    config = {'window': 3, 'tolerance': 4}
    stability = evaluate_stability(sensors, config)
    
    # Critical distraction: complex-looking but irrelevant bitwise op
    magic_key = 0
    for x in sensors[:5]:
        magic_key ^= (x << 2) | (x >> 1)
    
    # Final calculation - only this matters
    diagnostic_weight = 7
    adjustment_factor = 3
    base_score = extreme_count * diagnostic_weight
    final_diagnostic = base_score - (stability * adjustment_factor)
    
    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Global constants that seem important but partially unused
SYSTEM_WIDE_CONFIG = {
    'sampling_rate': 10,
    'calibration_offset': 0.05,
    'critical': 108,
    'version': '2.1a'
}

THRESHOLDS = {
    'warning': 100,
    'critical': 104  # This is the one that matters
}

# Simulate incoming data
raw_stream = generate_telemetry()
health_data = raw_stream[:]  # Copy to avoid mutation issues

# Call that drives everything
final_diagnostic = process_metrics(health_data, THRESHOLDS)
