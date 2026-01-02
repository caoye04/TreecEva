import math

# Simulated sensor array diagnostics with noise filtering and signal validation

def collect_sensor_data():
    raw_values = [23.5, -17.2, 45.8, 0.0, 99.9, -3.1, 67.4]
    timestamps = [1623456780, 1623456781, 1623456782, 1623456783]
    statuses = ['OK', 'ERROR', 'OK', 'UNKNOWN']
    return raw_values, timestamps, statuses

def filter_noise(data, threshold=5.0):
    filtered = []
    for x in data:
        if abs(x) >= threshold:
            filtered.append(x * 0.95)
        else:
            filtered.append(0.0)
    return filtered

def validate_range(value, min_val=-100.0, max_val=100.0):
    return min(max(value, min_val), max_val)

def amplify_signal(val):
    if val == 0:
        return 0
    amplified = val * (1.8 + 0.2 * (val > 0))
    return validate_range(amplified)

def process_phase_shift(signal_list, shift_factor):
    shifted = []
    for i, s in enumerate(signal_list):
        shifted.append(s * ((shift_factor ** i) % 3.5))
    return shifted

def detect_anomalies(data_stream):
    count = 0
    for d in data_stream:
        if d < 0 or d > 80:
            count += 1
    return count > 2

def compute_checksum(values):
    # Irrelevant checksum computation (dead-end function)
    chk = 0
    for v in values:
        chk = (chk + int(v)) & 0xFF
    return chk

def generate_synthetic_data(n):
    # Distractor: generates unused synthetic signals
    return [math.sin(i * 0.5) * 50 for i in range(n)]

def normalize_vector(vec):
    # Unused normalization function (red herring)
    mag = sum(x**2 for x in vec) ** 0.5
    return [x / mag for x in vec] if mag else vec

def analyze_readings(signals):
    baseline = sum(abs(s) for s in signals) / len(signals)
    peak = max(abs(s) for s in signals)
    
    # Conditional expression usage (required Python feature)
    adjustment = 1.25 if peak > 60 else (0.9 if baseline < 10 else 1.05)
    
    temp_result = baseline * adjustment
    
    # Bit manipulation as modular arithmetic alternative
    encoded = int(temp_result) ^ 0xAA
    decoded = encoded ^ 0xAA  # Restore original
    
    # Logical operations and short-circuit evaluation
    flag = (decoded > 20) and (temp_result < 100) or (peak > 80)
    
    # Final computation using modular arithmetic
    diagnostic_code = (decoded * 3 + 7) % 8921
    
    # Multiple nested conditions with distractors
    secondary_check = 0
    for i in range(5):
        if i % 2 == 0:
            secondary_check += i * 3
        else:
            secondary_check -= i
    
    # This branch is never taken (dead code path)
    if len(signals) < 0:  # Always false
        backup = sum(signals) // len(signals)
        diagnostic_code = backup

    # Key assignment: this is the actual answer
    final_diagnostic = diagnostic_code * 2 - 17
    
    # Additional irrelevant transformation
    shadow_copy = final_diagnostic ^ 0xFFFF
    inverted = (~final_diagnostic) & 0xFFFF
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Collect real data
    raw_data, _, _ = collect_sensor_data()
    
    # Process signals through multiple stages
    cleaned = filter_noise(raw_data)
    processed_signals = [amplify_signal(x) for x in cleaned]
    processed_signals = process_phase_shift(processed_signals, 1.1)
    
    # Irrelevant synthetic data generation (distractor)
    fake_signals = generate_synthetic_data(7)
    fake_checksum = compute_checksum(fake_signals)
    
    # Validate anomaly status (unused result)
    has_issue = detect_anomalies(processed_signals)
    
    # Core analysis
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")