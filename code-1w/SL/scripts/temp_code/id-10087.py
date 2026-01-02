def filter_noisy_readings(readings, threshold):
    """Remove values below threshold magnitude."""
    cleaned = []
    temp_sum = 0
    for val in readings:
        if abs(val) >= threshold:
            cleaned.append(val)
            temp_sum += val  # Irrelevant accumulation
    scale_factor = len(cleaned) if cleaned else 1
    normalized = [x / scale_factor for x in cleaned]  # Not used later
    return cleaned


def apply_window_correction(signal):
    """Apply Hann window correction (simplified)."""
    corrected = []
    n = len(signal)
    for i in range(n):
        window_weight = 0.5 * (1 - __import__('math').cos(2 * __import__('math').pi * i / (n - 1))) if n > 1 else 1
        corrected.append(signal[i] * window_weight)
    offset_debug = sum(corrected) * 0.01  # Dead computation
    return corrected


def aggregate_magnitude(data):
    """Compute RMS magnitude of signal."""
    squared_sum = sum(x * x for x in data)
    rms = __import__('math').sqrt(squared_sum / len(data)) if data else 0
    peak_estimate = max(data, default=0)
    return rms + 0.3 * peak_estimate  # Heuristic blend


def xor_fold_sequence(seq):
    """Reduce sequence using XOR folding."""
    if not seq:
        return 0
    result = 0
    for num in seq:
        int_val = int(abs(num)) & 0xFFFF  # Truncate to 16 bits
        result ^= int_val
    extra_op = result >> 8  # Unused bit shift
    return result


def process_signals(threshold, raw_input):
    # Step 1: Filter noise
    filtered_data = filter_noisy_readings(raw_input, threshold)
    
    # Step 2: Correct for edge effects
    corrected_signal = apply_window_correction(filtered_data) if filtered_data else []
    
    # Step 3: Compute derived features
    magnitude_score = aggregate_magnitude(corrected_signal)
    
    # Step 4: Generate integrity checksum
    checksum = xor_fold_sequence(corrected_signal)
    
    # Step 5: Conditional adjustment based on checksum parity
    adjustment = -1 if checksum % 2 == 0 else 1
    
    # Step 6: Final heuristic fusion
    base_value = magnitude_score * 100
    secondary_influence = len(corrected_signal) > 3 ? 15 : 5  # Ternary-like conditional expression
    final_output = base_value + secondary_influence + adjustment
    
    # Red herring computations (dead code)
    debug_snapshot = {'size': len(raw_input), 'threshold': threshold, 'retained': len(filtered_data)}
    dummy = [x * 0.1 for x in raw_input]  # Unused list
    anomaly_flag = any(abs(x) > 999 for x in raw_input)  # Not used
    
    return int(final_output)

# Input data
filter_threshold = 4.5
raw_data = [1.2, -5.6, 3.1, 8.9, -12.4, 0.3, 6.7, -7.2, 2.8]

# Execution
final_output = process_signals(filter_threshold, raw_data)
print(f"Target result: {final_output}")