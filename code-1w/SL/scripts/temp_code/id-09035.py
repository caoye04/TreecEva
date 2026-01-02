from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental diagnostics
def collect_readings():
    raw_samples = [127, 63, 255, 91, 182]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

def analyze_peaks(signal):
    peak_threshold = 100
    peaks = [x for x in signal if x > peak_threshold]
    peak_count = len(peaks)
    avg_peak = sum(peaks) / peak_count if peaks else 0
    return {'count': peak_count, 'average': avg_peak}

def compute_checksum(data):
    # Irrelevant cryptographic red herring
    checksum = 0
    for val in data:
        checksum ^= int(val)
    return checksum % 1000

def derive_entropy(signal):
    # Misleading complexity: unused entropy analysis
    total = sum(signal)
    if total == 0:
        return 0.0
    normalized = [s / total for s in signal]
    entropy = -sum(p * math.log2(p) for p in normalized if p > 0)
    return round(entropy, 4)

def filter_anomalies(log_entries):
    # Dead code path — never invoked
    anomalies = []
    for entry in log_entries:
        if entry.get('severity') > 3:
            anomalies.append(entry)
    return anomalies

def generate_timeline(events):
    # Unused timeline generator with string manipulation distraction
    timeline = {}
    for e in events:
        ts = e['timestamp']
        day = ts.split('T')[0].replace('-', '')
        if day not in timeline:
            timeline[day] = []
        timeline[day].append(e['type'])
    return {k: Counter(v) for k, v in timeline.items()}

def validate_sequence(pattern):
    # Decoy validation function with bitwise operations
    acc = 0
    for i, p in enumerate(pattern):
        acc += (p & (i + 1)) ^ (p >> 2)
    return acc % 17 == 0

def aggregate_metrics(timing_data, flags):
    base_score = sum(timing_data) / len(timing_data)
    flag_weights = {'urgent': 3, 'deferred': -2, 'normal': 1}
    adjustment = sum(flag_weights.get(f, 0) for f in flags)
    
    # Critical logic step: apply exponential backoff on high variance
    variance = sum((x - base_score) ** 2 for x in timing_data) / len(timing_data)
    if variance > 500:
        base_score = base_score * math.exp(-variance / 1000)
    
    # Incorporate bit-based status encoding (only some bits matter)
    status_flag = 0
    for f in flags:
        if 'u' in f:
            status_flag |= 4
        elif 'd' in f:
            status_flag |= 1
    if status_flag & 4:
        base_score += 15.0
    
    # Final transformation using dictionary lookup and string parsing
    mode_code = 'A1'
    mode_map = {'A1': 1.1, 'B2': 0.9, 'C3': 1.0}
    mode_multiplier = mode_map.get(mode_code, 1.0)
    
    result = base_score * mode_multiplier + adjustment
    return int(round(result))

# Main execution flow
if __name__ == '__main__':
    # Collect sensor data
    readings = collect_readings()
    
    # Extract timing-related features
    timing_data = [r * 1.1 for r in readings if r > 50]
    timing_data.append(45.5)
    
    # Analyze signal characteristics (some results ignored)
    analysis = analyze_peaks(readings)
    entropy_metric = derive_entropy(readings)  # Computed but not used
    checksum = compute_checksum(readings)       # Distractor metric
    
    # Flag generation with mixed relevance
    flags = ['normal', 'urgent', 'normal', 'deferred']
    
    # Simulate unused data structures
    log_entries = [
        {'timestamp': '2023-11-05T14:23:01', 'severity': 2, 'type': 'read'},
        {'timestamp': '2023-11-05T14:25:17', 'severity': 4, 'type': 'write'}
    ]
    event_pattern = [127, 63, 255]
    validate_sequence(event_pattern)  # Called but result unused
    
    # Generate irrelevant timeline
    generate_timeline(log_entries)
    
    # Core computation
    final_diagnostic = aggregate_metrics(timing_data, flags)
    
    # Output target result
    print(f"Result: {final_diagnostic}")