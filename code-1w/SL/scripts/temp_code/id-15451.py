import math

# Simulated sensor fusion system for environmental diagnostics
def analyze_harmonics(frequency_grid):
    harmonic_peaks = []
    for row in frequency_grid:
        for val in row:
            if val > 0 and math.log(val) % 1 < 0.1:
                harmonic_peaks.append(int(math.sqrt(val)))
    return sorted(set(harmonic_peaks))

def generate_reference_key(peaks):
    key = 0
    for i, p in enumerate(peaks):
        key += p * (31 ** i)
    return key % 10000

def compute_entropy(data_stream):
    # Irrelevant entropy calculation - red herring
    from collections import Counter
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0
    for count in counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 6)

def validate_signal_integrity(signal_chain, metadata):
    # Complex validation with multiple distractors
    checksum = 0
    for i, s in enumerate(signal_chain):
        if i % 3 == 0:
            checksum += (s ^ (i + 1)) & 255
        elif i % 4 == 2:
            checksum -= (s >> (i % 8)) ^ 17
    # Decoy computation
    normalization_factor = sum([x**2 for x in signal_chain if x > 50])
    if normalization_factor > 0:
        normalized = [x / math.sqrt(normalization_factor) for x in signal_chain]
        avg_norm = sum(normalized) / len(normalized)
    return checksum % 500 == metadata.get('token', 0)

def build_threshold_map(config_layers):
    # Real but partially misleading configuration builder
    base_map = {}
    decoy_acc = 0
    for layer in config_layers:
        tag = layer['tag']
        mode = layer['mode']
        if mode == 'adaptive':
            base_map[tag] = int(math.exp(layer['scale']))
        elif mode == 'static':
            base_map[tag] = layer['value']
        else:
            decoy_acc += layer.get('buffer', 0)  # Dead accumulation path
    # Additional irrelevant transformation
    temp_offsets = [v * 0.9 for v in base_map.values() if v > 10]
    scaling_hint = sum(temp_offsets) / len(temp_offsets) if temp_offsets else 0
    return base_map

def aggregate_diagnostic(signal_chain, threshold_map):
    # Core logic buried within distractions
    raw_energy = sum(x for x in signal_chain if x > 0)
    peak_count = len([x for x in signal_chain if x > 75])
    
    # Real dependency on map values
    adjustment = 0
    for key, thresh in threshold_map.items():
        if 'gamma' in key:
            adjustment += thresh // 10
        elif 'beta' in key:
            adjustment -= thresh % 25
    
    # Distractor: complex-looking but unused structure
    diagnostic_cube = [[[signal_chain[i] ^ j for j in range(3)] for i in range(len(signal_chain))] for _ in range(2)]
    cube_trace = sum(diagnostic_cube[0][i][i % 3] for i in range(min(len(signal_chain), 3)))
    
    # Actual formula for answer
    score_component_1 = raw_energy // 10
    score_component_2 = peak_count * 12
    net_adjustment = adjustment * 3
    
    # Final computation
    result = score_component_1 + score_component_2 + net_adjustment
    
    # Unused but plausible-looking refinement
    if result > 100:
        refined = result * 0.95
        refined = math.floor(refined) if refined % 2 else math.ceil(refined)
    
    return result

# Orchestration code with setup and red herrings
def main():
    # Sensor data input (real)
    signal_chain = [12, 45, 78, 88, 95, 33, 67, 91, 24, 82, 76, 55, 99]
    
    # Configuration layers (mixed relevance)
    config_layers = [
        {'tag': 'gamma_probe', 'mode': 'adaptive', 'scale': 2.3},
        {'tag': 'beta_shield', 'mode': 'static', 'value': 64},
        {'tag': 'omega_link', 'mode': 'dynamic', 'buffer': 150},
        {'tag': 'gamma_anchor', 'mode': 'adaptive', 'scale': 2.1},
        {'tag': 'beta_node', 'mode': 'static', 'value': 37}
    ]
    
    # Frequency grid for harmonic analysis (distractor)
    frequency_grid = [
        [16, 25, 36, 49],
        [64, 81, 100, 121],
        [144, 169, 196, 225]
    ]
    
    # Metadata for validation (partially used)
    metadata = {
        'version': '3.2.1',
        'token': 482,
        'active': True
    }
    
    # Trigger harmonic analysis (red herring function call)
    harmonic_signatures = analyze_harmonics(frequency_grid)
    ref_key = generate_reference_key(harmonic_signatures)
    
    # Compute entropy on signal (irrelevant but plausible)
    stream_pattern = [x % 10 for x in signal_chain]
    pattern_entropy = compute_entropy(stream_pattern)
    
    # Build actual threshold map needed for aggregation
    threshold_map = build_threshold_map(config_layers)
    
    # Validate integrity - returns False but not used in final calc
    is_valid = validate_signal_integrity(signal_chain, metadata)
    
    # Key statement containing the target variable assignment
    filtration_score = aggregate_diagnostic(signal_chain, threshold_map)
    
    # Print final result as required
    print(f"Result: {filtration_score}")

if __name__ == "__main__":
    main()