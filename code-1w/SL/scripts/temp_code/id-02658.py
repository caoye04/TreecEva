from collections import defaultdict, Counter
import math

# Simulated health monitoring system with diagnostic logic
def analyze_vital(vital, baseline, deviation_factor):
    return abs(vital - baseline) > deviation_factor * baseline

# Irrelevant utility function (decoy)
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

# Unused but plausible data transformation
def encrypt_code(code_str):
    return ''.join(chr((ord(c) + 3) % 128) for c in code_str)

# Core diagnostic processing
def compute_stability_index(readings):
    if len(readings) < 2:
        return 0.0
    variance = sum((readings[i+1] - readings[i]) ** 2 for i in range(len(readings)-1))
    return round(math.sqrt(variance / (len(readings) - 1)), 4) if variance else 0.0

# Bit manipulation for noise filtering (actually used)
def filter_noise(flag_code):
    # Extract only bits corresponding to valid sensor inputs
    valid_mask = 0b111111  # Only lower 6 bits are meaningful
    return flag_code & valid_mask

# Data integrity check (distractor)
def verify_checksum(data_block):
    checksum = 0
    for b in data_block.encode():
        checksum ^= b
    return format(checksum, '02x')

# Main processing function
def process_metrics(data, limits):
    diagnostics = defaultdict(int)
    stability_scores = []
    
    # Process each patient's vital stream
    for pid, vitals in data.items():
        temp, hr, bp, o2, resp, neuro = vitals
        
        # Boolean logic chain with comparisons and logical ops
        is_critical = (temp > limits['temp_high'] or temp < limits['temp_low'])
        is_critical = is_critical or (hr > limits['hr_high'])
        is_critical = is_critical and (o2 < limits['o2_low'])  # Short-circuit condition
        
        # Bitwise encoding of anomaly flags
        anomaly_flags = 0
        anomaly_flags |= (analyze_vital(temp, 37.0, 0.05) << 0)
        anomaly_flags |= (analyze_vital(hr, 75, 0.2) << 1)
        anomaly_flags |= (analyze_vital(bp, 120, 0.15) << 2)
        anomaly_flags |= (analyze_vital(o2, 98, 0.02) << 3)
        anomaly_flags |= (analyze_vital(resp, 16, 0.25) << 4)
        anomaly_flags |= (analyze_vital(neuro, 50, 0.3) << 5)
        
        # Filter noise from anomaly detection (key step)
        filtered_flags = filter_noise(anomaly_flags)
        
        # Count active anomalies
        active_anomalies = bin(filtered_flags).count('1')
        diagnostics[pid] = active_anomalies
        
        # Stability tracking on heart rate trend (used later)
        if len(vitals) >= 3:
            stability_scores.append(compute_stability_index([hr, bp, o2]))

    # Aggregate analysis
    total_anomalies = sum(diagnostics.values())
    
    # Red herring: unused complex calculation
    encrypted_diag = encrypt_code(f"ALERT-{total_anomalies}")
    
    # Real result computation
    avg_stability = sum(stability_scores) / len(stability_scores) if stability_scores else 0.0
    
    # Final diagnostic score combines anomalies and stability
    # Weighted combination: more instability increases diagnostic severity
    final_score = total_anomalies * 100 - int(avg_stability * 50)
    
    # Dead code path (never executed due to data)
    if False and len(encrypted_diag) > 10:
        final_score += 1000
    
    # Key output variable
    final_diagnostic = abs(final_score)  # Ensure positive index
    
    # Distractor print (not part of logic)
    _ = verify_checksum("DIAGNOSTIC_FRAME")
    
    return final_diagnostic

# Input data setup
health_data = {
    'P001': [38.2, 102, 138, 91, 22, 45],  # Elevated vitals
    'P002': [36.8, 88, 118, 96, 18, 52],   # Mild deviation
    'P003': [37.1, 74, 122, 99, 16, 49],   # Near normal
    'P004': [39.4, 118, 142, 87, 24, 40]   # Severe case
}

thresholds = {
    'temp_low': 36.0, 'temp_high': 38.0,
    'hr_high': 100,
    'bp_high': 140,
    'o2_low': 95,
    'resp_high': 20,
    'neuro_low': 45
}

# Signal normalization (unused but plausible)
signal_stream = [1.2, 0.8, 1.5, 2.1, 1.7]
normalized = normalize_signal(signal_stream)

# Execute main logic
temp_cache = [compute_stability_index([1, 2, 3]), compute_stability_index([5, 5, 5])]
final_diagnostic = process_metrics(health_data, thresholds)

# Output result
print(f"Result: {final_diagnostic}")