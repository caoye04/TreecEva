def analyze_sequence(data):
    # Irrelevant transformation (distractor)
    temp_result = [x ** 2 for x in data if x % 2 == 0]
    processed = [x for x in data if x > 0]
    shifted = [(x >> 1) for x in processed]  # Bit manipulation red herring
    return shifted

# Unused helper function (dead code path)
def validate_input(arr):
    return all(isinstance(x, int) for x in arr) and len(arr) > 0

# Decoy data structure
decoy_metrics = {
    'peak': 999,
    'baseline': 400,
    'noise_floor': 50
}

# Real data source
event_stream = [15, -3, 7, 22, 4, -8, 19, 11]

# Distractor: complex string processing with slicing
log_trace = "error@warning@info@debug"
trace_parts = log_trace.split('@')
critical_level = trace_parts[1][:3].upper()  # Result: WAR - irrelevant

# Extract meaningful signals
signal_peaks = [x for x in event_stream if x > 10]

# Hash map for weighting factors
weight_map = {
    15: 1.1,
    22: 0.9,
    19: 1.2,
    11: 0.8
}

# Set operation to filter valid keys (distractor usage)
available_keys = set(weight_map.keys())
valid_peaks = [p for p in signal_peaks if p in available_keys]

# Apply weights using dictionary lookup
weighted_values = [p * weight_map[p] for p in valid_peaks]

# Secondary transformation with integer division and rounding
normalized = [int(round(w / 10)) for w in weighted_values]  # Scale down

# Another layer of distraction: unused slicing on normalized
tail_segment = normalized[1:3]  # [1, 2] - not used later

# Adjustment factor derived from bitwise XOR of constants (misleading)
adjustment_factor = (17 ^ 29) & 15  # Evaluates to 13, but only partially relevant

# Core logic disguised among noise
base_metric = sum(normalized)  # 1 + 2 + 2 + 1 = 6

# Conditional adjustment with short-circuit logic (looks complex but simple)
sensitivity_mode = True
offset_correction = sensitivity_mode and (len(valid_peaks) > 3) or False
offset_value = 4 if offset_correction else 2  # True → 4

# Main evaluation function
def evaluate_performance(metrics, adj):
    # Redundant validation
    if not metrics:
        return 0
    
    # Real computation buried in abstraction
    raw_total = sum(metrics)
    adjusted_total = raw_total * adj
    
    # Additional decoy logic
    if adj > 10:
        adjusted_total -= 5  # This executes, subtracts 5
    
    # Final nonlinear correction (key step)
    final = adjusted_total + offset_value  # (6*13 - 5) + 4 = 78 - 5 + 4 = 77
    return final

# Log used in the key statement
metrics_log = normalized

# Critical execution point
final_score = evaluate_performance(metrics_log, adjustment_factor)

# Output result
print(f"Result: {final_score}")