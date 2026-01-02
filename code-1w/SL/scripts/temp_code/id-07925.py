def analyze_trend(values, threshold=0.5):
    if len(values) < 2:
        return False
    trend = all(v1 <= v2 for v1, v2 in zip(values, values[1:]))
    volatility = sum(abs(a - b) for a, b in zip(values, values[1:])) / len(values)
    return trend and volatility < threshold

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from math import log
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Unused but misleading transformation
def transform_signal(signal):
    transformed = []
    for i, s in enumerate(signal):
        if i % 3 == 0:
            transformed.append(s * 1.1)
        elif i % 3 == 1:
            transformed.append(s * 0.9)
        else:
            transformed.append(s)
    return [round(t, 3) for t in transformed]

# Dead code path with confusing intermediate calculations
def deprecated_normalization(vec):
    mean_val = sum(vec) / len(vec)
    std_dev = (sum((x - mean_val)**2 for x in vec) / len(vec)) ** 0.5
    normalized = [(x - mean_val) / std_dev for x in vec]
    return [round(n, 4) for n in normalized]

# Core logic disguised among distractions
def evaluate_dimension(dims):
    if not dims:
        return 0
    avg_dim = sum(dims) / len(dims)
    adjusted = [d for d in dims if d > avg_dim * 0.8]
    return sum(adjusted) // len(adjusted) if adjusted else 0

def evaluate_metrics(metals):
    weights = {'iron': 0.1, 'copper': 0.2, 'aluminum': 0.15, 'zinc': 0.25, 'nickel': 0.3}
    score = 0
    for metal, data in metals.items():
        purity = data.get('purity', 0)
        quantity = data.get('quantity', 0)
        score += weights.get(metal, 0) * (purity * quantity)
    return round(score, 3)

# Critical function with embedded distractors
def evaluate_performance(metrics_dict, base):
    # Distractor variables
    temp_cache = {}
    debug_log = []
    accumulator = 0
    
    # Real logic begins
    dimensions = metrics_dict.get('dimensions', [])
current_dim_score = evaluate_dimension(dimensions)

    # Misleading conditional that looks important but isn't decisive
    if current_dim_score > base * 1.2:
        debug_log.append('dimension_over_threshold')
        accumulator += 10
    elif current_dim_score < base * 0.8:
        debug_log.append('dimension_under_threshold')
        accumulator -= 5

    # Actual key metric
    material_composition = metrics_dict.get('materials', {})
    material_score = evaluate_metrics(material_composition)

    # Another decoy calculation
    signal_input = metrics_dict.get('signals', [])
    if signal_input:
        noise_floor = sum(s**2 for s in signal_input) / len(signal_input)
        snr = max(signal_input) / (noise_floor**0.5 + 1e-6)
        temp_cache['snr'] = round(snr, 3)

    # Main scoring logic hidden among noise
    adjustment_factor = 1.0
    if 'alignment' in metrics_dict:
        alignment_list = metrics_dict['alignment']
        if analyze_trend(alignment_list, threshold=0.4):
            adjustment_factor *= 1.15

    # Red herring: unused dictionary operations
    stats_summary = {
        'max_dimension': max(dimensions) if dimensions else 0,
        'min_purity': min((v.get('purity', 1) for v in material_composition.values()), default=1),
        'entry_count': len(material_composition)
    }
    stats_summary['range'] = stats_summary['max_dimension'] - stats_summary['min_purity']
    stats_summary['flagged'] = stats_summary['range'] > 5

    # Final computation — only this matters
    raw_performance = current_dim_score * 2.5 + material_score * 100
    final_score = int(raw_performance * adjustment_factor)
    
    # This print is required
    return final_score

# Setup realistic input with irrelevant fields
dummy_signals = [0.1, 0.15, 0.2, 0.22, 0.25]
metric_data = {
    'dimensions': [3, 5, 4, 6, 5],
    'materials': {
        'aluminum': {'purity': 0.92, 'quantity': 150},
        'copper': {'purity': 0.98, 'quantity': 80},
        'zinc': {'purity': 0.88, 'quantity': 120}
    },
    'signals': dummy_signals,
    'alignment': [1.0, 1.05, 1.1, 1.12, 1.15],  # Trending upward
    'calibration': {'offset': 0.01, 'gain': 1.02}
}
baseline = 4

# Execute critical statement
final_score = evaluate_performance(metric_data, baseline)
print(f"Result: {final_score}")