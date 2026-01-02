import math

# Simulated sensor array diagnostics with data filtering and noise analysis
def collect_sensor_data():
    raw_readings = [127, 255, 0, 64, 192, 32, 96, 160]
    noise_floor = 30
    filtered = []
    for val in raw_readings:
        if val > noise_floor:
            normalized = (val / 255.0) * 100
            if normalized > 20.0:
                filtered.append(round(normalized, 2))
    return filtered

# Secondary diagnostic chain - irrelevant but plausible
def compute_signal_entropy(data):
    entropy = 0.0
    total = sum(data)
    for x in data:
        prob = x / total if total else 0
        if prob > 0:
            entropy -= prob * math.log(prob, 2)
    return round(entropy, 3)

# Data transformation pipeline with red herrings
def preprocess_readings(raw_vals):
    scaled = [x * 1.5 for x in raw_vals]
    offset_corrected = [x - 10 for x in scaled]
    clipped = [min(max(x, 0), 100) for x in offset_corrected]  # Clamp to 0-100
    inverted = [100 - x for x in clipped]  # Inversion - unused distraction
    sorted_vals = sorted(clipped, reverse=True)
    return sorted_vals

# Core analysis logic buried in distractions
def calculate_baseline(readings):
    if len(readings) < 4:
        return 0
    quartile_idx = len(readings) // 4
    relevant_portion = readings[quartile_idx:-quartile_idx] if quartile_idx else readings
    return sum(relevant_portion) / len(relevant_portion)

# Decoy function - looks important but unused in critical path
def assess_system_health(diag_code, threshold=75.0):
    warnings = 0
    if diag_code < 20:
        warnings += 1
    elif diag_code > 90:
        warnings += 2
    status = "CRITICAL" if warnings >= 2 else "STABLE"
    return status

# Conditional expression and masking logic
def mask_outliers(data, limit=85.0):
    return [x if x <= limit else limit for x in data]

# Aggregation with multiple control flows
def integrate_diagnostics(primary, secondary):
    result = 0
    if primary > secondary:
        result = primary * 1.1
    else:
        result = secondary * 0.9
    adjustment = 5 if result > 70 else -2
    return result + adjustment

# Final analysis incorporating key computation
def analyze_readings(data):
    base = calculate_baseline(data)
    masked = mask_outliers(data)
    masked_avg = sum(masked) / len(masked)
    integrated = integrate_diagnostics(base, masked_avg)
    # Key manipulation: bitwise mix of integral components
    int_base = int(integrated)
    int_masked = int(masked_avg)
    magic_shift = (int_base << 2) ^ (int_masked >> 1) & 0xFF
    final_score = int_base + (magic_shift % 19)
    return final_score

# Orchestration with decoy variables and dead paths
if __name__ == "__main__":
    # Step 1: Collect real data
    sensor_output = collect_sensor_data()
    
    # Step 2: Preprocess (relevant)
    processed_data = preprocess_readings(sensor_output)
    
    # Step 3: Compute irrelevant entropy (distraction)
    entropy_metric = compute_signal_entropy(sensor_output)
    health_status = assess_system_health(entropy_metric)  # Dead end
    
    # Step 4: Critical analysis chain
    baseline_measure = calculate_baseline(processed_data)
    
    # Misleading conditional branch with unused outcome
    if baseline_measure > 60:
        scaling_factor = 1.75
        amplified_readings = [x * scaling_factor for x in processed_data]
        peak_value = max(amplified_readings)  # Unused
    else:
        correction_vector = [-5, -3, 0]  # Dead code path
    
    # Final diagnostic calculation (key statement)
    final_diagnostic = analyze_readings(processed_data)
    
    # OUTPUT REQUIRED RESULT
    print(f"Result: {final_diagnostic}")