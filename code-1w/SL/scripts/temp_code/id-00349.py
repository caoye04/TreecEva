from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [104, 95, 110, 90, 120, 85, 115, 100]
threshold = 100
calibration_factor = 0.95

# Irrelevant preprocessing: normalize readings (not used in final logic)
normalized = [calibration_factor * (x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) for x in raw_readings]

# Extract features
above_threshold = [x for x in raw_readings if x > threshold]
below_or_equal = [x for x in raw_readings if x <= threshold]

# Misleading statistical summary
distribution_stats = {
    'mean': sum(raw_readings) / len(raw_readings),
    'median': sorted(raw_readings)[len(raw_readings)//2],
    'std_dev': math.sqrt(sum((x - sum(raw_readings)/len(raw_readings))**2 for x in raw_readings) / len(raw_readings))
}

# Initialize performance tracking
performance_log = defaultdict(int)
for reading in raw_readings:
    if reading > threshold:
        performance_log['high'] += 1
    else:
        performance_log['low'] += 1

# Dead code path - never executed due to fixed condition
DEBUG_MODE = False
if DEBUG_MODE:
    debug_info = Counter(normalized)
    print(f'Debug: {debug_info}')

# Weighted metric computation (core logic)
def compute_stability_index(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return sum(diffs) / len(diffs) if diffs else 0

stability = compute_stability_index(sorted(raw_readings))

# Auxiliary function with red herring output
def analyze_trend(sequence):
    trend_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_score += 1
        elif sequence[i] < sequence[i-1]:
            trend_score -= 1
    # This function is called but its result is not used
    return abs(trend_score)
trend_analysis = analyze_trend(raw_readings)

# Core evaluation parameters
metrics = {
    'peak_count': len(above_threshold),
    'baseline_adherence': len(below_or_equal),
    'stability': stability,
    'consistency': len(raw_readings) - int(stability)
}

weights = {
    'peak_count': 0.3,
    'baseline_adherence': 0.2,
    'stability': -0.4,  # Inverse impact
    'consistency': 0.5
}

# Slice analysis - irrelevant subset
recent_slice = raw_readings[2:6]
slice_variance = sum((x - sum(recent_slice)/len(recent_slice))**2 for x in recent_slice)

# Lambda-based transformation (not ultimately used)
transform = lambda x, w: x * w if x > 0 else 0

# Actual evaluation logic
def evaluate_performance(met, wgt):
    total = 0.0
    for key in met:
        if key in wgt:
            # Apply weighted scoring
            total += met[key] * wgt[key]
    # Final adjustment based on system health (simulated)
    system_health = 1.1  # Assumed stable
    return int(total * system_health)

# Key statement
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")