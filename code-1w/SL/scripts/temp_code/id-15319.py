import math

# Simulated sensor data and configuration
raw_samples = [0.78, 1.23, -0.45, 2.01, 3.12, -1.05, 0.99, 1.02, 2.5, -0.88]
offsets = [0.1, -0.2, 0.3, -0.4, 0.5]
calibration_map = {i: math.sin(i * 0.5) for i in range(1, 6)}

# Irrelevant pre-processing (distractor)
decoy_buffer = [x ** 2 for x in raw_samples if x < 0]
temp_shift = sum(offsets) * 0.01

# Real signal processing begins
filtered_data = [x for x in raw_samples if abs(x) > 0.5]

# Misleading transformation chain (dead path)
shadow_copy = filtered_data[:]
for i in range(len(shadow_copy)):
    shadow_copy[i] = shadow_copy[i] * math.cos(i)  # Not used later

# Configuration with decoy keys
config = {
    'gain': 1.5,
    'threshold': 1.0,
    'mode': 'aggressive',
    'useless_metric': sum(decoy_buffer),
    'debug_level': temp_shift
}

# Auxiliary function that appears important but has red herrings
def analyze_pattern(data, cfg):
    magnitude = sum(abs(x) for x in data)
    peaks = [x for x in data if x > cfg['threshold']]
    score = len(peaks) * cfg['gain']
    
    # Fake complexity
    history_log = {f'step_{i}': score / (i + 1) for i in range(3)}
    return {'total_power': magnitude, 'valid_peaks': len(peaks), 'score': score}

# Another unused helper to increase interference
def validate_consistency(arr):
    if not arr:
        return False
    diff_arr = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    avg_change = sum(diff_arr) / len(diff_arr)
    return abs(avg_change) < 1.0

# Core logic buried in distractions
def transform_entry(val, idx, cfg):
    adjusted = val * cfg['gain']
    if adjusted > cfg['threshold']:
        adjusted = adjusted ** 0.5  # root compression
    return round(adjusted, 3)

# Main processor with conditional branching and slicing
def process_signal(signal, settings):
    # Early exit red herring
    if settings.get('mode') == 'invalid':
        return -999

    # Slicing to focus on middle segment
    trimmed = signal[1:-1]  # Exclude first and last

    # Bitwise distraction with no real effect
    control_flag = 0b1010
    mode_mask = 0b1100
    if control_flag & mode_mask:
        pass  # Placeholder branch

    # Actual transformation
    processed = []
    for i, val in enumerate(trimmed):
        new_val = transform_entry(val, i, settings)
        processed.append(new_val)
    
    # Secondary filter based on transformed values
    cleaned = [x for x in processed if x != 0]

    # Final aggregation buried in noise
    baseline = settings['gain'] * len(cleaned)
    fluctuation = max(cleaned) - min(cleaned)
    
    # Decoy dictionary operations
    stats = {
        'count': len(processed),
        'base_calc': baseline,
        'swing': fluctuation,
        'extra_field': calibration_map.get(len(processed), 0)
    }
    
    # Critical computation
    net_effect = sum(cleaned) + stats['base_calc']
    
    # Distractor: unused complex structure
    summary_tree = {
        'root': {
            'leaf_1': [net_effect / 2],
            'leaf_2': {'value': net_effect * 0.1}
        }
    }
    
    # The real answer
    final_scalar = int(round(net_effect, 0))
    return final_scalar

# Unused analysis calls (increase interference)
dummy_analysis = analyze_pattern(raw_samples, config)
consistency_check = validate_consistency(filtered_data)

# Key execution point
final_output = process_signal(filtered_data, config)

# Output result as required
print(f"Result: {final_output}")