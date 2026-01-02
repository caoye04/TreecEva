import math

# Simulated sensor data processing pipeline with diagnostic analysis
def collect_readings():
    raw_signals = [127, 255, 193, 64, 222, 89, 154, 201]
    calibration_offset = 17
    adjusted = [max(0, x - calibration_offset) for x in raw_signals]
    return adjusted

# Irrelevant helper - dead code path (red herring)
def legacy_compatibility_mode(data):
    if sum(data) % 2 == 0:
        return [x ^ 255 for x in data]
    else:
        return [x >> 1 for x in data]

# Signal smoothing using moving average (relevant)
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window_avg = sum(signal[start:end]) / (end - start)
        smoothed.append(round(window_avg, 2))
    return smoothed

# Frequency domain approximation (distractor - not used in final path)
def estimate_dominant_frequency(signal):
    total_variation = 0
    for i in range(1, len(signal)):
        total_variation += abs(signal[i] - signal[i-1])
    return round(total_variation / len(signal), 3)

# Core data transformation (relevant)
def transform_magnitude(data):
    transformed = []
    for x in data:
        if x < 100:
            transformed.append(int(math.sqrt(x) * 10))
        elif x < 200:
            transformed.append(x // 2)
        else:
            transformed.append(int(math.log(x, 2) * 15))
    return transformed

# Threshold categorization map (relevant)
def generate_threshold_map():
    categories = {'low': 40, 'moderate': 75, 'high': 120, 'critical': 200}
    scaling_factor = 1.3
    # Misleading modification that doesn't affect final result
    temp_adjusted = {k: v * scaling_factor for k, v in categories.items()}
    # Actual return uses original thresholds
    return categories  # Red herring: temp_adjusted looks important but unused

# Data integrity check (irrelevant - never called)
def validate_checksum(data):
    checksum = 0
    for item in data:
        checksum = (checksum + item * 3) % 256
    return checksum == 42

# Main analysis engine (relevant)
def analyze_metrics(data, thresholds):
    counts = {'low': 0, 'moderate': 0, 'high': 0, 'critical': 0}
    
    # Nested logic with distractors
    temp_result = []
    for val in data:
        # Complex conditional chain
        if val < thresholds['low']:
            counts['low'] += 1
            temp_result.append(val * 1.1)
        elif val < thresholds['moderate']:
            counts['moderate'] += 1
            temp_result.append(val * 1.05)
        elif val < thresholds['high']:
            counts['high'] += 1
            temp_result.append(val * 0.95)
        else:
            counts['critical'] += 1
            temp_result.append(val * 0.85)
    
    # Distracting intermediate calculation
    avg_temp = sum(temp_result) / len(temp_result) if temp_result else 0
    deviation_score = sum([abs(x - avg_temp) for x in temp_result])
    
    # Final computation path (key)
    severity_index = 0
    severity_index += counts['low'] * 1
    severity_index += counts['moderate'] * 3
    severity_index += counts['high'] * 7
    severity_index += counts['critical'] * 15
    
    # Secondary adjustment based on pattern
    pattern_streak = 0
    max_streak = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            pattern_streak += 1
            max_streak = max(max_streak, pattern_streak)
        else:
            pattern_streak = 0
    
    if max_streak >= 3:
        severity_index = int(severity_index * 1.2)
    
    # Dead assignment - looks important but not used
    final_normalization = severity_index / (len(data) or 1)
    
    return severity_index  # Actual return value

# Unused utility function (red herring)
def format_diagnostics_report(diag_value):
    header = "=== SYSTEM DIAGNOSTIC REPORT ==="
    status_line = f"Status: {'CRITICAL' if diag_value > 100 else 'STABLE'}"
    footer = "--- END OF TRANSMISSION ---"
    return '\n'.join([header, status_line, footer])

# Orchestration function
if __name__ == "__main__":
    # Step 1: Collect and preprocess data
    raw_data = collect_readings()
    
    # Step 2: Smooth the signal (relevant)
    filtered_data = smooth_signal(raw_data)
    processed_data = transform_magnitude([int(x) for x in filtered_data])
    
    # Irrelevant string manipulation (distractor)
    log_id = "SENS-LOG-2023"
    log_parts = log_id.split('-')
    session_tag = ''.join([part[0] for part in log_parts]).lower()
    metadata_key = session_tag.upper() + "_" + str(len(processed_data))
    
    # Generate threshold configuration
    threshold_map = generate_threshold_map()
    
    # Perform final analysis
    final_diagnostic = analyze_metrics(processed_data, threshold_map)
    
    # Print result (required format)
    print(f"Result: {final_diagnostic}")