def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper that's never called
def deprecated_filter(data):
    return [x for x in data if x > 0]

# Decoy transformation with misleading intermediate output
def transform_magnitude(signal):
    result = []
    for val in signal:
        if val < 0:
            result.append(abs(val) ** 0.5 * -1)
        else:
            result.append(abs(val) ** 0.5)
    print(f'Debug: Transformed magnitude preview = {result[:2]}')  # Distractor output
    return result

# Main analysis function with early returns and conditional logic
def analyze_signal(data, limit):
    if not data:
        return -999

    total_power = sum(x ** 2 for x in data)
    average_amplitude = round(sum(abs(x) for x in data) / len(data), 4)
    
    # Bit manipulation red herring
    magic_offset = (len(data) ^ 255) & 17
    decoy_value = (magic_offset << 3) | 7

    # Conditional expression with case conversion distraction
    signal_type = 'complex' if any(isinstance(x, str) and x.lower() == 'qam' for x in ["QAM", "PSK"] ) else 'real'
    
    # Critical branching logic with short-circuiting
    if signal_type == 'complex' and len(data) > 10 or total_power < limit:
        adjustment = 0.85
        # Dead code path - never reached due to logic above
        if total_power > 1000:
            adjustment *= 1.2  # unreachable
    else:
        adjustment = 1.15

    # Core calculation (answer depends on this)
    base_diagnostic = int(total_power * adjustment) + magic_offset
    
    # Simulate diagnostic calibration with list comprehension side effect
    calibration_steps = [base_diagnostic // (i+1) for i in range(3)]
    final_adjustment = sum(calibration_steps) % 19

    final_diagnostic = base_diagnostic - final_adjustment
    
    # Redundant string formatting (distractor)
    status_msg = f"Signal OK: {str(final_diagnostic).zfill(6)}\n"
    print(status_msg.strip())  # Misleading output but not the answer

    return final_diagnostic

# Unused data structures for interference
historical_logs = {'errors': [], 'counts': {}}
debug_registry = set()

# Primary execution flow
raw_input_data = [0.12, -0.34, 0.56, -0.78, 0.23, -0.45, 0.67, -0.89, 0.14, -0.25, 0.36]
processed_data = preprocess_signal(raw_input_data)
threshold = 0.4 * len(processed_data)

# Key statement
final_diagnostic = analyze_signal(processed_data, threshold)
print(f'Result: {final_diagnostic}')