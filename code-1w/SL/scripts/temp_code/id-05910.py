from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    raw_data = [23.4, 24.1, 22.8, 25.0, 23.9, 24.2, 23.7, 24.6]
    timestamps = [1623456780 + i*60 for i in range(len(raw_data))]
    return list(zip(timestamps, raw_data))

def filter_outliers(data, threshold=1.5):
    values = [x[1] for x in data]
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [d for d in data if lower_bound <= d[1] <= upper_bound]

def rolling_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        avg = sum([data[i+j][1] for j in range(window)]) / window
        smoothed.append((data[i+window//2][0], round(avg, 2)))
    return smoothed

def calculate_trend(series):
    diffs = [series[i+1][1] - series[i][1] for i in range(len(series)-1)]
    return sum(diffs) / len(diffs)

def compress_data(binary_sequence):
    # Irrelevant function - simulates bit manipulation red herring
    result = 0
    for bit in binary_sequence:
        result = (result << 1) | bit
    return result

def generate_checksum(structure):
    # Decoy function - not used in main logic
    if isinstance(structure, dict):
        return sum(len(str(v)) for v in structure.values())
    return 0

def analyze_distribution(readings):
    counts = defaultdict(int)
    for ts, val in readings:
        bucket = int(val // 0.5) * 0.5
        counts[bucket] += 1
    return dict(counts)

def merge_datasets(ds1, ds2):
    # Dead code path - never called
    combined = {}
    for k in set(ds1.keys()) | set(ds2.keys()):
        combined[k] = ds1.get(k, 0) + ds2.get(k, 0)
    return combined

def normalize_scale(value, old_min, old_max, new_min, new_max):
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

def evaluate_performance(metrics, base):
    score = 0
    weights = {'stability': 0.4, 'consistency': 0.3, 'drift': 0.2, 'density': 0.1}
    
    # Key computation path
    stability = abs(base['mean'] - metrics['mean'])
    consistency = metrics['std_dev']
    drift = abs(metrics['trend'])
    density = metrics['mode_freq']
    
    # Distractor: irrelevant weight adjustments
    temp_weights = {k: v * 1.0 for k, v in weights.items()}
    temp_weights['phantom'] = 0.05  # Unused
    
    # Actual scoring
    score += weights['stability'] * (100 - min(stability * 10, 100))
    score += weights['consistency'] * (100 - min(consistency * 8, 100))
    score += weights['drift'] * (100 - min(drift * 50, 100))
    score += weights['density'] * min(density * 25, 100)
    
    # More distractions: unused transformations
    candidate_scores = [score * f for f in [0.95, 1.0, 1.05]]
    capped = [min(s, 100) for s in candidate_scores]
    
    return round(score, 4)

# Main execution flow
data_stream = collect_readings()
filtered_readings = filter_outliers(data_stream)
smoothed_data = rolling_average(filtered_readings, window=2)

trend_value = calculate_trend(smoothed_data)
distribution = analyze_distribution(smoothed_data)

# Generate various intermediate metrics (many are distractions)
stat_summary = {
    'count': len(smoothed_data),
    'mean': sum(x[1] for x in smoothed_data) / len(smoothed_data),
    'std_dev': (sum((x[1] - sum(x[1] for x in smoothed_data)/len(smoothed_data))**2 for x in smoothed_data) / len(smoothed_data))**0.5,
    'trend': trend_value,
    'mode_freq': max(Counter(round(x[1], 1) for x in smoothed_data).values())
}

# Irrelevant bit sequence transformation
binary_pattern = [1, 0, 1, 1, 0, 1, 0, 0, 1]
encoded = compress_data(binary_pattern)

# Unused data structure
summary_table = defaultdict(list)
for key, val in stat_summary.items():
    summary_table['processed'].append(normalize_scale(val, 0, 100, 0, 1))

# Baseline configuration (simulated)
baseline_config = {
    'mean': 24.0,
    'std_dev': 0.5,
    'trend': 0.0,
    'mode_freq': 3
}

# Critical statement
final_score = evaluate_performance(stat_summary, baseline_config)

# Print result
print(f"Result: {final_score}")