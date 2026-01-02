import math

# Simulated telemetry data from a satellite subsystem
base_readings = [14, 7, 23, 11, 5, 19, 3]
telemetry_log = {f'sensor_{i}': base_readings[i] for i in range(len(base_readings))}

def apply_calibration(data):
    # Irrelevant calibration function (dead path)
    return {k: v * 1.05 for k, v in data.items()}

def filter_anomalies(log):
    # Misleading preprocessing: filters values > 20 (only one element)
    filtered = {k: v for k, v in log.items() if v <= 20}
    return filtered

def compute_checksum(seq):
    # Red herring: computes sum of squares mod 1000
    checksum = sum([x**2 for x in seq]) % 1000
    temp_result = checksum * 2  # Distractor
    return checksum

def generate_sequence(n):
    # Unused sequence generator (dead code)
    return [i**2 % 17 for i in range(n)]

def rolling_window_avg(values, window_size=3):
    # Decoy function: calculates moving average but not used in final result
    averages = []
    for i in range(len(values) - window_size + 1):
        avg = sum(values[i:i+window_size]) / window_size
        averages.append(avg)
    return averages

def transform_data(log_dict):
    # Extracts and transforms values using slicing and lambda
    values = list(log_dict.values())
    shifted = values[1:] + [values[0]]  # Rotate left by 1
    processed = list(map(lambda x: (x * 2) + 1, shifted))  # Transform each element
    return processed

def integrate_subsystems(primary, secondary):
    # Complex but irrelevant integration logic
    combined = []
    for i in range(min(len(primary), len(secondary))):
        combined.append(primary[i] ^ secondary[i])  # Bitwise XOR
    return combined or [0]  # Default fallback

def validate_consistency(arr):
    # Checks parity count (distraction)
    even_count = sum(1 for x in arr if x % 2 == 0)
    return even_count >= 3

def analyze_system_state(log):
    # Core logic hidden among distractions
    raw_values = list(log.values())
    
    # Step 1: Apply reverse slicing to get last four then first three
    segment_a = raw_values[-4:]
    segment_b = segment_a[:3]  # Take first three of last four
    
    # Step 2: Compute weighted contribution
    weights = [1, -1, 2]
    weighted_sum = sum(segment_b[i] * weights[i] for i in range(len(weights)))
    
    # Step 3: Use dictionary key counting
    key_count = len(log.keys())
    offset = key_count // 2
    
    # Step 4: Combine with modular arithmetic
    intermediate = (weighted_sum + offset) % 13
    
    # Step 5: Add constant derived from list length
    adjustment = len(raw_values)  # = 7
    
    # Step 6: Final transformation
    result = (intermediate * 3) + adjustment
    
    # Irrelevant branching (does not affect result)
    if result > 10:
        temp_flag = True
        buffer = [result * 2]  # Unused
    else:
        temp_flag = False
    
    # More red herrings
    dummy_lookup = {'a': 1, 'b': 2, 'c': result * 10}  # Unused
    
    return result

# Main execution flow
adjusted_telemetry = filter_anomalies(telemetry_log)
data_stream = transform_data(adjusted_telemetry)

# Unused components adding interference
checksum_val = compute_checksum(base_readings)
smoothed_data = rolling_window_avg(base_readings)
validation_ok = validate_consistency(data_stream)

# Critical statement
final_diagnostic = analyze_system_state(telemetry_log)

print(f"Result: {final_diagnostic}")