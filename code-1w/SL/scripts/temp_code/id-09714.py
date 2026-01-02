from collections import defaultdict, Counter
import math

# Simulated system metrics with irrelevant and relevant fields
def generate_metrics():
    data = defaultdict(float)
    data['throughput'] = 120.5
    data['latency_ms'] = 45.2
    data['error_rate'] = 0.034
    data['cache_hit_ratio'] = 0.88
    data['retry_count'] = 3
    data['bandwidth_util'] = 76.4
    data['temp_debug_ignored'] = 999.0  # red herring
    data['power_draw_watts'] = 150.2
    return data

# Irrelevant helper that looks important
def calculate_efficiency_index(x, y):
    if x <= 0 or y <= 0:
        return 0
    return (x * y) / (x + y)

# Decoy function – never actually used in critical path
def analyze_stability_flags(flags):
    score = 0
    for flag in flags:
        if flag.startswith('ERR'):
            score -= 10
        elif flag == 'OK':
            score += 5
    return score  # unused result

# Another decoy: processes string logs but not used in final calculation
def parse_log_entry(log_line):
    parts = log_line.split('|')
    timestamp = parts[0]
    level = parts[1].strip()
    message = parts[2].strip()
    char_freq = Counter(message)
    suspicious_chars = sum(1 for c in message if c in '\\/?*')
    return suspicious_chars > 3  # irrelevant to main logic

# Core metric transformation with distractions
def transform_metric(value, name):
    if name == 'latency_ms':
        return 100 - min(value, 100)
    elif name == 'error_rate':
        return max(0, 100 * (1 - value))
    elif name == 'throughput':
        return min(value / 1.5, 100)
    elif name.endswith('_ratio') or name.endswith('_util'):
        return value  # already percentage-like
    else:
        return abs(hash(name)) % 100  # fallback for unknown (distraction)

# Main scoring logic buried among noise
def evaluate_performance(metrics, config):
    raw_values = []
    weights = {
        'throughput': 0.25,
        'latency_adjusted': 0.30,
        'error_free_score': 0.20,
        'cache_hit_ratio': 0.15,
        'bonus_factor': 0.10
    }

    # Transform relevant metrics
    for key, val in metrics.items():
        transformed = transform_metric(val, key)
        raw_values.append((key, transformed))

    # Build working dictionary
    processed = dict(raw_values)

    # Compute derived values — some are distractions
    processed['latency_adjusted'] = processed.get('latency_ms', 0)
    processed['error_free_score'] = processed.get('error_rate', 0)
    processed['bonus_factor'] = 0.0

    # Secret bonus logic: only triggered by specific condition
    if metrics['retry_count'] < 5 and metrics['error_rate'] < 0.05:
        # Hidden XOR-based validator (bit manipulation)
        key_seed = int(metrics['latency_ms'] * 10) ^ int(metrics['throughput'])
        key_seed = key_seed & 0xFF  # keep in byte range
        if key_seed % 7 == 0:  # rare condition
            processed['bonus_factor'] = 15.0
        else:
            processed['bonus_factor'] = 5.0  # misleading default
    else:
        processed['bonus_factor'] = 0.0

    # Distractor block: complex but unused computation
    debug_snapshot = []
    for k, v in processed.items():
        debug_snapshot.append(f"{k}={v:.2f}")
    snapshot_str = '|'.join(debug_snapshot)
    anomaly_detected = 'CRIT' in snapshot_str  # always False

    # Actual weighted score
    total_score = 0.0
    weight_sum = 0.0
    for metric_name, weight in weights.items():
        value = processed.get(metric_name, 0.0)
        total_score += value * weight
        weight_sum += weight

    normalized_score = total_score / weight_sum

    # Final adjustment using modular arithmetic
    int_part = int(normalized_score)
    fractional = normalized_score - int_part
    checksum = (int_part % 97 + int(fractional * 1000)) % 11
    final_normalized = normalized_score + (checksum * 0.01)

    # Redundant clamp
    final_normalized = max(0.0, min(final_normalized, 100.0))

    # This variable is the real answer
    final_score = round(final_normalized * 100) / 100  # two decimal precision

    # Dead code: looks like logging but commented out
    # print(f"[DEBUG] Final integrity: {final_score % 1:.3f}")

    return final_score

# Unused configuration objects (distractors)
benchmark_config = {
    'version': '2.1a',
    'strict_mode': True,
    'debug_trace': False,
    'timeout_sec': 30
}

metric_set = generate_metrics()

# Simulated log entries that look analyzable but aren't used
logs_pool = [
    "2024-05-01 10:00:01| INFO | System initialized",
    "2024-05-01 10:00:02| DEBUG | temp_debug_ignored=42",
    "2024-05-01 10:00:03| WARN | Retry attempt #1"
]

for entry in logs_pool:
    parse_log_entry(entry)  # side-effect free, distractor

# Flags that feed into unused analysis
stability_flags = ['OK', 'OK', 'ERR_TIMEOUT', 'OK']
analyze_stability_flags(stability_flags)  # call with no effect

# Critical execution point
final_score = evaluate_performance(metric_set, benchmark_config)

# Output the target result
print(f"Target result: {final_score}")