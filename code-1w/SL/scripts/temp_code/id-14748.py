from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic evaluation
def collect_readings():
    raw_streams = [
        [12, 15, 12, 18, 12, 21],
        [9, 11, 9, 14, 9, 17],
        [6, 8, 6, 10, 6, 13]
    ]
    return raw_streams

def filter_anomalies(streams):
    cleaned = []
    for s in streams:
        avg = sum(s) / len(s)
        filtered = [x for x in s if abs(x - avg) < 10]
        cleaned.append(filtered)
    return cleaned

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_frequencies(data):
    # Irrelevant function - decoy
    freq_map = defaultdict(int)
    for row in data:
        for val in row:
            freq_map[val] += 1
    return freq_map

def accumulate_trends(dataset):
    # Dead code path - never used
    trends = []
    for seq in dataset:
        trend = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
        trends.append(trend)
    return trends

def normalize_series(data):
    flattened = [item for sublist in data for item in sublist]
    min_val, max_val = min(flattened), max(flattened)
    if max_val == min_val:
        return [0.5] * len(flattened)
    return [(x - min_val) / (max_val - min_val) for x in flattened]

def derive_signature(norm_vals):
    # Misleading intermediate computation
    sig = 0
    for i, v in enumerate(norm_vals):
        sig += v * math.sin(i)
    return round(sig, 6)

def partition_by_quantile(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    q1 = sorted_vals[n//4]
    q3 = sorted_vals[3*n//4]
    low = [x for x in values if x < q1]
    mid = [x for x in values if q1 <= x <= q3]
    high = [x for x in values if x > q3]
    return {'low': low, 'mid': mid, 'high': high}

def evaluate_stability(bins):
    stability_score = 0
    if len(bins['low']) > 0:
        stability_score += sum(bins['low']) / len(bins['low'])
    if len(bins['high']) > 0:
        stability_score -= sum(bins['high']) / len(bins['high'])
    return int(stability_score)

def build_threshold_map(config_id):
    # Complex but partially irrelevant mapping
    base_map = defaultdict(float)
    base_map.update({
        't1': 0.15, 't2': 0.25, 't3': 0.45, 't4': 0.65,
        'alpha': 1.1, 'beta': 0.9, 'gamma': 1.3
    })
    
    adjustment = math.cos(config_id * 0.1)
    for k in base_map:
        if 't' in k:
            base_map[k] *= (1 + adjustment * 0.1)
    
    # Only 't3' and 't4' are actually used later
    return base_map

def transform_readings(clean_data):
    # Core transformation
    transposed = []
    for i in range(len(clean_data[0])):
        col = [row[i] for row in clean_data if i < len(row)]
        transposed.append(col)
    
    processed = []
    for col in transposed:
        shifted = [x << 1 for x in col]  # Bit shift: relevant
        powered = [x ** 0.5 for x in shifted]  # Square root
        rounded = [round(x, 2) for x in powered]
        processed.append(rounded)
    
    return processed

def analyze_pattern(grid, thresholds):
    # Main analysis logic
    t3_val = thresholds['t3']
    t4_val = thresholds['t4']
    
    aggregate = []
    for row in grid:
        for val in row:
            if val > t3_val and val < t4_val:
                aggregate.append(val * 100)
    
    if not aggregate:
        return -1
    
    # Key computation
    mean_agg = sum(aggregate) / len(aggregate)
    deviation_sum = 0
    for a in aggregate:
        deviation_sum += abs(a - mean_agg)
    
    # Final result based on controlled logic chain
    final_value = int(mean_agg - (deviation_sum / len(aggregate)))
    
    # Irrelevant post-processing (dead end)
    if final_value > 100:
        temp = final_value
        for _ in range(3):
            temp = (temp ^ 0xF) % 17
    
    return final_value

# --- Execution Flow ---
data_source = collect_readings()
cleaned_readings = filter_anomalies(data_source)

# Irrelevant calls - red herrings
decoy_freqs = generate_frequencies(cleaned_readings)
decoy_trends = accumulate_trends(cleaned_readings)
normalized_vector = normalize_series(cleaned_readings)
fake_signature = derive_signature(normalized_vector)

partitioned = partition_by_quantile(normalized_vector)
stab_index = evaluate_stability(partitioned)

threshold_map = build_threshold_map(config_id=7)
transformed_data = transform_readings(cleaned_readings)
final_diagnostic = analyze_pattern(transformed_data, threshold_map)
print(f"Target result: {final_diagnostic}")