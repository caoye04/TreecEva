from itertools import combinations

def analyze_sequence(data):
    peak_count = 0
    temp_sum = 0
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peak_count += 1
        temp_sum += data[i] ** 2
    # Irrelevant smoothing operation
    smoothed = [data[0]] + [round((data[i-1] + data[i] + data[i+1]) / 3) for i in range(1, len(data)-1)] + [data[-1]]
    return peak_count

def validate_timing(ticks):
    intervals = [ticks[i+1] - ticks[i] for i in range(len(ticks)-1)]
    avg_interval = sum(intervals) / len(intervals)
    stable = all(abs(x - avg_interval) < 5 for x in intervals)
    # Dead computation - not used later
    jitter_score = sum(abs(intervals[i+1] - intervals[i]) for i in range(len(intervals)-1))
    return stable

def calculate_performance(results):
    raw_values = [r['score'] for r in results]
    weights = [0.1, 0.2, 0.3, 0.4]
    
    # Compute weighted average
    weighted_avg = sum(raw_values[i] * weights[i] for i in range(len(weights)))
    
    # Generate auxiliary metrics (some irrelevant)
    pair_correlations = []
    for a, b in combinations(range(len(raw_values)), 2):
        correlation = (raw_values[a] - raw_values[b]) ** 2
        pair_correlations.append(correlation)
    
    # Noise threshold filtering (unused path)
    filtered_pairs = [c for c in pair_correlations if c < 200]
    noise_level = len(pair_correlations) - len(filtered_pairs)
    
    # Key logic: adjust score based on pattern analysis
    trend_consistent = True
    for i in range(1, len(raw_values)):
        if raw_values[i] < raw_values[i-1]:
            trend_consistent = False
            break
    
    adjustment_factor = 1.1 if trend_consistent else 0.9
    
    # Secondary check using helper function
    timestamps = [r['timestamp'] for r in results]
    timing_valid = validate_timing(timestamps)
    
    if timing_valid:
        adjustment_factor *= 1.05
    
    # Final performance calculation
    base_metric = weighted_avg * adjustment_factor
    
    # Distractor: unused complexity with itertools
    windowed_sums = [sum(window) for window in combinations(raw_values, 3)]
    complexity_penalty = len(windowed_sums) > 5
    
    # Actual final score
    final_score = int(round(base_metric))
    
    # Additional red herring variables
    max_window_sum = max(windowed_sums) if windowed_sums else 0
    anomaly_flags = [x for x in raw_values if x < 50]
    
    return final_score

# Simulated benchmark results
benchmark_results = [
    {'score': 85, 'timestamp': 100, 'module': 'arith'},
    {'score': 88, 'timestamp': 104, 'module': 'logic'},
    {'score': 92, 'timestamp': 108, 'module': 'control'},
    {'score': 96, 'timestamp': 112, 'module': 'struct'}
]

# Trigger analysis chain
sequence_data = [10, 20, 15, 25, 18]
analyze_sequence(sequence_data)  # Warm-up call with side effect none

final_score = calculate_performance(benchmark_results)
print(f"Target result: {final_score}")