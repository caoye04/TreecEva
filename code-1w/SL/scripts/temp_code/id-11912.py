from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return entropy

def preprocess_metrics(raw_data):
    # Parse and filter sensor readings (some irrelevant)
    cleaned = [x for x in raw_data if 0 <= x <= 100]
    outlier_count = len(raw_data) - len(cleaned)
    stats = defaultdict(float)
    stats['avg'] = sum(cleaned) / len(cleaned) if cleaned else 0
    stats['peak'] = max(cleaned) if cleaned else 0
    stats['noise_floor'] = min(x for x in cleaned if x > 10) if any(x > 10 for x in cleaned) else 0
    return stats, outlier_count

def adjust_for_bias(value, bias_factor=1.0):
    # Unused bias correction (dead path)
    return value * (1 + bias_factor * 0.05)

def compute_weighted_segments(components, scaling):
    # Complex transformation with red herring logic
    temp_results = []
    cumulative = 0
    for i, val in enumerate(components):
        if i % 3 == 0:
            cumulative += val * scaling ** 2
        elif i % 3 == 1:
            cumulative += int(val / scaling)
        else:
            cumulative -= math.sqrt(val) if val > 0 else 0
        temp_results.append(cumulative)
    
    # Distractor: unused aggregation
    peak_temp = max(temp_results) if temp_results else 0
    decay_factor = peak_temp * 0.1
    
    # Actual relevant output
    return sum(temp_results) % 1000

def validate_integrity(trace_log):
    # Bit manipulation decoy
    checksum = 0
    for entry in trace_log:
        checksum ^= int(entry * 100) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF
    return checksum == 42

def evaluate_performance(metrics, weights):
    base_value = metrics['avg'] * weights[0]
    peak_bonus = (metrics['peak'] >= 90) * weights[1] * 10
    
    # Simulated complexity with conditional nesting (some paths irrelevant)
    adjustment = 0
    if metrics['avg'] > 75:
        if metrics['noise_floor'] < 25:
            adjustment += weights[2] * 5
        else:
            adjustment -= weights[2] * 2  # Dead branch due to data
    else:
        adjustment += weights[2]
    
    # Hidden dependency on list comprehension side-effect
    history = [18, 22, 19, 88, 91, 77, 65, 44, 30, 95]
    recent_highs = [h for h in history if h > 85]
    streak = len(recent_highs)
    
    if streak >= 3:
        adjustment += weights[3] * streak
    else:
        adjustment -= weights[3]  # Not taken
    
    # Core calculation buried in distractions
    raw_score = base_value + peak_bonus + adjustment
    
    # Final non-linear transformation (key step)
    final_score = int((raw_score ** 1.05) - 15) % 873
    
    # Red herring: unrelated string processing
    log_str = "perf_log_" + "_".join(map(str, recent_highs))
    encoded = ''.join(chr(97 + (ord(c) % 26)) for c in log_str if c.isdigit())
    
    return final_score

# Main execution with misleading setup
data_stream = [89, 92, 101, 73, -5, 95, 88, 105, 44, 33, 90, 77, 22]
trace = [0.1, 0.3, 0.4, 0.9]

# Unused variables (distractors)
max_capacity = 1024
scaling_factor = 2.5
reference_id = hash('baseline_v7')

# Preprocess phase
cleaned_metrics, errors_found = preprocess_metrics(data_stream)

# Weight configuration (hidden relevance)
weights_config = [1.2, 0.8, 1.5, 0.7]

# Irrelevant data structure transformation
summary_table = defaultdict(list)
for k, v in cleaned_metrics.items():
    summary_table[k].append(round(v * 1.1, 2))

# Key computation buried in flow
temp_diagnostic = compute_weighted_segments([10, 20, 30], scaling_factor)
integrity_ok = validate_integrity(trace)

# Critical statement
final_score = evaluate_performance(cleaned_metrics, weights_config)

print(f"Result: {final_score}")