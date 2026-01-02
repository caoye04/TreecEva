def analyze_readings(data, threshold=50):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    
    # Distractor: irrelevant statistical computation
    mean_value = sum(data) / len(data) if data else 0
    variance_proxy = sum((x - mean_value) ** 2 for x in data) / len(data) if data else 0

    # Semi-relevant transformation (only max matters later)
    adjusted_values = [x * 0.9 + 5 for x in above_threshold]
    peak_adjusted = max(adjusted_values) if adjusted_values else 0

    return len(above_threshold), peak_adjusted, mean_value


def validate_stability(metric, history):
    # Irrelevant complexity: tracks stability but not used in final score
    if not history:
        return True
    recent_trend = [history[i] < history[i+1] for i in range(len(history)-1)]
    improvements = sum(recent_trend)
    return improvements > len(history) // 2

# Simulated sensor readings over time
current_readings = [45, 67, 89, 52, 43, 78, 91, 50, 66]
baseline = [55, 60, 58, 62, 59]

# Auxiliary variables - mostly distractions
system_status = "nominal"
last_calibration = "2023-11-05"
stability_log = [True, False, True, True]

# Intermediate processing with red herring calculations
size_factor = len(current_readings) * 0.1
offset_correction = sum(baseline) % 7

# Key data extraction (used later)
valid_count, max_enhanced, avg = analyze_readings(current_readings)

# Distractor block: unused conditional branch
if avg > 60:
    system_status = "elevated"
    temp_adj = offset_correction * 2.5
else:
    system_status = "stable"
    temp_adj = 0

# Another distraction: string manipulation unrelated to logic
diagnostic_flag = "SYS_OK" if system_status == "stable" else "WARN"
diagnostic_code = diagnostic_flag.lower().replace("_", "-")

# Core logic begins here — only from this point some values matter
def calculate_performance(base, readings):
    base_median = sorted(base)[len(base)//2]
    reading_max = max(readings)
    
    # Conditional expression determining scaling
    scale = 1.5 if reading_max > 80 else 1.1
    
    # Multiple assignment distractor
    (temp, _) = (scale * base_median, 0)
    
    # Actual performance formula
    raw_score = reading_max * scale - base_median
    
    # Additional noise: dead code path
    if False:
        raw_score += temp_adj  # Never executed
    
    # Final adjustment using list comprehension (filtering relevant readings)
    significant_boost = sum([r//10 for r in readings if r > 75])
    final_raw = raw_score + significant_boost
    
    # Normalize with size factor (which depends on input length)
    normalized = final_raw / (1 + size_factor)
    
    return int(normalized)

# Critical execution point
final_score = calculate_performance(baseline, current_readings)

print(f"Result: {final_score}")