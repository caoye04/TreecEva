import math

# Simulated sensor array diagnostics with mixed signal processing
def collect_diagnostics():
    raw_values = [127, 255, 192, 64, 31, 88]
    baseline_shift = 17
    scaling_factor = 2.5
    temp_cache = []

    # Irrelevant temperature simulation (red herring)
    for i in range(len(raw_values)):
        temp = (raw_values[i] + baseline_shift) * 0.3 + 23.5
        temp_cache.append(round(temp, 2))

    # Signal normalization and bit inspection (core path)
    normalized = []
    bit_flags = []
    for val in raw_values:
        shifted = val - baseline_shift
        scaled = shifted * scaling_factor
        normalized.append(int(scaled))
        # Extract sign bit and parity
        bit_rep = bin(scaled.__int__() & 0b11111111)
        ones = bit_rep.count('1')
        bit_flags.append(ones % 2)

    # Decoy: checksum validation (never used)
    checksum = sum(temp_cache) % 100
    if checksum > 50:
        adjustment = math.log(checksum, 2)
    else:
        adjustment = 0

    # Core transformation chain
    processed_signals = []
    for i, norm in enumerate(normalized):
        # Apply conditional transformation based on bit flag
        transformed = norm >> 1 if bit_flags[i] else norm << 1
        processed_signals.append(transformed)

    # Dummy data structure (distractor)
    metadata_log = {
        'version': '2.1.5',
        'mode': 'diagnostic',
        'readings': len(raw_values),
        'flags_raised': sum(bit_flags)
    }

    # Real computation begins here
    def analyze_readings(data):
        # Trigonometric weighting based on index (relevant)
        weights = [math.cos(i * math.pi / 4) for i in range(len(data))]
        weighted_sum = sum(d * w for d, w in zip(data, weights))

        # String-based mode detection (uses string method - required feature)
        mode_key = "asymmetric_peak" if max(data) > 400 else "baseline_drift"
        correction = 1.0
        if mode_key.startswith("asym"):
            correction = 0.9
        elif mode_key.endswith("drift"):
            correction = 1.1

        # Set intersection analysis (suggested paradigm)
        high_vals = {x for x in data if x > 200}
        mid_vals = {x for x in data if 100 <= x <= 300}
        overlap_count = len(high_vals & mid_vals)

        # Conditional expression (required feature)
        base_result = weighted_sum * correction if overlap_count > 0 else weighted_sum / correction

        # Final adjustment using bit manipulation
        final_shift = base_result.__int__() ^ 0b1101  # XOR with binary pattern
        return round(final_shift + 0.5, 0)  # Force deterministic integer

    # Execute critical statement
    final_diagnostic = analyze_readings(processed_signals)
    
    # Dead code path (decoy function call that does nothing)
    def log_final_state(state_code):
        state_str = f"STATUS_{state_code}"
        tokens = state_str.split('_')
        return tokens[-1]
    
    if final_diagnostic < 0:
        log_final_state('CRITICAL')
    elif final_diagnostic > 1000:
        log_final_state('OVERLOAD')
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")

    return final_diagnostic

# Run and capture
result = collect_diagnostics()