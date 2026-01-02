import math

# Simulated system diagnostics (irrelevant data)
def analyze_health(status_codes):
    threshold = 75
    return sum(1 for code in status_codes if code > threshold)

# Decoy function - never called
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Misleading utility with unused result
def normalize_vector(vec):
    norm = math.sqrt(sum(x ** 2 for x in vec))
    return [x / norm for x in vec] if norm else vec

# Unused transformation chain
temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
avg_temp = sum(temp_readings) / len(temp_readings)
deviations = [(t - avg_temp) ** 2 for t in temp_readings]
variance = sum(deviations) / len(deviations)

# Core data structures
metrics_log = {
    'latency_ms': [120, 110, 135, 105, 140],
    'throughput_ops': [850, 900, 870, 920, 855],
    'error_rate': [0.02, 0.01, 0.03, 0.01, 0.04],
    'memory_mb': [450, 470, 460, 480, 455]
}

benchmark_weights = {
    'latency_ms': -0.3,      # Negative weight: lower is better
    'throughput_ops': 0.4,   # Positive weight: higher is better
    'error_rate': -0.25,      # Negative weight
    'memory_mb': -0.05       # Minor penalty
}

# Red herring list comprehension
_ = [math.ceil(w * 100) for w in benchmark_weights.values() if w < 0]

# Intermediate transformations (some relevant, some not)
processed = {}
for key, values in metrics_log.items():
    if key == 'latency_ms':
        processed[key] = sum([max(0, 150 - v) for v in values])  # bonus for low latency
    elif key == 'throughput_ops':
        processed[key] = sum([min(1000, v) // 10 for v in values])
    elif key == 'error_rate':
        processed[key] = sum([int(100 * (1 - min(0.1, e) * 10)) for e in values])
    else:
        processed[key] = 0  # ignored in final calculation

# Dead code branch (never executed due to logic)
if sum(processed.get('memory_mb', [])) > 1000:
    processed['throughput_ops'] *= 1.1

# Auxiliary calculation with decoy variables
total_bonus = 0
decoys = [1.5, 2.3, 0.7, 4.1]
for i, val in enumerate(decoys):
    total_bonus += math.sin(val) ** 2 + math.cos(val) ** 2  # always 1 per iteration

# Actual scoring logic buried in distractions
def evaluate_performance(log, weights):
    score_components = {}
    
    # Irrelevant pre-checks
    valid_keys = set(weights.keys())
    log_keys = set(log.keys())
    if not valid_keys.intersection(log_keys):
        return -1
    
    aggregate = {}
    for k in weights:
        if k in log:
            raw_values = log[k]
            if k == 'latency_ms':
                # Normalize by ideal baseline
                aggregate[k] = sum([(120 / max(v, 1)) * 0.8 for v in raw_values[:3]])
            elif k == 'throughput_ops':
                aggregate[k] = sum([t * 0.001 for t in raw_values])
            elif k == 'error_rate':
                aggregate[k] = sum([(1 - min(e, 0.05)) * 50 for e in raw_values])
            else:
                aggregate[k] = 10  # dummy fallback
    
    # Weighted combination
    total = 0.0
    for metric, weight in weights.items():
        if metric in aggregate:
            total += aggregate[metric] * abs(weight)  # use absolute weight magnitude
    
    # Final adjustment based on hidden rule: only first 3 latency samples count double
    latency_contribution = (log['latency_ms'][0] + log['latency_ms'][1] + log['latency_ms'][2])
    if latency_contribution < 370:
        total += 15  # performance bonus
    
    return int(total)

# Secondary distraction: set operations with no impact
critical_metrics = {'latency_ms', 'throughput_ops'}
optional_metrics = {'error_rate', 'memory_mb', 'cache_hit_ratio'}
redundant = critical_metrics | optional_metrics
missing = optional_metrics - log_keys

# String manipulation decoy
diagnostic_tag = "SYS_" + "".join([k[:2].upper() for k in sorted(log_keys)[:3]])

# Key execution point
final_score = evaluate_performance(metrics_log, benchmark_weights)

# Irrelevant formatting
result_str = f"{diagnostic_tag}: {final_score:+.1f}"

# Target result output
Result: {final_score}