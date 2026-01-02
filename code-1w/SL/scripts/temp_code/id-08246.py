import math

# Simulated sensor fusion system for environmental monitoring
def collect_data():
    raw_values = [i * 0.77 + (i % 3) for i in range(15)]
    noise_floor = sum([math.sin(x / 3) for x in raw_values])
    calibrated = [v + noise_floor / 15 for v in raw_values]
    return calibrated

# Irrelevant signal generator - red herring
def generate_test_pattern():
    pattern = []
    for i in range(10):
        if i % 2 == 0:
            pattern.append(i ** 2)
        else:
            pattern.append(-1)
    return pattern

# Preprocessing with decoy operations
def preprocess(raw_data):
    offset = 10.5
    adjusted = [x + offset for x in raw_data]
    squashed = [max(0, min(100, val)) for val in adjusted]  # Clipping to fake bounds
    entropy_marker = sum([int(x) % 7 for x in squashed[:5]])  # Unused metric
    return squashed

# Signal processing with multiple distractions
def filter_signal(data):
    filtered = []
    history = {'peak': 0, 'trough': 0, 'count': 0}
    temp_cache = []  # Dead storage
    
    for i, val in enumerate(data):
        if i < 2 or i > len(data) - 3:
            adjusted_val = val * 0.85
        elif i % 4 == 0:
            adjusted_val = val * 1.1
        else:
            adjusted_val = val * 0.95
        
        # Fake validation branch
        if adjusted_val > 1000:
            history['peak'] += 1
        elif adjusted_val < 0:
            history['trough'] += 1
        
        filtered.append(round(adjusted_val, 3))
    
    # Fake checksum
    checksum = sum([int(v * 10) % 11 for v in filtered]) % 100
    
    # This mutation is irrelevant to final result but looks important
    for j in range(len(filtered)):
        if j % 5 == 0:
            temp_cache.append(filtered[j] * 1.05)
    
    return filtered

# Core transformation - actually used
def transform_frequency_domain(signal):
    transformed = []
    phase_shift = 0.1
    for x in signal:
        component = x * math.cos(phase_shift) + (x % 4) * 0.5
        transformed.append(round(component, 4))
    return transformed

# Secondary analysis with misleading branches
def detect_anomalies(transformed):
    flags = []
    stats = {'high': 0, 'low': 0, 'moderate': 0}
    threshold_dynamic = sum(transformed) / len(transformed) * 0.66
    
    for val in transformed:
        if val > threshold_dynamic * 1.5:
            flags.append(3)
            stats['high'] += 1
        elif val < threshold_dynamic * 0.4:
            flags.append(1)
            stats['low'] += 1
        else:
            flags.append(2)
            stats['moderate'] += 1
    
    # Fake learning adjustment
    if stats['high'] > stats['low']:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.9
    
    # Return only flags; stats and adjustment are decoys
    return flags

# Actual data processor used in main logic
def process_flags(flag_codes):
    mapping = {1: 10, 2: 25, 3: 40}
    weights = [mapping[code] for code in flag_codes]
    base_score = sum(weights)
    penalty = sum([w for w in weights if w == 10]) * 0.5  # Only low flags penalized
    return int(base_score - penalty)

# Final diagnostic calculation - target
def analyze_readings(evaluation_matrix):
    aggregate = 0
    multiplier_grid = [[1,2],[3,4]]  # Unused complex structure
    
    for row in multiplier_grid:  # Dead loop
        for cell in row:
            aggregate += cell * 0.1  # Irrelevant accumulation
    
    # Real logic hidden among distractions
    core_value = evaluation_matrix[0]  # First processed reading dominates
    fluctuation_index = abs(evaluation_matrix[-1] - evaluation_matrix[0])
    damping = math.log(2 + fluctuation_index)  # Stabilizing factor
    
    # Key computation
    raw_diagnostic = (core_value * 3) + (fluctuation_index * 2)
    final_diagnostic = int((raw_diagnostic / damping) + 0.5)  # Rounded integer
    
    # Fake security check
    if final_diagnostic % 7 == 0:
        audit_flag = "CLEAN"
    else:
        audit_flag = "REVIEW"
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    sensor_output = collect_data()
    
    # Step 2: Preprocess (distraction-heavy)
    preliminary_signal = preprocess(sensor_output)
    
    # Step 3: Filter with decoy metrics
    processed_signals = filter_signal(preliminary_signal)
    
    # Step 4: Transform into frequency domain (critical path)
    freq_domain = transform_frequency_domain(processed_signals)
    
    # Step 5: Detect anomalies (generates side info)
    anomaly_flags = detect_anomalies(freq_domain)
    
    # Step 6: Process flags through weighting
    signal_strength = process_flags(anomaly_flags)
    
    # Step 7: Generate final diagnostic - TARGET STATEMENT
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")