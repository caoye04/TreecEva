import math

# Simulated sensor array data processing with diagnostic logic
def collect_sensor_readings():
    raw_readings = [14.2, 18.7, 22.1, 19.5, 25.3, 20.4, 17.8, 23.6]
    calibration_offset = 1.8
    adjusted = [r + calibration_offset for r in raw_readings]
    return adjusted

# Irrelevant helper - distractor function (dead path)
def legacy_compatibility_mode(data):
    if sum(data) > 100:
        return [x * 0.95 for x in data if x > 20]
    else:
        return [x + 1 for x in data]

# Signal filtering with moving average
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        segment = data[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

# Outlier detection - used but partially misleading intermediate result
def detect_outliers(values, sensitivity=2.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    threshold = sensitivity * std_dev
    outliers = [v for v in values if abs(v - mean_val) > threshold]
    # Misleading count - looks important but not used in final result
    outlier_count_hint = len(outliers) * 2 + 5  
    return [v for v in values if abs(v - mean_val) <= threshold]  # filtered inliers

# Data normalization - actually contributes to final result
def normalize_range(data, target_min=-1.0, target_max=1.0):
    if not data:
        return []
    old_min, old_max = min(data), max(data)
    if old_min == old_max:
        return [0.0] * len(data)
    return [
        target_min + (x - old_min) * (target_max - target_min) / (old_max - old_min)
        for x in data
    ]

# Conditional expression based transformation - required Python feature
def apply_filter_mode(signal, mode_flag):
    return [
        x * 1.25 if mode_flag else x * 0.75
        for x in signal
    ]

# Core analysis function with nested logic and early termination
def analyze_signal(clean_data, critical_threshold):
    if not clean_data:
        return -999

    magnitude = sum(abs(x) for x in clean_data)
    
    # Early return red herring - condition looks plausible but rarely triggers
    if magnitude < 0.5:
        return -1  # dead code in practice due to data scale

    peak = max(clean_data, key=abs)
    avg = sum(clean_data) / len(clean_data)
    
    # Complex conditional expression combining multiple factors
    base_score = (magnitude * 0.3) + (abs(peak) * 0.4) + (abs(avg) * 0.3)
    
    # Key branching logic with subtle dependency
    adjustment_factor = 0.85 if abs(peak) > critical_threshold else 1.15
    
    # Final computation chain
    temp_result = base_score * adjustment_factor
    
    # Apply non-linear correction only if conditions met
    temp_result = (
        temp_result ** 1.1
        if peak < 0 and temp_result > 5
        else temp_result ** 0.9
    )
    
    # Final rounding to simulate diagnostic precision
    return round(temp_result, 4)

# --- Main execution with distractions ---
if __name__ == "__main__":
    # Step 1: Collect and adjust raw data
    sensor_data = collect_sensor_readings()
    
    # Distractor: unused legacy transformation
    compat_data = legacy_compatibility_mode(sensor_data)  
    
    # Step 2: Smooth the signal
    refined_signal = smooth_signal(sensor_data)
    
    # Step 3: Remove statistical outliers (modifies data meaningfully)
    filtered_signal = detect_outliers(refined_signal, sensitivity=1.5)
    
    # Step 4: Normalize to standard range
    calibrated_signal = normalize_range(filtered_signal)
    
    # Distractor: secondary processed version not used
    alt_normalization = normalize_range(calibrated_signal, 0, 100)  
    
    # Step 5: Apply dynamic filter based on conditional logic
    activation_mode = len(calibrated_signal) % 2 == 0  # depends on post-filter length
    conditioned_signal = apply_filter_mode(calibrated_signal, activation_mode)
    
    # Distractor: auxiliary metric that seems important
    entropy_approx = sum(math.log(abs(x) + 1e-8) for x in conditioned_signal)
    entropy_floor = math.floor(abs(entropy_approx))
    
    # Final analysis parameters
    threshold = 0.4
    final_diagnostic = analyze_signal(conditioned_signal, threshold)
    
    # Critical output - must print this exact format
    print(f"Target result: {final_diagnostic}")