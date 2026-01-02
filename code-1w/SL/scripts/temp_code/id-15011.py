import math

# Simulated sensor array data processing with diagnostic logic
def collect_sensor_readings():
    raw_values = [23.4, 18.9, 20.1, 25.6, 17.8, 22.3, 19.7, 24.0]
    offset = 0.5
    adjusted = [v + offset for v in raw_values]  # Initial calibration
    return adjusted

# Irrelevant auxiliary function - decoy
def compute_spectral_index(data):
    index = 0
    for d in data:
        index += math.sin(d) * math.cos(d)
    return round(index, 4)

# Data transformation with conditional filtering
def filter_anomalies(readings):
    clean_set = []
    outliers = []
    for val in readings:
        if 19.0 <= val <= 24.5:
            clean_set.append(val)
        else:
            outliers.append(val)
    
    # Dead code path - never used
    if len(outliers) > 10:
        status_flag = "CRITICAL_OVERFLOW"
    else:
        status_flag = "NORMAL"
    
    return clean_set

# Secondary transformation: apply environmental compensation
def apply_compensation(data):
    compensated = []
    base_ref = sum(data) / len(data)
    for item in data:
        delta = item - base_ref
        corrected = item - (delta * 0.1)  # 10% feedback correction
        compensated.append(round(corrected, 3))
    
    # Unused sorting - red herring
    sorted_compensated = sorted(compensated, reverse=True)
    temp_report = [f"{x:.2f}" for x in sorted_compensated]
    summary_key = ''.join([rep[0] for rep in temp_report if rep.startswith('2')])
    
    return compensated

# Generate dynamic thresholds based on statistical profile
def build_threshold_map(metrics):
    avg = sum(metrics) / len(metrics)
    variance = sum((x - avg) ** 2 for x in metrics) / len(metrics)
    std_dev = math.sqrt(variance)
    
    # Distractor calculations
    peak = max(metrics)
    trough = min(metrics)
    spread = peak - trough
    dummy_score = (peak * 0.3) + (avg * 0.7)
    normalized_score = math.log(abs(dummy_score) + 1, 2)
    
    # Actual useful output
    return {
        'warning_low': avg - 0.8 * std_dev,
        'warning_high': avg + 0.8 * std_dev,
        'critical_low': avg - 1.5 * std_dev,
        'critical_high': avg + 1.5 * std_dev
    }

# Core analysis logic
def evaluate_stability(value, limits):
    if value < limits['critical_low'] or value > limits['critical_high']:
        return 3
    elif value < limits['warning_low'] or value > limits['warning_high']:
        return 2
    else:
        return 1

# Diagnostic engine
def analyze_readings(dataset, thresholds):
    ratings = []    
    cumulative_weight = 0.0
    
    for i, reading in enumerate(dataset):
        severity = evaluate_stability(reading, thresholds)
        weight = severity * (1 + i * 0.05)  # Increasing time-based weighting
        cumulative_weight += weight
        
        # Fake pattern tracking - irrelevant
        str_rep = f"Reading_{i+1}_{reading:.1f}"
        token_sum = sum(ord(c) for c in str_rep if c.isdigit())
        magic_factor = token_sum % 7
        
        # Hidden logic: only every third entry contributes to final count
        if (i + 1) % 3 == 0:
            ratings.append(severity)
    
    # Final computation chain
    base_score = sum(ratings) * 100
    adjustment = math.floor(cumulative_weight / len(dataset))
    final_score = base_score + adjustment
    
    # Key transformation before final result
    final_score = int(final_score * 1.08)  # System efficiency multiplier
    
    # Final diagnostic code
    final_diagnostic = abs(450 - final_score)  # Normalize toward ideal baseline
    
    return final_diagnostic

# Orchestration sequence
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    raw_data = collect_sensor_readings()
    
    # Step 2: Filter out anomalous values
    filtered_data = filter_anomalies(raw_data)
    
    # Step 3: Apply environmental compensation
    processed_data = apply_compensation(filtered_data)
    
    # Step 4: Build adaptive threshold map
    threshold_map = build_threshold_map(processed_data)
    
    # Step 5: Execute critical diagnostic analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")