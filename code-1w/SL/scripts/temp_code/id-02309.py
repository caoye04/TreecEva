from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation system
def collect_sensor_readings():
    readings = [15, 22, 15, 30, 22, 18, 30, 30, 25, 15]
    return readings

# Irrelevant audio processing stub (dead code path)
def analyze_frequency_spectrum(data):
    fft_result = []
    for i in range(len(data)):
        fft_result.append(sum([data[j] * math.sin(j * i) for j in range(3)]))
    return fft_result  # never used

# Misleading preprocessing function that looks important
def normalize_signal(x):
    if x > 25:
        return x * 0.85
    elif x < 20:
        return x * 1.1
    else:
        return x + 1

# Core data transformation pipeline
def transform_readings(raw):
    count_map = Counter(raw)
    adjusted = []
    for val in raw:
        if count_map[val] > 2:
            adjusted.append(val + 3)
        elif count_map[val] == 1:
            adjusted.append(val - 2)
        else:
            adjusted.append(val)
    return adjusted

# Decoy function: appears related but unused
def compute_entropy(data):
    total = len(data)
    probs = [freq / total for freq in Counter(data).values()]
    return -sum(p * math.log2(p) for p in probs)

# Auxiliary calculation with red herring variables
def calculate_baseline(readings):
    temp_shift = 0
    baseline = sum(readings) / len(readings)
    outlier_count = 0  # misleading counter
    
    for r in readings:
        if r > baseline * 1.3 or r < baseline * 0.7:
            outlier_count += 1
            temp_shift += 1  # unused accumulation
    
    # Actual adjustment logic
    if baseline < 20:
        baseline += 5
    else:
        baseline -= 2
    
    return int(baseline)

# Complex metric evaluator with set operations
def evaluate_metrics(readings):
    unique_values = set(readings)
    high_performers = {x for x in unique_values if x >= 25}
    mid_range = {x for x in unique_values if 18 <= x < 25}
    low_range = {x for x in unique_values if x < 18}
    
    # Distractor set operation
    overlap_check = high_performers & mid_range  # always empty
    
    score_a = len(high_performers) * 10
    score_b = len(mid_range) * 5
    penalty = len(low_range) * 3
    
    return score_a + score_b - penalty

# Main evaluation logic
def generate_diagnostics(data):
    diagnostics = defaultdict(list)
    for i, val in enumerate(data):
        if val % 2 == 0:
            diagnostics['even'].append((i, val))
        else:
            diagnostics['odd'].append((i, val))
    
    # Unused diagnostic accumulations
    diagnostics['flagged'] = [v for v in data if v > 28]
    diagnostics['corrected'] = [normalize_signal(v) for v in data]
    
    return dict(diagnostics)

# Final performance assessor - this is the key function
def evaluate_performance(metrics, dataset):
    base = calculate_baseline(dataset)
    metric_score = evaluate_metrics(dataset)
    
    # Critical logic step 1: transform data
    processed = transform_readings(dataset)
    
    # Critical logic step 2: use transformed mean
    avg_processed = sum(processed) / len(processed)
    
    # Critical logic step 3: combine scores
    raw_score = metric_score + base + avg_processed
    
    # Critical logic step 4: final nonlinear adjustment
    if raw_score > 60:
        final = raw_score * 0.95
    else:
        final = raw_score * 1.05
    
    return int(final)

# --- Execution Flow ---
if __name__ == '__main__':
    # Collect raw data
    raw_sensor_data = collect_sensor_readings()
    
    # Generate irrelevant analysis (distraction)
    signal_normalized = [normalize_signal(x) for x in raw_sensor_data]
    entropy_value = compute_entropy(raw_sensor_data)  # dead computation
    freq_analysis = analyze_frequency_spectrum(raw_sensor_data)  # unused
    
    # Build diagnostic report (partly irrelevant)
    health_report = generate_diagnostics(raw_sensor_data)
    
    # Define key variables for target question
    metric_set = {'type': 'performance', 'version': '2.1'}
    benchmark_data = raw_sensor_data
    
    # Execute target statement
    final_score = evaluate_performance(metric_set, benchmark_data)
    
    print(f"Target result: {final_score}")