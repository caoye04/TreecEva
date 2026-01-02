import math

def preprocess_signals(data_stream):
    # Irrelevant preprocessing (distractor)
    filtered = [x for x in data_stream if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return [math.sin(x) for x in normalized]

def compute_hash(sequence):
    # Decoy function: looks important but unused in critical path
    acc = 0
    for i, val in enumerate(sequence):
        acc += val * (i + 1)
    return acc % 1000

def analyze_phase_shifts(ticks):
    # Dead code path — never called
    shifts = []
    for i in range(1, len(ticks)):
        shifts.append(ticks[i] - ticks[i-1])
    return shifts

def evaluate_stability(rhythm):
    # Distractor computation with misleading intermediate
    baseline = sum(rhythm) / len(rhythm)
    variance = sum((x - baseline) ** 2 for x in rhythm) / len(rhythm)
    threshold = 0.5 if variance < 0.3 else 1.2
    return [x for x in rhythm if abs(x - baseline) < threshold]

def extract_features(signal):
    # Unused feature extraction (red herring)
    magnitude = sum(abs(x) for x in signal)
    peaks = [i for i, x in enumerate(signal) if i > 0 and signal[i-1] < x > signal[i+1]]
    return {'magnitude': magnitude, 'peaks': len(peaks)}

def aggregate_metrics(log, flags):
    # Core logic buried in noise
    stage_weights = {k: v * 1.5 for k, v in {'init': 2, 'sync': 3, 'flow': 4}.items()}
    
    # Real computation starts here
    timing_values = [entry['t'] for entry in log if entry['active']]
    duration = timing_values[-1] - timing_values[0]
    
    # Bit manipulation decoy
    bit_encoded = 0
    for t in timing_values[:3]:
        bit_encoded ^= int(t) & 0xF
    
    # Real aggregation
    total_impulse = sum(int(t * 100) % 7 for t in timing_values)
    flag_score = sum(1 for f in flags if f in ['OK', 'READY']) * 10
    
    # Set operation distraction
    expected_flags = {'OK', 'READY', 'STANDBY'}
    missing = expected_flags - set(flags)
    penalty = len(missing) * 5
    
    # Slicing distraction
    recent_logs = log[-5:]
    recent_avg = sum(entry['t'] for entry in recent_logs) / len(recent_logs)
    
    # Dictionary-based weighting
    category_map = {}
    for entry in log:
        cat = entry.get('cat', 'unknown')
        category_map[cat] = category_map.get(cat, 0) + 1
    
    # Actual answer computation
    base_metric = total_impulse + flag_score - penalty
    adjustment = len(category_map) * 3
    final_value = int(base_metric + adjustment - duration)
    
    return final_value

# Simulated system telemetry
timing_log = [
    {'t': 10.2, 'active': True, 'cat': 'init'},
    {'t': 15.7, 'active': False, 'cat': 'sync'},  # inactive
    {'t': 20.1, 'active': True, 'cat': 'sync'},
    {'t': 25.3, 'active': True, 'cat': 'flow'},
    {'t': 30.8, 'active': True, 'cat': 'flow'},
    {'t': 35.0, 'active': True, 'cat': 'flow'}
]

system_flags = ['OK', 'READY', 'PENDING']

# Unused variables (distractors)
data_stream = [0.1, -0.2, 0.4, 0.8, -0.3]
processed = preprocess_signals(data_stream)
hash_code = compute_hash([10, 20, 30])
features = extract_features(processed)

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output result
print(f"Result: {final_diagnostic}")