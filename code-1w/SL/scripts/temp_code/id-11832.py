from collections import defaultdict, Counter
import math

# Simulated quantum register diagnostics with noise filtering
def preprocess_register_data(raw_reads):
    filtered = []
    for val in raw_reads:
        if val < 0:
            continue
        if val % 7 == 0:
            # Noise signature: skip multiples of 7
            continue
        filtered.append(val)
    return filtered

# Legacy function – unused but looks relevant (red herring)
def deprecated_calibration(sequence):
    return sum(x ** 0.5 for x in sequence if x > 10)

# Core analysis engine
def compute_coherence_score(values):
    if not values:
        return 0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return round(math.sqrt(variance), 6) if variance > 1 else 0.5

# Frequency-based anomaly detection
def detect_anomalies(counts):
    total = sum(counts.values())
    anomalies = 0
    for freq in counts.values():
        if freq / total < 0.05:
            anomalies += 1
    return anomalies

# Main diagnostic pipeline
def analyze_system_state(registers, log_entries):
    # Step 1: Extract active qubit readings
    quantum_data = []
    for reg in registers:
        for bit_pos, val in enumerate(reg):
            if val > 0 and bit_pos % 3 != 2:  # Filter by position
                quantum_data.append(val * 2)

    # Step 2: Apply noise filter
    cleaned_data = preprocess_register_data(quantum_data)

    # Step 3: Count state occurrences (potential distraction)
    state_counter = Counter(cleaned_data)

    # Step 4: Compute coherence metric
    score = compute_coherence_score(cleaned_data)

    # Step 5: Analyze log for error bursts (mostly irrelevant)
    error_tracker = defaultdict(int)
    burst_count = 0
    for entry in log_entries:
        if 'ERROR' in entry:
            error_tracker['total'] += 1
            if entry.count('!') > 2:
                burst_count += 1  # Unused downstream

    # Step 6: Detect rare states in quantum data
    anomaly_count = detect_anomalies(state_counter)

    # Step 7: Simulate hardware correction factor (distractor)
    correction_factor = 0
    for i in range(len(log_entries)):
        if i % 11 == 0:
            correction_factor += len(log_entries) // (i + 1)

    # Step 8: Weighted diagnostic calculation
    base_diagnostic = score * 100
    adjusted_diagnostic = base_diagnostic - (anomaly_count * 5)

    # Step 9: Apply fake environmental compensation (dead logic)
    temp_offset = 0
    for log in log_entries:
        if 'TEMP' in log:
            try:
                temp_offset += int(log.split('TEMP=')[1].split()[0])
            except:
                pass
    # Not used in final result

    # Step 10: Final decision logic
    if adjusted_diagnostic < 20:
        final_diagnostic = int(adjusted_diagnostic + 17)
    elif anomaly_count > 3:
        final_diagnostic = int(adjusted_diagnostic - 8)
    else:
        final_diagnostic = int(adjusted_diagnostic + 3)

    # Irrelevant debug output (looks important)
    debug_snapshot = {
        'coherence': score,
        'drops': len(quantum_data) - len(cleaned_data),
        'correction': correction_factor,
        'temp_shift': temp_offset
    }
    
    return final_diagnostic

# Input data setup
quantum_registers = [
    [1, 14, 0],
    [21, 3, 7],
    [5, 0, 9],
    [15, 6, 12]
]

system_log = [
    'STATUS OK',
    'ERROR! CRITICAL FAULT',
    'TEMP=23.5 C',
    'ERROR! SYSTEM STALL',
    'INFO: CYCLE COMPLETE',
    'ERROR!! RESTARTING'
]

# Execute main analysis
cleaned_input = preprocess_register_data([item for sublist in quantum_registers for item in sublist])
deprecated_result = deprecated_calibration(cleaned_input)  # Dead assignment

final_diagnostic = analyze_system_state(quantum_registers, system_log)
print(f"Target result: {final_diagnostic}")