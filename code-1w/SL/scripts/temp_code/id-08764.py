def analyze_signal_integrity(bandwidth, packets):
    base_latency = 12.5
    jitter_buffer = 0.0
    signal_strength = [p['strength'] for p in packets if p['bandwidth_ratio'] > bandwidth]
    
    # Irrelevant power calculation (distractor)
    total_power_used = sum([p['strength'] * 0.3 for p in packets])
    efficiency_ratio = total_power_used / (len(packets) + 1)

    # Real processing begins
    delays = [p['delay'] for p in packets]
    phase_codes = []
    for d in delays:
        if d < 5:
            phase_codes.append(1)
        elif d < 10:
            phase_codes.append(-1)
        else:
            phase_codes.append(2)

    # Secondary irrelevant transformation
    encoded_peaks = [d % 3 for d in delays if d > 7]
    peak_magnitude = sum(encoded_peaks) / (len(encoded_peaks) or 1)

    # Core logic with list comprehension
    adjusted_phases = [pc * (1 + (bw * 0.1)) for pc, bw in zip(phase_codes, [p['bandwidth_ratio'] for p in packets])]
    
    # Aggregation step
    raw_shift = sum(adjusted_phases)
    correction_factor = len([d for d in delays if d % 2 == 0])
    net_phase_shift = int(raw_shift - correction_factor)

    # Final red herring computation (not used)
    timing_entropy = 0.0
    for i in range(len(delays)):
        for j in range(i+1, len(delays)):
            timing_entropy += abs(delays[i] - delays[j])
    timing_entropy /= (len(delays) ** 2)

    final_adjustment = process_timing(delays, phase_codes)
    return net_phase_shift


def process_timing(delays, codes):
    # Dummy helper function to mislead about importance
    weighted_sum = 0
    for i, d in enumerate(delays):
        weighted_sum += d * codes[i] * 0.1
    return round(weighted_sum, 3)

# Input data
packets_data = [
    {'strength': 45, 'bandwidth_ratio': 0.4, 'delay': 3},
    {'strength': 60, 'bandwidth_ratio': 0.7, 'delay': 8},
    {'strength': 52, 'bandwidth_ratio': 0.5, 'delay': 12},
    {'strength': 33, 'bandwidth_ratio': 0.9, 'delay': 4},
    {'strength': 70, 'bandwidth_ratio': 1.2, 'delay': 11}
]

# Execution entry point
result_value = analyze_signal_integrity(0.6, packets_data)
print(f"Result: {result_value}")