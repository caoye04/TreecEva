import itertools

# Simulated sensor array diagnostics with embedded signal processing
sensor_ids = [101, 102, 103, 104]
diagnostic_flags = {'calibrated': True, 'no_noise': False, 'baseline_set': True}

# Irrelevant historical thresholds (distractor data)
historical_thresholds = {
    't1': 0.85, 't2': 0.91, 't3': 0.77, 't4': 0.66,
    't5': 0.55, 't6': 0.49, 't7': 0.72, 't8': 0.88
}

def generate_phase_shift(seq):
    # Unused function - red herring
    return [x * 0.9 + 0.1 for x in seq if x > 0.5]

def compute_entropy(data):
    # Computationally irrelevant to final result
    import math
    return -sum(p * math.log2(p) for p in data if p > 0)

# Real signal preprocessing chain
def preprocess_signal(raw_signals):
    filtered = []
    for s in raw_signals:
        if s < 0.1:
            continue
        adjusted = s * 1.05 if s < 0.5 else s * 0.98
        filtered.append(round(adjusted, 4))
    return filtered

# Misleading intermediate transformation (not used in final path)
temp_amplitudes = [0.31, 0.48, 0.62, 0.71, 0.39]
processed_amplitudes = [a**2 for a in temp_amplitudes if a > 0.4]

# Core data generation
raw_trend_data = [0.12, 0.33, 0.51, 0.67, 0.81, 0.44, 0.29]
signal_sequence = preprocess_signal(raw_trend_data)  # [0.126, 0.3465, 0.4998, 0.6566, 0.7938, 0.4312, 0.3045]

# Bit manipulation layer (partially relevant)
def apply_mask(value, mask=0b1101):
    shifted = int(value * 100)
    return shifted ^ mask  # XOR with mask

masked_values = [apply_mask(v) for v in signal_sequence]

# Decoy statistical analysis
mean_masked = sum(masked_values) / len(masked_values)
variance_proxy = sum((x - mean_masked)**2 for x in masked_values) / len(masked_values)

# Real control flow with nested conditions and tuple unpacking
def evaluate_stability(metrics):
    if len(metrics) < 5:
        return (False, 0)
    
    # Tuple unpacking and destructuring
    first, *middle, last = metrics
    peak = max(middle)
    
    if first < 10 or last < 10:
        status = 'unstable'
    elif peak > 70 and diagnostic_flags['calibrated']:
        status = 'stable'
    else:
        status = 'conditional'
    
    score = (peak + last) // 2
    return (status == 'stable', score)

stability_flag, stability_score = evaluate_stability(masked_values)

# Weight assignment with dictionary default fallbacks (some keys unused)
weight_config = {
    'base': 0.4,
    'adaptive': 0.3,
    'legacy_mode': 0.1,  # unused parameter
    'fallback': 0.2
}

weights = [
    weight_config.get('base'),
    weight_config.get('adaptive'),
    weight_config.get('fallback'),
    0.1  # hardcoded residual weight
]

# Use of itertools: zipping signal with cycling weights
trend_sequence = list(itertools.islice(itertools.cycle(signal_sequence), 12))

# Critical function: aggregate_metrics affects final answer
def aggregate_metrics(seq, w):
    total = 0.0
    # Nested loop with modular arithmetic indexing
    for i in range(len(seq)):
        weight_index = i % len(w)
        contribution = seq[i] * w[weight_index]
        if i % 3 == 0:
            contribution *= 1.1  # boost every third term
        elif i % 4 == 0:
            contribution *= 0.95
        total += contribution
    
    # Final adjustment using bitwise AND on scaled total
    scaled = int(total * 100)
    flag_mask = 0b11111111
    adjusted_scaled = scaled & flag_mask  # Apply bit mask
    return round(adjusted_scaled / 100.0, 6)

# Dead code path - never executed
if __debug__:
    debug_log = """
    Starting full diagnostic trace...
    Sensor sync: OK
    Clock drift: NOMINAL
    Noise floor: WITHIN TOLERANCE
    """

# Key execution point
final_diagnostic = aggregate_metrics(trend_sequence, weights)

# Result output
print(f"Target result: {final_diagnostic}")