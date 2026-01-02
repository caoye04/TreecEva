from collections import defaultdict, Counter
import math

# Simulated system telemetry data with mixed signal types
technical_metrics = [127, 255, 192, 168, 100, 200, 250, 144]
error_codes = [404, 503, 404, 403, 500, 503, 404, 404]
signal_strengths = [-72.3, -80.1, -65.7, -90.5, -73.2, -68.9, -85.4, -77.6]

# Irrelevant auxiliary data (distractor)
user_preferences = {'theme': 'dark', 'auto_save': True, 'refresh_rate': 60}
recent_queries = [("status", 1), ("debug", 0), ("trace", 1)]
baseline_threshold = sum(technical_metrics) / len(technical_metrics)

# Data preprocessing with red herring transformations
shifted_signals = [round(s + 5.0) for s in signal_strengths]  # Distractor: rounded but unused later
discrete_levels = [int(abs(s) // 10) for s in signal_strengths]

# Misleading diagnostic path (dead code path)
def legacy_diagnostic(metrics):
    if not metrics:
        return 0
    avg = sum(metrics) >> 3
    return avg & 0xFF

# Another decoy function with plausible name
def estimate_bandwidth(metric_list):
    total = 0
    for m in metric_list:
        if m > 200:
            total += m << 2
        else:
            total += m >> 1
    return total % 1000  # Unused result

# Real processing begins here
log_entries = defaultdict(int)
for code in error_codes:
    log_entries[code] += 1

system_flags = []
for i, metric in enumerate(technical_metrics):
    if i % 2 == 0 and metric >= 192:
        system_flags.append((i, metric))

# Complex conditional bit manipulation (relevant)
flag_sum = 0
for idx, val in system_flags:
    flag_sum ^= (val << 1) | (idx & 3)

# Secondary analysis using Counter (relevant)
frequent_errors = Counter(error_codes)
top_error_count = frequent_errors.most_common(1)[0][1]

# Mixed arithmetic with distractor variables
scaling_factor = math.log(baseline_threshold, 2)
dummy_calc = estimate_bandwidth(technical_metrics)  # Called but not used

# Key intermediate with misleading comment
# Note: This 'adjusted' value is actually irrelevant to final result
adjusted = int(scaling_factor * top_error_count * 1.5) if top_error_count > 3 else 0

# Actual core logic: pattern analysis based on frequency and bit state
pattern_score = 0
for code, count in log_entries.items():
    if count >= 2:
        # Weight by inverse of error magnitude (lower codes weighted more)
        weight = 1000 // (code + 1)
        pattern_score += weight * count

# Final transformation involving multiple concepts
def analyze_pattern(entries, flags):
    base = pattern_score
    modifier = len(flags) * 100
    
    # Additional adjustment based on discrete signal distribution
    level_counter = Counter(discrete_levels)  # Reuse from earlier
    dominant_level = level_counter.most_common(1)[0][1]
    
    # Red herring inside function
    temp_debug = {k: v for k, v in entries.items() if v > 1}
    debug_sum = sum(temp_debug.keys())  # Computed but unused
    
    # Real formula
    result = base + modifier
    if dominant_level >= 3:
        result += 50
    
    # Final bitwise twist
    result = (result ^ flag_sum) & 0xFFFF  # Bound to 16 bits
    
    return result

# Execution point of interest
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")