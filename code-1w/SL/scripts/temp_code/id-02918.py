import itertools

def analyze_sequence(data_stream):
    # Irrelevant transformation: bit manipulation red herring
    masked_values = [d ^ 0xAB for d in data_stream if d % 3 != 0]
    shifted = [(v >> 2) & 0xFF for v in masked_values]
    return shifted[:len(data_stream)//2] if shifted else [0]

def validate_input(entries):
    # Dead code path: never actually used in main logic
    if not all(isinstance(e, int) for e in entries):
        raise ValueError('Invalid entry')
    return sorted(set(entries))

def compute_legacy_metric(x, y):
    # Distractor function: looks important but unused
    return (x ** 0.5 + y ** 0.5) * 1.618

def extract_features(signal):
    # Real but overcomplicated feature extraction with irrelevant parts
    features = []
    for i, val in enumerate(signal):
        if i % 4 == 0:
            features.append(val ** 2)
        elif i % 3 == 0:
            features.append(abs(val - 50))
    padded = list(itertools.zip_longest(features, [], fillvalue=1))
    return [f[0] for f in padded]

def evaluate_performance(log, weights):
    base = 0
    modifiers = {"latency": 1.2, "throughput": 0.8, "error_rate": -2.0}
    
    # Core relevant logic buried in noise
    for key, readings in log.items():
        if key == "latency":
            base += sum(readings) * weights[key]
        elif key == "throughput":
            base += max(readings) * weights[key]
        elif key == "error_rate":
            base += min(readings) * weights[key]
    
    # Decoy calculation with misleading intermediate
    temp_result = base * 0.95
    adjustment = 0
    for w in weights.values():
        adjustment += w ** 2
    final_score = int(base + adjustment)  # Final answer derived here
    
    # Unused branching distractor
    if temp_result > 1000:
        final_score *= 0.9
    
    return final_score

# Simulated monitoring data — meaningful input
metrics_log = {
    "latency": [120, 115, 130, 125],
    "throughput": [850, 870, 830, 860],
    "error_rate": [3, 5, 2, 4]
}

# Weights that matter
benchmark_weights = {
    "latency": 0.4,
    "throughput": 0.5,
    "error_rate": -1.0
}

# Dummy signal and data streams — irrelevant distractions
raw_signal = [23, 45, 67, 89, 12, 34, 56, 78]
dynamic_stream = list(range(97, 112))

# Unused but plausible-looking preprocessing
features_out = extract_features(raw_signal)
noise_filtered = analyze_sequence(dynamic_stream)

# Key execution point
final_score = evaluate_performance(metrics_log, benchmark_weights)

# Output result as required
print(f"Target result: {final_score}")