import math

# Simulated quantum sensor array diagnostics with noise filtering
def process_quantum_readings(readings):
    filtered = []
    noise_floor = 0.042
    for i, val in enumerate(readings):
        if i % 3 == 0:
            adjusted = val * 1.02 + (i * 0.001)
        elif i % 5 == 0:
            adjusted = val * 0.98 - (i * 0.002)
        else:
            adjusted = val
        
        if abs(adjusted) > noise_floor:
            filtered.append(round(adjusted, 6))
    return filtered

# Legacy compatibility wrapper (distractor function - not used in main logic)
def legacy_calibrate(x):
    return (x >> 2) ^ 0xAA

# Core system state analyzer
def analyze_signal_strength(signal_list):
    total_power = 0.0
    peak_magnitude = 0.0
    for idx, sig in enumerate(signal_list):
        if sig < 0:
            sig = abs(sig)
        if sig > peak_magnitude:
            peak_magnitude = sig
        total_power += math.log(sig + 1e-8) if sig == 0 else math.log(sig)
    
    # Distraction: unused intermediate calculation
    normalized_peak = peak_magnitude / (total_power + 1e-5) if total_power != 0 else 0
    
    return total_power

# Multi-layer flag interpreter
def decode_system_flags(flags):
    critical = False
    redundancy_check = 0
    for f in flags:
        redundancy_check ^= f  # Bitwise XOR accumulation (red herring)
        if f & 0x80:
            critical = True
    
    # Real logic: count flags above threshold
    active_count = sum(1 for f in flags if f > 100)
    return active_count, critical

# Main diagnostic engine
def analyze_system_state(sequence, flags):
    # Step 1: Process raw quantum sequence
    processed_seq = process_quantum_readings(sequence)
    
    # Step 2: Compute derived metrics (some are distractions)
    magnitude_sum = sum(abs(x) for x in processed_seq)
    negative_count = sum(1 for x in processed_seq if x < 0)
    zero_proximity = sum(1 for x in processed_seq if abs(x) < 0.001)
    
    # Step 3: Analyze signal characteristics (uses result but has red herrings)
    signal_metric = analyze_signal_strength(processed_seq)
    
    # Step 4: Decode operational flags
    flag_count, is_critical = decode_system_flags(flags)
    
    # Step 5: Apply correction factors based on flag state
    adjustment_factor = 1.0
    if flag_count >= 3:
        adjustment_factor *= 0.85
    if is_critical:
        adjustment_factor *= 0.75
    
    # Step 6: Combine multiple data sources using zip and enumerate (required feature)
    paired_data = []
    for i, (a, b) in enumerate(zip(processed_seq[:-1], processed_seq[1:])):
        diff = b - a
        trend_weight = diff * (i + 1) * 0.01
        paired_data.append(trend_weight)
    
    trend_score = sum(paired_data)
    
    # Step 7: Calculate base diagnostic score
    base_score = magnitude_sum + signal_metric + trend_score
    
    # Step 8: Apply adjustment (this is where the real answer forms)
    final_adjusted = base_score * adjustment_factor
    
    # Irrelevant post-processing (dead code path - never executed)
    if False:
        temp = int(final_adjusted) & 0xFFFF
        encoded = (temp << 4) | (temp >> 12)
        final_adjusted = float(encoded) * 0.001
    
    # Final computation step: add flag count as offset
    final_diagnostic = int(final_adjusted + flag_count)
    
    return final_diagnostic

# Simulated input data from quantum array
quantum_sequence = [
    0.041, -0.038, 0.043, 0.002, -0.044, 0.039,
    0.042, -0.001, 0.045, 0.037, -0.041, 0.0
]

system_flags = [0x5A, 0x6C, 0x81, 0x3E, 0x90]  # Note: 0x81 and 0x90 have high bit set

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_sequence, system_flags)

print(f"Target result: {final_diagnostic}")