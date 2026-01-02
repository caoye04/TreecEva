def analyze_readings(readings):
    cumulative_score = 0
    for i, val in enumerate(readings):
        if i % 2 == 0:
            cumulative_score += val ** 0.5
        else:
            cumulative_score -= val // 4
    return int(cumulative_score)

# Irrelevant helper (decoy function)
def validate_input(data):
    return isinstance(data, list) and all(isinstance(x, int) for x in data)

# Unused transformation path
def transform_sequence(seq):
    return [x * 1.5 for x in seq if x > 10]

# Real processing chain
def filter_critical(values, limit):
    return [v for v in values if v > limit]

def compute_entropy(vals):
    total = sum(vals)
    probs = [v / total for v in vals]
    from math import log2
    return round(-sum(p * log2(p) for p in probs if p > 0), 6)

def aggregate_diagnostics(data):
    base = sum(data) // len(data)
    deviation = sum(abs(x - base) for x in data)
    return base + (deviation % 7)

# Distractor variables
temp_cache = [0] * 15
backup_registry = set()
legacy_mode = True

# Main health monitoring simulation
health_data = [88, 52, 91, 44, 73, 60, 29, 82, 37, 58]
thresholds = {"low": 30, "high": 75}

# Dead code branch (never executed)
if False:
    health_data = [x + 10 for x in health_data]
    thresholds["high"] += 5

# Real signal extraction
strong_signals = filter_critical(health_data, thresholds["high"])
diagnostic_entropy = compute_entropy(strong_signals)

# Dummy computation with misleading intermediate
normal_readings = [x for x in health_data if thresholds["low"] <= x <= thresholds["high"]]
shadow_index = sum(x & 7 for x in normal_readings)

# Core logic masked by noise
baseline_metric = analyze_readings(health_data)
diagnostic_code = aggregate_diagnostics(strong_signals)

# Set operation distraction
unique_flags = set(range(5, 20)) | {len(normal_readings), shadow_index, baseline_metric}
flag_intersection = unique_flags & {7, 12, 29, baseline_metric}

# Conditional expression mix
status_weight = 1.5 if len(flag_intersection) > 2 else 0.8
adjustment_factor = diagnostic_entropy if status_weight > 1 else 3.0

# Critical execution point
final_diagnostic = process_metrics(health_data, thresholds)

# Actual implementation buried below
def process_metrics(data, limits):
    above_high = [x for x in data if x > limits["high"]]
    below_low = [x for x in data if x < limits["low"]]
    mid_range = [x for x in data if limits["low"] <= x <= limits["high"]]
    
    # Composite metric
    score_a = sum(above_high) // (len(above_high) or 1)
    score_b = min(mid_range) if mid_range else 0
    score_c = len(below_low) * 12
    
    # Red herring: unused bitwise combination
    decoy_mask = score_a ^ score_b & 0xFF
    
    # Real result construction
    primary = score_a - score_b
    secondary = len(above_high) + (sum(mid_range) // 10)
    
    # Final deterministic computation
    result = primary * 2 + secondary - score_c
    
    # Additional distraction
    metadata_log = {
        'entries': len(data),
        'decoy': decoy_mask,
        'timestamp': 1699999999
    }
    
    return result

# Print required output
Result: {final_diagnostic}