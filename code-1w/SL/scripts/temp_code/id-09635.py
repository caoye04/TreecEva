import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [18, 22, 19, 25, 30, 28, 20, 17]
    offset = 5
    adjusted = [x + offset for x in raw_readings]
    return adjusted

# Irrelevant helper - dead function (distractor)
def compute_efficiency_score(values):
    total = sum(values)
    score = total * 0.87 if total > 100 else total * 0.5
    return score  # never used

# Noise filtering using moving average (relevant)
def filter_noise(data):
    window_size = 3
    smoothed = []
    for i in range(len(data)):
        if i < window_size - 1:
            smoothed.append(data[i])
        else:
            window = data[i - window_size + 1:i + 1]
            smoothed.append(sum(window) / len(window))
    return smoothed

# Bit manipulation for error checking (relevant)
def detect_anomalies(values):
    anomaly_flags = 0
    for val in values:
        if val & 1:  # check least significant bit
            anomaly_flags ^= val  # XOR into flag
    return anomaly_flags

# Data categorization (partially relevant, partial red herring)
def categorize_levels(data):
    categories = {'low': [], 'medium': [], 'high': []}
    thresholds = {'low': 20, 'medium': 25}
    for x in data:
        if x < thresholds['low']:
            categories['low'].append(x)
        elif x < thresholds['medium']:
            categories['medium'].append(x)
        else:
            categories['high'].append(x)
    
    # Distractor computation - unused result
    summary_stats = {
        'count_low': len(categories['low']),
        'count_medium': len(categories['medium']),
        'count_high': len(categories['high'])
    }
    
    # Another decoy transformation
    weighted_sum = sum([v * 0.1 for v in categories['low']]) + \
                   sum([v * 0.2 for v in categories['medium']]) + \
                   sum([v * 0.3 for v in categories['high']])
    
    return categories  # returned but only length of high used later

# Signal processor combines multiple concepts (core logic)
def process_signal_sequence(raw):
    shifted = [x << 1 for x in raw]  # bit shift left by 1 (multiply by 2)
    clipped = [min(x, 50) for x in shifted]
    diff_pairs = [(clipped[i+1] - clipped[i]) for i in range(len(clipped)-1)]
    
    # Use itertools to generate combinations (red herring - unused)
    pair_combinations = list(itertools.combinations(diff_pairs, 2))
    avg_change = sum(diff_pairs) / len(diff_pairs) if diff_pairs else 0
    
    # Conditional expression used (required python feature)
    trend = 'rising' if avg_change > 0 else 'falling'
    
    # Decoy statistical measure
    variance_proxy = sum((x - avg_change) ** 2 for x in diff_pairs) / len(diff_pairs) if diff_pairs else 0
    
    return clipped, trend

# Main analyzer (relevant)
def analyze_signal(data):
    base_sum = sum(data)
    element_count = len(data)
    mean_val = base_sum / element_count
    
    # Recursive helper to compute multiplicative digital root (relevant)
    def multiplicative_digital_root(n):
        if n < 10:
            return n
        product = 1
        for digit in str(int(abs(n))):
            if digit != '0':
                product *= int(digit)
        return multiplicative_digital_root(product)
    
    mdr_result = multiplicative_digital_root(base_sum)
    
    # Set operation (relevant but subtle)
    unique_remainders = set(val % 7 for val in data)
    remainder_influence = sum(unique_remainders)
    
    # Destructuring assignment (required concept)
    first, *middle, last = data
    
    # Final computation chain
    temp_a = first * last
    temp_b = len(middle) * mdr_result
    temp_c = remainder_influence
    
    # Key formula
    intermediate = temp_a + temp_b - temp_c
    final_diagnostic = abs(intermediate) * (1 if len(unique_remainders) % 2 == 0 else -1)
    
    # Dead code path - misleading
    if final_diagnostic == 0:
        backup = sum(data[i] * (i+1) for i in range(len(data)))
        final_diagnostic = backup // 10
    
    return final_diagnostic

# --- Execution Flow ---
raw_sensor_data = collect_sensor_readings()

# Unused efficiency metric (distractor)
efficiency_metric = compute_efficiency_score(raw_sensor_data)

filtered_data = filter_noise(raw_sensor_data)
anomaly_code = detect_anomalies(filtered_data)
categorized_data = categorize_levels(filtered_data)
processed_data, trend_label = process_signal_sequence(filtered_data)

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")