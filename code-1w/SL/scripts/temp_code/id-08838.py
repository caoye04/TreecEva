def analyze_performance(raw_data, baseline):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_data if x > 0]
    adjusted = [round(n * 0.98) for n in normalized]

    # Dead code path (unused function)
    def deprecated_filter(arr):
        return [a for a in arr if a % 2 == 0]

    # Unused statistical computation
    mean_val = sum(adjusted) / len(adjusted) if adjusted else 0
    variance = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0

    # Relevant transformation: extract magnitude and phase
    magnitude = [abs(x) for x in raw_data]
    phase_shift = [x % 37 for x in magnitude]  # Modular arithmetic

    # Bit manipulation red herring
    bit_analysis = 0
    for p in phase_shift:
        bit_analysis ^= (p << 1) | (p >> 2)
    
    # Linear search for critical threshold breach
    breach_index = -1
    for i, val in enumerate(magnitude):
        if val > baseline * 2.5:
            breach_index = i
            break

    # Decoy dictionary with misleading diagnostics
    decoy_health = {
        'status': 'unstable',
        'error_count': 12,
        'last_reset': 'never'
    }

    # Real processing begins: frequency of significant events
    event_freq = {}
    for m in magnitude:
        if m > baseline:
            event_freq[m] = event_freq.get(m, 0) + 1

    # Use of zip and enumerate (required Python features)
    ranked_events = []
    sorted_magnitude = sorted(set(magnitude), reverse=True)
    for idx, (rank, mag) in enumerate(zip(range(len(sorted_magnitude)), sorted_magnitude)):
        if rank < 10:  # Top 10 only
            ranked_events.append((idx + rank, mag))

    # Conditional expression with distractor logic
    signal_quality = 'high' if len(ranked_events) > 5 else 'low'
    penalty = 15 if signal_quality == 'high' else 5

    # Core logic hidden among distractions: compute diagnostic score
    total_weight = 0
    for key, count in event_freq.items():
        if key % 5 == 0:  # Only multiples of 5 contribute
            total_weight += key // count if count > 0 else 0

    # Additional irrelevant set operation
    unique_phases = set(phase_shift)
    phase_gaps = [sorted(unique_phases)[i+1] - sorted(unique_phases)[i] 
                 for i in range(len(unique_phases)-1)]

    # Final computation tied to breach index (key dependency)
    adjustment_factor = abs(breach_index * penalty)
    if adjustment_factor == 0:
        adjustment_factor = 7

    # Critical statement
    final_diagnostic = (total_weight * adjustment_factor) - bit_analysis % 100

    # Print required output
    print(f"Result: {final_diagnostic}")

# Simulate input data
log_entries = [42, -18, 95, 63, 42, 150, -9, 37, 95, 204]
system_threshold = 40

# Execute main logic
analyze_performance(log_entries, system_threshold)