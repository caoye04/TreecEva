from collections import defaultdict, Counter

# Simulated system metrics for performance analysis
cpu_load = [0.65, 0.72, 0.58, 0.81, 0.77]
memory_usage = [0.78, 0.82, 0.69, 0.85, 0.74]
disk_io = [0.45, 0.52, 0.61, 0.58, 0.55]
network_latency = [120, 95, 134, 110, 102]

def normalize_metrics(raw_values):
    return [round(val * 100, 2) for val in raw_values]

def calculate_trend(data):
    """Irrelevant function - not used in final computation"""
    changes = []
    for i in range(1, len(data)):
        changes.append(data[i] - data[i-1])
    return changes

def filter_outliers(values, threshold=1.5):
    """Dead code path - never called"""
    median_val = sorted(values)[len(values)//2]
    return [v for v in values if abs(v - median_val) < threshold]

def analyze_peaks(signal):
    peaks = 0
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks += 1
    return peaks if peaks > 0 else 1  # Avoid division by zero later (decoy)

# Irrelevant transformations
norm_cpu = normalize_metrics(cpu_load)
norm_memory = normalize_metrics(memory_usage)
temp_buffer = [x + 5 for x in norm_cpu]  # Distractor buffer

# Core metric data used in evaluation
metric_data = {
    'latency_ms': network_latency,
    'error_rate': [0.002, 0.003, 0.001, 0.004, 0.002],
    'throughput': [480, 520, 460, 540, 500]
}

# Misleading baseline calculations
baseline_latency = sum(network_latency) / len(network_latency)
adjusted_throughput = [tp * (1 - err) for tp, err in zip(metric_data['throughput'], metric_data['error_rate'])]

# Unused statistical analysis
freq_count = Counter([round(x, -1) for x in metric_data['throughput']])  # Grouped by tens
usage_pattern = defaultdict(int)
for val in metric_data['error_rate']:
    usage_pattern[round(val, 3)] += 1

# Decoy thresholds
safety_margin = 0.15
grace_period = 3
stale_threshold = 90  # Not actually used

base_threshold = 475
scaling_factor = 1.08

# Conditional expression with red herring branch
evaluation_mode = 'strict' if base_threshold > 450 else 'relaxed'
bonus_applied = False

# Key function that computes the final result
def evaluate_performance(metrics, threshold):
    score = 0
    peak_latency = max(metrics['latency_ms'])
    avg_error = sum(metrics['error_rate']) / len(metrics['error_rate'])
    total_throughput = sum(metrics['throughput'])
    
    # Real logic starts here
    if total_throughput >= threshold:
        score += 40
        if peak_latency < 130:
            score += 30
            recent_errors = metrics['error_rate'][-2:]
            if all(e <= 0.003 for e in recent_errors):
                score += 25
                # Complex conditional expression with embedded logic
                adjustment = (1.2 if avg_error < 0.0025 else 1.1) if evaluation_mode == 'strict' else 1.0
                score = int(score * adjustment)
                
                # Bit manipulation decoy (looks important but unused)
                binary_flag = 0b1010 ^ 0b1100 & 0b1111
                encoded_shift = (binary_flag << 2) >> 1
                
                # Final multiplier based on trend (but trend function was never properly defined for this)
                throughput_trend = metrics['throughput'][-1] - metrics['throughput'][0]
                if throughput_trend > 0:
                    score += 15
            else:
                score += 10
        else:
            score += 15
    else:
        score += 20
        
    # Dead code block - looks like it affects score but doesn't
    if bonus_applied:
        extra = 0
        for val in temp_buffer:
            if val > 70:
                extra += 2
        score += extra
        
    # Final adjustment using string method (unusual but valid distractor)
    key_string = "performance_boost_activated"
    if 'boost' in key_string and key_string.endswith('ed'):
        # This condition is true but only adds fixed amount
        score += 5
    
    return score

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Result: {final_score}")