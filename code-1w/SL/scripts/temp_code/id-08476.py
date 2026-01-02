def analyze_pattern(sequence, mode='strict'):
    if mode == 'strict':
        return sum((i * v) for i, v in enumerate(sequence)) % 7
    return sum(v ** 2 for v in sequence if v % 3 == 0)

# Irrelevant helper (distractor)
def decrypt_key(token):
    return ''.join(chr((ord(c) - 97 - 3) % 26 + 97) for c in token.lower())

# Unused function (dead code path)
def legacy_calibrate(x):
    return x >> 2 if x > 100 else x << 1

# Core data structures
signal_stream = [12, 5, 8, 19, 3, 7, 11]
offset_table = {k: k**2 % 13 for k in range(10)}

# Misleading intermediate computation
baseline_correction = sum(signal_stream[i] + offset_table.get(i, 0) for i in range(len(signal_stream))) // len(signal_stream)

# Decoy variable with plausible but unused logic
risk_flag = any(signal_stream[i] > signal_stream[i+1] for i in range(len(signal_stream)-1)) and baseline_correction > 10

# Conditional expression with nested logic
adjustment_factor = 1.5 if all(x % 2 == 1 for x in signal_stream[:4]) else 0.8

# Primary transformation chain
filtered_readings = [x for x in signal_stream if x % 2 == 0]
eval_score = analyze_pattern(filtered_readings, mode='strict' if len(filtered_readings) < 5 else 'relaxed')

# Bit manipulation red herring
bit_diagnostic = (eval_score << 2) ^ 0b1101 & 255

# String-based decoy processing
status_tag = "ALERT" if bit_diagnostic > 100 else "OK"
enriched_log = f"[DIAG-{bit_diagnostic:03d}] Status:{status_tag}"

# Unused lambda (distractor)
validate_entry = lambda x: x.isdigit() and int(x) in offset_table

# Complex data structure with cross-references
threshold_map = {
    'low':  min(filtered_readings) * adjustment_factor if filtered_readings else 5,
    'high': max(filtered_readings) * adjustment_factor if filtered_readings else 15,
    'critical': 120
}

# Another irrelevant computation
simulated_load = sum((k + v) * 2 for k, v in threshold_map.items()) % 50

# Core signature generation (relevant)
health_signature = [
    eval_score,
    len(filtered_readings) * 3,
    sum(offset_table.values()) % 17
]

# Conditional expression using logical operations and comparisons
dynamic_weight = 2 if simulated_load < 30 and not risk_flag else 1

# Main processing function with closure-like behavior
def process_metrics(metrics, config):
    base = metrics[0] + metrics[1]
    tweak = config['low'] + config['high']
    # Logical short-circuit evaluation
    penalty = 10 if config['critical'] > 100 and (base > 20 or len(metrics) == 3) else 0
    # Final computation
    result = (base * tweak - penalty) // dynamic_weight
    return result + (1 if status_tag == "ALERT" else 0)

# Critical execution point
final_diagnostic = process_metrics(health_signature, threshold_map)

print(f"Result: {final_diagnostic}")