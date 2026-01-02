def analyze_readings(readings):
    cumulative = 0
    temp_adjustment = 0.78
    offset_tracker = []
    for idx, val in enumerate(readings):
        if idx % 3 == 0:
            cumulative += val * 1.1
        elif idx % 4 == 0:
            cumulative -= val * 0.9
        else:
            cumulative += val
        offset_tracker.append(cumulative * temp_adjustment)
    return offset_tracker

readings_data = [12, 18, 25, 30, 14, 22, 36, 41]
processed_offsets = analyze_readings(readings_data)

# Irrelevant transformation chain (dead path)
decoy_map = {i: x * 0.5 for i, x in enumerate(processed_offsets) if x > 20}
scaling_factor = sum(decoy_map.values()) if decoy_map else 1.0
temp_result = [x / scaling_factor for x in processed_offsets]  # unused

# Real data path begins here
raw_diagnostics = [sum(processed_offsets[:3]), sum(processed_offsets[3:5]), len(processed_offsets)]

# Misleading normalization block
normalization_cache = {}
for i in range(len(raw_diagnostics)):
    key = f"norm_{i}"
    normalized = raw_diagnostics[i] / (raw_diagnostics[-1] + 1e-6)
    normalization_cache[key] = round(normalized, 4)

# Core computation disguised among distractors
def apply_weighting(values, strategy='balanced'):
    weights = {
        'aggressive': [1.5, -0.2, 0.8],
        'conservative': [0.8, 0.3, 1.1],
        'balanced': [1.1, 0.5, 0.9]
    }
    
    # Dead function - never called
    def calculate_entropy(arr):
        total = sum(arr)
        return [-x/total * __import__('math').log(x/total) for x in arr]
    
    selected_weights = weights.get(strategy, weights['balanced'])
    weighted_sum = sum(v * w for v, w in zip(values, selected_weights))
    return weighted_sum

# Simulate alternate diagnostic paths (unused)
alt_diagnostics_a = apply_weighting(raw_diagnostics, 'aggressive')
alt_diagnostics_b = apply_weighting(raw_diagnostics, 'conservative')

# Actual signal processing pipeline
def process_metrics(metrics, weight_mode=None):
    base_vector = [m * 1.05 for m in metrics]
    adjustment_lookup = {i: base_vector[i] * 0.1 for i in range(len(base_vector))}
    
    # Secondary correction using dictionary mapping
    corrected = []
    for i, val in enumerate(base_vector):
        correction = adjustment_lookup.get(i, 0)
        if i % 2 == 0:
            corrected.append(val + correction)
        else:
            corrected.append(val - correction)
    
    # Final integration step
    integrated = 0
    for j, c in enumerate(corrected):
        if j == 0:
            integrated += c * 1.2
        elif j == 1:
            integrated += c * 0.85
        else:
            integrated += c * 1.0
    
    # Decoy side-effect (no impact)
    __log_entry = {'final_value': integrated, 'timestamp': 'ignored'}
    
    return round(integrated, 6)

weights = 'balanced'  # ignored in logic but looks relevant
final_diagnostic = process_metrics(raw_diagnostics, weights)
print(f"Target result: {final_diagnostic}")