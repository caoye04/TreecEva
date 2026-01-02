def analyze_signal_strength(raw_samples, config):
    sample_stats = {}
    temp_accum = 0
    max_val = float('-inf')
    min_val = float('inf')
    
    for idx, val in enumerate(raw_samples):
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
        temp_accum += abs(val)

    avg_abs = temp_accum / len(raw_samples) if raw_samples else 0
    
    # Irrelevant normalization path (dead logic)
    normalized = []
    if config.get('normalize', False):
        range_val = max_val - min_val or 1
        normalized = [(x - min_val) / range_val for x in raw_samples]

    # Distractor: unused frequency analysis
    freq_count = {}
    for v in raw_samples:
        rounded = round(v)
        freq_count[rounded] = freq_count.get(rounded, 0) + 1

    # Actual relevant filtering
    noise_floor = config.get('noise_floor', 0.5)
    filtered_data = [s for s in raw_samples if abs(s) > noise_floor]

    # Unused peak detection
    peaks = []
    for i in range(1, len(filtered_data) - 1):
        if filtered_data[i] > filtered_data[i-1] and filtered_data[i] > filtered_data[i+1]:
            peaks.append(i)

    return filtered_data, avg_abs, max_val


def build_threshold_map(bounds_config):
    # Complex distractor logic with partial relevance
    base_map = {}
    fallback_used = False
    
    for key, rng in bounds_config.items():
        if isinstance(rng, dict) and 'low' in rng and 'high' in rng:
            mid = (rng['low'] + rng['high']) / 2
            base_map[key] = {
                'center': mid,
                'range': abs(rng['high'] - rng['low'])
            }
        else:
            base_map[key] = {'center': 0, 'range': 1}
            fallback_used = True

    # Dead code: unused transformation
    if fallback_used:
        backup = {k: v['center'] * 2 for k, v in base_map.items()}
        _ = [x for x in backup.values() if x > 1]  # Unused list comp

    # Only this part is actually used later
    return {k: v['center'] for k, v in base_map.items()}


def process_signals(data, thresholds):
    if not data or not thresholds:
        return 0
    
    # Real computation begins
    signal_sum = sum(data)
    adjustment_factor = thresholds.get('primary', 1.0)
    secondary_boost = thresholds.get('secondary', 0.0)
    
    # Red herring: complex tuple unpacking with unused values
    extras = [(i, x, x**2, x**3) for i, x in enumerate(data) if x > 0]
    indices, values, squares, cubes = zip(*extras) if extras else ([], [], [], [])
    
    # Meaningful but obscured logic
    magnitude_class = 'high' if abs(signal_sum) > 10 else 'low'
    class_multiplier = {'high': 3, 'low': 1}[magnitude_class]
    
    # Conditional expression with distractor variables
    spike_count = len([v for v in data if v > 5])
    bonus = spike_count * 0.5 if spike_count > 2 else (-1 * len(values))  # Partially misleading

    # Actual formula for final result
    raw_output = signal_sum * adjustment_factor * class_multiplier
    final_output = int(raw_output + bonus + secondary_boost)
    
    # Irrelevant set operations
    unique_squares = set(squares)
    odd_squares = {s for s in unique_squares if s % 2 == 1}
    large_odds = odd_squares - {s for s in odd_squares if s < 50}  # Unused
    
    return final_output

# Main execution
config_settings = {
    'noise_floor': 0.75,
    'normalize': True  # Triggers dead path in analysis
}

bounds = {
    'primary': {'low': 2.0, 'high': 4.0},
    'secondary': {'low': -1.0, 'high': 1.0},
    'spare': 'invalid_entry'  # Triggers fallback in map builder
}

raw_input_samples = [1.2, -0.3, 0.1, 6.5, -2.4, 8.1, 0.0, 7.3, -1.8, 9.0]

# Key processing steps
filtered, average_magnitude, global_max = analyze_signal_strength(raw_input_samples, config_settings)
threshold_map = build_threshold_map(bounds)
final_output = process_signals(filtered, threshold_map)

print(f"Result: {final_output}")