from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for environmental monitoring system
def collect_readings():
    raw_samples = [105, 92, 118, 99, 103, 112, 95, 108, 101, 97]
    timestamps = [1623456000 + i*60 for i in range(10)]
    return list(zip(timestamps, raw_samples))

def filter_outliers(data, threshold=1.5):
    values = [x[1] for x in data]
    q1 = sorted(values)[2]
    q3 = sorted(values)[7]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [entry for entry in data if lower_bound <= entry[1] <= upper_bound]

def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        smoothed.append(sum(series[start:i+1]) / (i - start + 1))
    return smoothed

def compute_checksum(data_list):
    # Irrelevant cryptographic checksum (red herring)
    chk = 0
    for val in data_list:
        chk = (chk * 31 + val) % 10007
    return chk

def analyze_trend(pattern):
    # Misleading trend analysis with unused result
    deltas = [pattern[i+1] - pattern[i] for i in range(len(pattern)-1)]
    pos = sum(1 for d in deltas if d > 0)
    neg = sum(1 for d in deltas if d < 0)
    return 'increasing' if pos > neg else 'decreasing'

def transform_signal(readings):
    # Signal transformation with decoy operations
    transformed = []
    phase_shift = 0.1
    for ts, val in readings:
        noise_component = (ts % 7) * 0.01
        signal = val * math.sin(phase_shift) + noise_component
        normalized = (signal + 1) / 2
        transformed.append(max(0, min(1, normalized)))
    return transformed

def generate_metadata(keys):
    # Dead code path - never used
    meta = defaultdict(str)
    for k in keys:
        meta[k] = f"processed_v2_{k.lower()[:3]}"
    return dict(meta)

def calculate_entropy(sequence):
    # Distractor function: looks important but unused
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def integrate_series(values):
    # Another red-herring integration function
    integral = 0
    for v in values:
        integral += abs(v) * 0.1
    return round(integral, 3)

def evaluate_performance(metrics, base):
    # Core logic buried among distractions
    adjustment_factor = 1.75
    penalty_rate = 0.02
    score = base
    
    # Key calculation chain
    for m in metrics:
        if m > 0.8:
            score *= adjustment_factor
        elif m < 0.3:
            score *= (1 - penalty_rate)
        
    # Final nonlinear transformation
    score = int(score ** 1.1) ^ 4321  # Bitwise obfuscation
    score = (score + 1234) % 50000
    return score

# Main execution with multiple diversions
if __name__ == '__main__':
    # Step 1: Collect raw data
    samples = collect_readings()
    
    # Step 2: Filter outliers (relevant)
    filtered_data = filter_outliers(samples)
    clean_values = [x[1] for x in filtered_data]
    
    # Step 3: Apply rolling average (partially relevant preprocessing)
    smoothed_readings = rolling_average(clean_values)
    
    # Step 4: Compute irrelevant checksum (distraction)
    checksum = compute_checksum(clean_values)
    
    # Step 5: Analyze non-existent trend (misdirection)
    trend_result = analyze_trend(smoothed_readings)
    
    # Step 6: Transform signal into normalized space (core relevance)
    processed_signal = transform_signal(filtered_data)
    
    # Step 7: Generate unused metadata (dead path)
    fields = ['Temperature', 'Humidity', 'Pressure']
    metadata_catalog = generate_metadata(fields)
    
    # Step 8: Calculate distracting entropy (irrelevant metric)
    entropy_value = calculate_entropy([round(x, 2) for x in processed_signal])
    
    # Step 9: Perform fake integration (more distraction)
    integral_measure = integrate_series(processed_signal)
    
    # Step 10: Extract key evaluation metrics (critical path)
    metric_data = [x for x in processed_signal if 0.1 <= x <= 0.95]  # Filtering valid metrics
    
    # Step 11: Set baseline from obscured calculation (hidden initial state)
    baseline = len(clean_values) * 250
    
    # Step 12: Evaluate performance - THIS IS THE KEY STATEMENT
    final_score = evaluate_performance(metric_data, baseline)
    
    # Output target result
    print(f"Result: {final_score}")