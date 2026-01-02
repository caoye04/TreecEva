import math

# Simulated sensor fusion system for environmental monitoring
# Complex logic with distractors and multiple abstraction layers
def collect_telemetry():
    raw_data = [144, 25, 73, 18, 91, 64, 37, 52]
    offset = 3
    calibrated = [math.sqrt(x + offset) for x in raw_data]
    return [round(v, 2) for v in calibrated]

# Irrelevant preprocessing function (dead path)
def normalize_samples(samples):
    mean_val = sum(samples) / len(samples)
    return [(x - mean_val) / mean_val for x in samples]

# Unused transformation chain
def transform_signal(data):
    shifted = [x * 1.5 for x in data]
    modded = [x % 13 for x in shifted]
    return sorted(modded, reverse=True)

# Core processing with meaningful logic buried inside distractions
def filter_anomalies(logs):
    threshold = 8.5
    anomalies = []
    valid_entries = []
    
    # Distractor: unused statistical calculations
    total = sum(logs)
    count = len(logs)
    average = total / count
    variance_proxy = sum((x - average) ** 2 for x in logs) / count
    entropy_estimate = -sum((x / total) * math.log(x / total) for x in logs if x > 0)
    
    # Real filtering logic
    for val in logs:
        if val > threshold:
            anomalies.append(val)
        else:
            valid_entries.append(val)
    
    # Red herring: unused anomaly summary
    anomaly_count = len(anomalies)
    anomaly_ratio = anomaly_count / len(logs)
    
    return valid_entries

# Data enrichment with set operations (required feature)
def augment_with_references(base_set):
    ref_a = {2.0, 3.5, 4.8, 6.1, 7.3, 8.0, 9.2}
    ref_b = {1.8, 3.5, 5.2, 6.1, 7.9, 8.7}
    ref_c = {4.8, 6.1, 7.3, 9.2, 10.1}
    
    common_refs = ref_a & ref_b & ref_c  # intersection
    extended_refs = ref_a | ref_b | ref_c  # union
    
    # Only this line matters: enriching with union
    enriched = list(extended_refs) + base_set
    
    # Decoy computation
    exclusive_refs = (ref_a ^ ref_b) ^ ref_c
    
    return sorted(enriched)

# Secondary processing with conditional expressions and integer division
def process_critical_path(values):
    result = 0
    temp_accum = 0
    
    for i, v in enumerate(values):
        # Complex conditional expression
        contribution = (v * 2 if v < 5 else v * 1.5) if i % 2 == 0 else (v // 2 if v > 7 else v)
        
        # Integer division and rounding side calculation (mostly irrelevant)
        coarse_val = int(contribution)
        rounded_val = round(contribution)
        
        temp_accum += contribution
        
        # Accumulation with selective addition
        if i % 3 != 0:
            result += rounded_val
    
    # This derived value is actually used later
    derived_magnitude = int(temp_accum // 1.8)
    
    return result, derived_magnitude

# Final analysis combining multiple concepts
def analyze_readings(entries):
    # Initialize several misleading variables
    baseline_score = 0
    risk_factor = 1.0
    stability_index = 0.0
    diagnostic_weight = 0
    
    # Real logic begins: summation and accumulation
    cumulative = 0
    for x in entries:
        if x > 6:
            cumulative += x * 0.7
        elif x > 4:
            cumulative += x * 0.9
        else:
            cumulative += x * 1.1
    
    # Conditional expression influencing final result
    adjustment = 1.25 if len(entries) > 10 else 0.88
    
    # Key calculation
    preliminary_diagnostic = cumulative * adjustment
    
    # Several decoy transformations
    normalized_diagnostic = preliminary_diagnostic / (max(entries) or 1)
    log_transformed = math.log(preliminary_diagnostic) if preliminary_diagnostic > 0 else 0
    inverted_scale = 100 / (1 + preliminary_diagnostic)
    
    # Final computation - only this matters
    final_diagnostic = int(preliminary_diagnostic // 0.97) + 5
    
    # Dead code paths with misleading names
    if final_diagnostic > 100:
        baseline_score += 20
        risk_factor *= 1.1
    else:
        stability_index = 95.0
        diagnostic_weight = 3
    
    return final_diagnostic

# Orchestration with hidden execution flow
if __name__ == "__main__":
    # Step 1: Collect raw telemetry
    sensor_readings = collect_telemetry()  # [12.04, 5.29, 8.72, 4.58, 9.75, 8.12, 6.32, 7.35]
    
    # Step 2: Filter out high readings (anomalies)
    processed_logs = filter_anomalies(sensor_readings)
    
    # Step 3: Augment with reference data using set operations
    enhanced_logs = augment_with_references(processed_logs)
    
    # Step 4: Process through critical path (returns tuple)
    _, magnitude = process_critical_path(enhanced_logs)
    
    # Step 5: Final diagnostic analysis
    final_diagnostic = analyze_readings(processed_logs)  # Note: using original filtered, not enhanced
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")