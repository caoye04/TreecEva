import math

# Simulated sensor data processing pipeline with diagnostic logic
def collect_samples():
    raw = [14, 17, 23, 36, 42, 55, 61, 73, 88, 91]
    noise_floor = 15
    adjusted = [x - noise_floor if x > noise_floor else 0 for x in raw]
    return adjusted

def filter_outliers(data, limit=50):
    # Irrelevant filtering function (not used in final path)
    return [x for x in data if x < limit]

def generate_checksum(seq):
    # Distractor: generates a checksum but not used in main logic
    return sum(x ^ (i * 3) for i, x in enumerate(seq)) % 1000

def encrypt_segment(data):
    # Dead code path: looks important but unused
    key = 257
    return [(x ^ key) % 256 for x in data]

def normalize_readings(data):
    max_val = max(data)
    return [round(x / max_val, 6) for x in data]

def apply_calibration(signal, factors=None):
    if factors is None:
        factors = [1.1, 0.9, 1.05, 0.95, 1.0] * 20
    calibrated = []
    for i, val in enumerate(signal):
        factor = factors[i % len(factors)]
        calibrated.append(val * factor)
    return [round(x, 6) for x in calibrated]

def compute_entropy(data):
    # Misleading complexity: computes entropy but not used
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data if x > 0]
    return round(-sum(p * math.log2(p) for p in probabilities), 6)

def build_index_map(keys):
    # Unused helper that creates red herring variables
    return {k: i * 2 for i, k in enumerate(keys)}

def evaluate_stability(readings):
    diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return avg_diff < 0.1

def analyze_signal(data, config_map):
    # Core analysis logic
    base_weight = config_map['weight_a']
    scale_factor = config_map['scale_b']
    offset = config_map.get('offset', 0)

    # Key transformation
    transformed = [((x ** 2) * base_weight + offset) for x in data]
    
    # Conditional branch based on derived property
    if sum(transformed) > 1000:
        processed = [math.sqrt(x) for x in transformed if x > 0]
        processed = [p for p in processed if p > 2.0]
    else:
        processed = [x / scale_factor for x in transformed]

    # Further refinement using lambda and zip
    modifiers = [0.8, 1.2, 0.9, 1.1] * (len(processed)//4 + 1)
    processor = lambda val, mod: round(val * mod, 6)
    refined = [processor(v, m) for v, m in zip(processed, modifiers[:len(processed)])]

    # Final aggregation
    aggregate = sum(refined)
    adjustment = math.floor(aggregate / 100) if aggregate > 500 else math.ceil(aggregate / 50)
    result = int(aggregate - adjustment)

    # Critical answer variable
    final_diagnostic = result * 2
    return final_diagnostic

# Irrelevant data structures (distractors)
log_registry = {'entry_1': 'init', 'entry_2': 'calibrated'}
device_states = ['active', 'standby', 'error', 'active']
state_weights = {s: i + 1 for i, s in enumerate(device_states)}

# Main execution flow
samples = collect_samples()
normalized = normalize_readings(samples)
calibrated = apply_calibration(normalized)

# Generate irrelevant intermediate values
checksum = generate_checksum(calibrated)
entropy_metric = compute_entropy(calibrated)
stability_flag = evaluate_stability(calibrated)

# Build unused index structure
index_lookup = build_index_map(['A', 'B', 'C'])

# Real configuration map used in analysis
threshold_map = {
    'weight_a': 1.75,
    'scale_b': 0.5,
    'offset': 4
}

# Processed data actually used in final call
processed_data = [round(x * 100) for x in calibrated if x > 0.1]

# Key statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output result as required
print(f"Target result: {final_diagnostic}")