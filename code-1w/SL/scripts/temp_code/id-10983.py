import math

def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    peaks = 0
    for i in range(1, len(seq)-1):
        if seq[i-1] < seq[i] > seq[i+1]:
            peaks += 1
    return peaks

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * math.log(p)
    return round(entropy, 6)

def transform_signal(data, key=5):
    # Irrelevant transformation with decoy logic
    shifted = [(x + key) % 256 for x in data]
    filtered = [x for x in shifted if x % 2 == 0]
    return [x ^ 17 for x in filtered]  # Dead end path

def evaluate_stability(rhythm):
    diffs = [abs(rhythm[i] - rhythm[i-1]) for i in range(1, len(rhythm))]
    variance = sum(d**2 for d in diffs) / len(diffs) if diffs else 0
    return variance < 15

def calculate_checksum(records):
    # Distractor function - looks important but unused in final result
    chk = 0
    for r in records:
        chk = (chk + r * 113) % 10007
    return chk

def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]

def aggregate_metrics(data):
    # Core logic embedded within noise
    baseline = data.get('baseline', [])
    signals = data.get('signals', [])
    events = data.get('events', [])
    
    # Irrelevant preprocessing
    transformed = transform_signal(signals, key=7)
    checksum = calculate_checksum(signals)  # Red herring
    
    # Relevant computation begins
    norm_baseline = normalize_readings(baseline)
    avg_baseline = sum(norm_baseline) / len(norm_baseline) if norm_baseline else 0
    
    event_count = len(events)
    pattern_score = analyze_pattern(events)
    entropy_metric = compute_entropy(baseline)
    
    # Conditional expression with meaningful impact
    adjustment_factor = 1.5 if evaluate_stability(events) else 0.8
    
    # Lambda used for dynamic thresholding
    severity_index = lambda x: 1 + math.log(1 + x)
    
    # Dictionary operations to combine metrics
    metrics_dict = {
        'base': avg_baseline * 100,
        'complexity': severity_index(pattern_score) * event_count,
        'entropy': entropy_metric * 10,
        'stability': adjustment_factor * 10
    }
    
    # Final calculation - only this contributes to answer
    raw_score = sum(metrics_dict.values())
    final_diagnostic = int(round(raw_score * 1.76))
    
    # Unused variables - distractions
    dummy_1 = [transformed, checksum, severity_index(9)]
    dummy_2 = {'temp': 0, 'flag': False}
    
    return final_diagnostic

# Simulated health monitoring data
health_data = {
    'baseline': [85, 90, 95, 100, 92, 88, 94],
    'signals': [120, 150, 130, 140, 160, 135],
    'events': [70, 78, 85, 79, 88, 92, 87],
    'timestamp': '2023-11-05T14:30:00Z',
    'device_id': 'HMD-7X'
}

# Key execution point
final_diagnostic = aggregate_metrics(health_data)
print(f"Result: {final_diagnostic}")