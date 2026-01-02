import math

# Simulated sensor data from industrial monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.3, 26.0, 24.7, 23.9, 25.1]
pressure_readings = [101.3, 102.1, 100.9, 103.5, 104.0, 102.8, 101.7, 103.2]
humidity_readings = [45.2, 46.1, 44.8, 47.3, 48.0, 46.5, 45.9, 47.1]

# Irrelevant baseline constants for red herring
temp_baseline = 20.0
pressure_baseline = 100.0
humidity_baseline = 40.0

# Distractor: unused function
def calculate_average(data_list):
    return sum(data_list) / len(data_list)

# Distractor: dead code path
if False:
    adjusted_temps = [t * 1.02 for t in temperature_readings]
    adjusted_pressures = [p * 0.99 for p in pressure_readings]

# Real processing begins
scaling_factor = 1.15
offset_correction = 0.85

# Normalize readings using z-score (only temperature used in final logic)
normalized_temps = []
mean_temp = sum(temperature_readings) / len(temperature_readings)
std_temp = (sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)) ** 0.5
for t in temperature_readings:
    normalized_temps.append((t - mean_temp) / std_temp)

# Apply non-linear transformation with conditional expression
distorted_temps = [
    nt ** 3 if nt > 0 else math.log(abs(nt) + 1) * -1
    for nt in normalized_temps
]

# Accumulate transformed values with threshold filtering
accumulated_score = 0
for dt in distorted_temps:
    if abs(dt) > 0.5:
        accumulated_score += int(abs(dt) * 10)

# Process logs: extract severity levels
raw_log_entries = [
    {'timestamp': 1, 'type': 'INFO', 'value': 23.5},
    {'timestamp': 2, 'type': 'WARNING', 'value': 25.3},
    {'timestamp': 3, 'type': 'ERROR', 'value': 26.0},
    {'timestamp': 4, 'type': 'WARNING', 'value': 24.7},
    {'timestamp': 5, 'type': 'INFO', 'value': 23.9},
    {'timestamp': 6, 'type': 'ERROR', 'value': 25.1}
]

# Extract only error-level values
error_values = [entry['value'] for entry in raw_log_entries if entry['type'] == 'ERROR']
warning_values = [entry['value'] for entry in raw_log_entries if entry['type'] == 'WARNING']  # unused distractor

# Compute moving average of errors (only if more than one error)
if len(error_values) > 1:
    error_avg = sum(error_values) / len(error_values)
else:
    error_avg = 0.0

# Unused intermediate computations as red herrings
total_warnings = len(warning_values)
avg_warning_value = sum(warning_values) / len(warning_values) if warning_values else 0

# Processed logs contain both statistical score and error average
processed_logs = {
    'diagnostic_score': accumulated_score,
    'critical_average': error_avg,
    'size_flag': len(error_values) >= 2
}

# Distractor: complex but unused dictionary transformation
metadata_index = {}
for i, entry in enumerate(raw_log_entries):
    key = f"log_{i}_{entry['type'].lower()}"
    metadata_index[key] = math.sin(i * 0.5) + entry['value'] * 0.01

# Function to analyze processed logs
def analyze_readings(log_data):
    score = log_data['diagnostic_score']
    critical = log_data['critical_average']
    flag = log_data['size_flag']
    
    # Complex conditional logic with nested expressions
    base = score * 2 if critical > 25.0 else score
    adjustment = 10 if flag else -5
    
    # Additional computation with bit manipulation red herring
    mask = 0b1101
    decoy_result = base ^ mask  # irrelevant operation
    
    # Final calculation
    result = base + adjustment
    
    # Dead code path
    if __debug__:
        result += 1  # This does nothing in normal execution
    
    return int(result)

# Key statement
final_diagnostic = analyze_readings(processed_logs)

# Print result for verification
print(f"Result: {final_diagnostic}")