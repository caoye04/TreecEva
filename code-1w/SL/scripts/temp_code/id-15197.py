import itertools

# Simulated health monitoring system with diagnostic logic
def analyze_biomarkers(data_chunk):
    base_score = 0
    for val in data_chunk:
        if val > 70:
            base_score += val * 0.3
        elif val > 40:
            base_score += val * 0.1
    return int(base_score)

# Distractor function: unused in final computation
def legacy_calculate_risk(age, bmi):
    risk = (age * 0.2) + (bmi * 1.5)
    adjusted = risk * 0.8 if age < 50 else risk * 1.1
    return adjusted  # Dead end

# Data transformation pipeline
def normalize_readings(readings):
    normalized = [(x - min(readings)) / (max(readings) - min(readings)) * 100 for x in readings]
    offset_correction = sum([n * 0.05 for n in normalized[:5]])
    return [n + offset_correction for n in normalized]

# Main processing with red herrings and decoys
def evaluate_stress_markers(seq):
    stress_index = 0
    for i, s in enumerate(seq):
        if i % 3 == 0:
            stress_index += hash(s) % 10
        elif 'elevated' in s:
            stress_index += 7
    return stress_index * 2

# Real computational path buried under noise
def filter_anomalies(values, limit):
    filtered = []
    anomaly_count = 0
    for v in values:
        if abs(v - 50) > limit:
            anomaly_count += 1
        else:
            filtered.append(v)
    # Decoy statistic
    suppression_rate = anomaly_count / len(values) if values else 0
    return filtered

# Critical function: computes final diagnostic score
def process_metrics(metrics, config):
    stage_one = [x * config['factor_a'] for x in metrics]
    
    # Bit manipulation red herring
    bit_fiddle = 0
    for x in stage_one:
        bit_fiddle ^= int(x) & 0xFF
        bit_fiddle += (int(x) >> 4) & 0x0F
    
    # Real transformation
    stage_two = [y * config['factor_b'] for y in stage_one]
    
    # Irrelevant combinatorics
    pairs = list(itertools.combinations(stage_two[:6], 2))
    pair_sum = sum(a + b for a, b in pairs)  # Misleading aggregate
    
    # Core logic: conditional accumulation
    cumulative = 0
    for idx, val in enumerate(stage_two):
        if idx % 2 == 0 and val > 100:
            cumulative += val * 0.25
        elif idx % 4 == 3:
            cumulative -= val * 0.1
    
    # Final adjustment using logical conditions
    threshold_met = sum(1 for v in stage_two if v > 150)
    modifier = 1.15 if threshold_met >= 3 else 0.9

    intermediate_result = cumulative * modifier

    # Apply bitmask unrelated to result
    mask = 0xFFFF
    masked = int(intermediate_result) & mask

    # Actual answer derivation
    final_value = int(intermediate_result) + 13
    
    return final_value

# --- Execution Context ---
if __name__ == "__main__":
    # Input data
    raw_health_signals = [68, 72, 65, 88, 91, 77, 63, 85]
    
    # Irrelevant dataset
    motion_artifacts = [0.4, 0.7, 1.2, 0.3, 0.8]
    calibration_sequence = ['baseline', 'elevated', 'recovery', 'elevated']
    
    # Unused variables (distractors)
    patient_age = 47
    patient_bmi = 24.5
    session_id = 'DX-7890'
    protocol_version = 'v3.2-alpha'
    
    # Normalization with side effect (but not used later)
    corrected_signals = normalize_readings(raw_health_signals)
    
    # Biomarker analysis - looks important but irrelevant
    biomarker_score = analyze_biomarkers(raw_health_signals)
    
    # Stress evaluation on decoy data
    stress_diagnostic = evaluate_stress_markers(calibration_sequence)
    
    # Filtering anomalies (result partially ignored)
    cleaned_data = filter_anomalies(raw_health_signals, limit=20)
    
    # Configuration buried among noise
    config_settings = {
        'factor_a': 2.1,
        'factor_b': 1.8,
        'timeout': 3000,
        'debug_mode': False,
        'log_level': 'warning'
    }
    
    # Key execution point
    final_diagnostic = process_metrics(cleaned_data, config_settings)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")