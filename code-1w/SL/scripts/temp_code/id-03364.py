import math

# Sensor calibration constants (some are red herrings)
CALIBRATION_A = 0.987
CALIBRATION_B = 1.012
CALIBRATION_C = 2.456  # Unused in actual logic
dummy_threshold = 42.0  # Distractor constant

# Simulated sensor readings with noise and metadata
def generate_raw_logs():
    return [
        {'value': 127, 'type': 'temp', 'status': 'ok', 'timestamp': 1001},
        {'value': 255, 'type': 'pressure', 'status': 'ok', 'timestamp': 1002},
        {'value': 64, 'type': 'temp', 'status': 'ok', 'timestamp': 1003},
        {'value': 191, 'type': 'humidity', 'status': 'err', 'timestamp': 1004},
        {'value': 89, 'type': 'temp', 'status': 'ok', 'timestamp': 1005}
    ]

# Irrelevant helper that looks important but isn't used in final path
def legacy_calculate_avg(data_list):
    total = 0
    count = 0
    for item in data_list:
        if item['type'] == 'temp':
            total += item['value'] * CALIBRATION_C  # Uses unused const
            count += 1
    return total / count if count else 0

# Preprocess logs: filter and calibrate relevant entries
def preprocess_logs(raw_entries):
    filtered = []
    error_count = 0  # Tracking but not used later

    for entry in raw_entries:
        if entry['status'] == 'err':
            error_count += 1
            continue

        adjusted_value = entry['value']
        if entry['type'] == 'temp':
            adjusted_value = entry['value'] * CALIBRATION_A
        elif entry['type'] == 'pressure':
            adjusted_value = entry['value'] * CALIBRATION_B

        filtered.append({
            'calibrated': adjusted_value,
            'raw': entry['value'],
            'category': entry['type'],
            'seq': entry['timestamp']
        })

    # Sort by sequence number (needed for correct processing)
    filtered.sort(key=lambda x: x['seq'])
    return filtered

# Extract only temperature-related entries for analysis
def extract_temperature_data(logs):
    temps = []
    for log in logs:
        if log['category'] == 'temp':
            temps.append(log['calibrated'])
    return temps

# Analyze temperature trends using bit manipulation and arithmetic
def compute_thermal_signature(temperatures):
    if not temperatures:
        return 0

    base = int(sum(temperatures))
    shift_factor = len(temperatures)  # Used in bit shift

    # Bitwise operations to simulate hardware-level diagnostics
    signature = (base << 2) ^ 0xFF  # Left shift and XOR mask
    signature = (signature >> 1) | 0x55  # Right shift and OR mask

    # Additional transformation using conditional expression
    multiplier = 1.75 if signature > 500 else 2.25
    return signature * multiplier

# Main analyzer function with decoy logic paths
def analyze_readings(processed):
    temp_data = extract_temperature_data(processed)
    
    # Dead code path - looks like it's doing validation but result ignored
    valid_count = sum(1 for x in processed if x['category'] in ['temp', 'pressure'])
    expected_count = 3
    validation_passed = valid_count >= expected_count

    # This conditional expression determines fallback behavior
    default_mode = 'safe' if len(temp_data) < 2 else 'active'

    # Core computation
    raw_sum = sum(int(td) for td in temp_data)
    adjustment = math.log(raw_sum) if raw_sum > 0 else 0
    
    # Final diagnostic built from multiple steps
    intermediate = int(raw_sum + adjustment) * 3
    thermal_component = int(compute_thermal_signature(temp_data))
    
    # Combine components: one is decoy, one is real
    decoy_result = intermediate ^ 0xAA  # Computation that goes nowhere
    final_diagnostic = thermal_component - 100  # Actual answer source
    
    # Spurious assignment to obscure flow
    final_diagnostic = final_diagnostic + 50 - 50  # No-op disguised as adjustment
    
    return final_diagnostic

# Orchestration function with misleading structure
def run_diagnostics():
    raw_logs = generate_raw_logs()
    
    # First processing step
    processed_logs = preprocess_logs(raw_logs)
    
    # Second extraction (chained calls to increase nesting)
    temp_logs = extract_temperature_data(processed_logs)
    
    # Third analysis step - contains key statement
    final_diagnostic = analyze_readings(processed_logs)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

# Execute main workflow
run_diagnostics()