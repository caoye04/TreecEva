import math

# System calibration constants (some irrelevant)
default_offset = 0.7854
temporal_factor = 1.61803
dummy_thresholds = [0.1, 0.3, 0.6, 0.9]
scaling_matrix = [[2, -1], [1, 3]]

# Core logic inputs
base_signals = [0.45, 0.67, 0.23, 0.89, 0.51]
activation_flags = [True, False, True, True, False]

# Irrelevant transformation chain 1
def transform_sequence(seq):
    return [math.sin(x * temporal_factor) for x in seq if x > 0.25]

# Dummy model weights (unused in final calculation)
model_weights = {
    'layer_1': [0.2, 0.5],
    'layer_2': [0.8, 0.3],
    'layer_3': [0.6, 0.9]
}

# Misleading diagnostic function that appears important
def legacy_diagnostic(signal, weights):
    score = 0
    for i, w in enumerate(weights['layer_1']):
        score += w * math.cos(signal * i)
    return round(score, 4)

# Auxiliary function with red herring logic
def compute_resonance(values):
    resonance = 1.0
    for v in values:
        resonance *= (v + default_offset) % 1.1
    return resonance

# Data alignment via dictionary mapping (partially relevant)
position_map = {i: val for i, val in enumerate([x * 1.5 for x in base_signals])}

# Complex filter with distracting conditionals
def filter_critical_nodes(indices, flags, data_map):
    result_indices = []
    temp_cache = []
    for idx in indices:
        raw_val = data_map[idx]
        # Distracting nested conditions
        if flags[idx] and raw_val > 0.5:
            if idx % 2 == 0:
                temp_cache.append(raw_val * 1.2)
            else:
                temp_cache.append(raw_val * 0.8)
        elif not flags[idx]:
            temp_cache.append(-0.1 * raw_val)
        else:
            temp_cache.append(0)  # dead branch
        result_indices.append(idx * 2)  # irrelevant transformation
    return temp_cache  # only this matters

# Signal booster - looks important but unused
def boost_signal(signal_list, exponent=2):
    boosted = []
    for s in signal_list:
        boosted.append(s ** exponent if s > 0.5 else s)
    return boosted

# Core evaluation engine
logic_core = {
    'nodes': [{'id': i, 'signal': s, 'active': f} for i, (s, f) in enumerate(zip(base_signals, activation_flags))],
    'config': {'version': '2.1', 'mode': 'adaptive'}
}

class StabilityAnalyzer:
    def __init__(self, core_data):
        self.data = core_data
        self.internals = {}

    def extract_features(self):
        signals = [node['signal'] for node in self.data['nodes']]
        actives = [node['active'] for node in self.data['nodes']]
        weighted_sum = sum(s * (1.5 if a else 0.5) for s, a in zip(signals, actives))
        
        # Red herring feature computation
        self.internals['entropy'] = -sum(s * math.log(s) for s in signals if s > 0)
        self.internals['peak'] = max(signals)
        self.internals['legacy_score'] = legacy_diagnostic(weighted_sum, model_weights)
        
        # Actual relevant intermediate
        self.internals['adjusted_sum'] = weighted_sum * 0.85
        return self.internals['adjusted_sum']

    def validate_topology(self):
        ids = [node['id'] for node in self.data['nodes']]
        # Complex validation with decoy logic
        if all(id >= 0 for id in ids) and len(ids) == len(set(ids)):
            if sum(ids) % 2 == 0:
                return len(ids) * 1.1
            else:
                return len(ids) * 0.9
        return 0.0

    def assess_fluctuations(self, threshold_ref):
        signals = [node['signal'] for node in self.data['nodes']]
        variations = [abs(a - b) for a, b in zip(signals, signals[1:])]
        high_var_count = sum(1 for v in variations if v > 0.3)
        return high_var_count > threshold_ref

# Threshold configuration (mix of relevant and irrelevant entries)
thresholds = {
    'primary': 0.4,
    'secondary': 0.75,
    'stability_floor': 1.0,
    'fluctuation_limit': 2,
    'legacy_mode': False
}

# Secondary processing chain with misleading side effects
def apply_calibration(features, analyzer):
    calibrated = {}
    calibrated['level_a'] = features * 1.05
    calibrated['level_b'] = calibrated['level_a'] * 0.95
    
    # Fake recursive smoothing
    def smooth(val, depth):
        if depth <= 0 or val < 0.1:
            return val
        return 0.5 * smooth(val * 0.5, depth - 1) + 0.5 * val
    
    calibrated['smoothed'] = smooth(calibrated['level_b'], 3)
    analyzer.internals.update(calibrated)  # side effect, partially distracts
    return calibrated['smoothed']

# Main evaluation function
def evaluate_stability(core_data, config):
    analyzer = StabilityAnalyzer(core_data)
    
    # Step 1: Extract key features
    base_score = analyzer.extract_features()
    
    # Step 2: Apply fake calibration (modifies internals but not critical path)
    _ = apply_calibration(base_score, analyzer)
    
    # Step 3: Validate structure (result used later)
    topology_weight = analyzer.validate_topology()
    
    # Step 4: Assess dynamics
    is_unstable = analyzer.assess_fluctuations(config['fluctuation_limit'])
    
    # Step 5: Filter nodes through misleading pipeline
    indices = list(range(len(core_data['nodes'])))
    filtered_outputs = filter_critical_nodes(indices, [n['active'] for n in core_data['nodes']], position_map)
    
    # Step 6: Compute auxiliary metric (irrelevant)
    dummy_resonance = compute_resonance(base_signals)
    
    # Step 7: Aggregate real contributions
    aggregate = base_score * topology_weight
    
    # Step 8: Final adjustment based on stability check
    if is_unstable:
        aggregate *= 0.5
    else:
        aggregate *= 1.1
    
    # Step 9: Apply final non-linear transformation
    final_value = int((aggregate ** 2) / 2.5) + 33
    
    # Critical assignment point
    final_diagnostic = final_value
    
    # Dead code paths below
    if final_diagnostic < 0:
        final_diagnostic = 0
    elif final_diagnostic > 1000:
        final_diagnostic = 999  # never reached

    return final_diagnostic

# Execute main logic
final_diagnostic = evaluate_stability(logic_core, thresholds)
print(f"Result: {final_diagnostic}")