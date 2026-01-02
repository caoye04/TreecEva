import math

# Sensor calibration constants (irrelevant to final result but look important)
BASE_SENSITIVITY = 0.87
CALIBRATION_OFFSET = 12.3
dummy_counter = 0

# Simulated environmental sensor readings
temp_readings = [22.1, 23.5, 24.0, 21.8, 25.3, 26.7, 20.4]
humidity_readings = [45, 48, 52, 58, 44, 60, 55]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1020, 1008]

# Irrelevant transformation: normalize humidity with no effect on outcome
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

# Unused function - red herring
def calculate_heat_index(temp, humidity):
    return 0.5 * (temp + humidity)

# Another decoy: computes average drift (never used)
def compute_drift(data):
    return sum(abs(data[i+1] - data[i]) for i in range(len(data)-1)) / len(data)

drift_warning = compute_drift(temp_readings) > 1.0

# Real processing begins here
processed_temps = [round(t * 1.02) for t in temp_readings if t > 21]

# Misleading intermediate aggregation
aggregated_stats = {
    'avg_temp': sum(temp_readings) / len(temp_readings),
    'max_humidity': max(humidity_readings),
    'min_pressure': min(pressure_readings),
    'temp_variance': sum((t - 24.0)**2 for t in temp_readings) / len(temp_readings)
}

# Decoy dictionary with plausible but unused keys
threshold_map = {
    'safe_temp_range': (18, 30),
    'ideal_humidity': (40, 60),
    'pressure_stable': 5,
    'critical_multiplier': 2.5,  # unused
    'fallback_mode': False      # unused
}

# Auxiliary function that appears critical but only some parts matter
def validate_stability(readings, tolerance=1.5):
    deviations = [abs(r - 24.0) for r in readings]
    unstable_count = sum(1 for d in deviations if d > tolerance)
    return unstable_count < 3

# This function looks like it does a lot, but only one line matters
# Distractor: uses dictionary, list comprehension, conditionals
# Only the count of temps > 24.5 contributes to final answer
processed_data = {
    'readings': [t for t in processed_temps if t >= 23],
    'count': len([t for t in processed_temps if t >= 23]),
    'stable': validate_stability(temp_readings),
    'flags': [],
    'version': '2.1a'
}

# Dead code path - never executed, but adds confusion
if __debug__:
    processed_data['flags'].append('DEBUG_ACTIVE')

# Critical function: heavily obscured by irrelevant logic
# Most parameters are ignored; only specific internal logic counts
# Note: threshold_map is passed but only safe_temp_range is checked, and even then partially
# The actual answer comes from a side computation involving modulo and bit counting
# Misleading use of dictionary operations and nested logic
# Final answer depends only on: sum of processed_temps elements > 24.5, mod 7, then XOR with bit count of 42

def analyze_readings(data, thresholds):
    # Extract relevant temperatures
    relevant_temps = [t for t in data['readings'] if t > 24.5]
    
    # Compute sum of relevant temps
    temp_sum = sum(relevant_temps)
    
    # These variables look important but don't affect output
    diagnostic_code = 0
    if data['stable'] and temp_sum > 50:
        diagnostic_code |= 0x10
    if len(data['flags']) > 0:
        diagnostic_code |= 0x08
    
    # Threshold check - looks critical, but result unused
    low_t, high_t = thresholds['safe_temp_range']
    within_bounds = all(low_t <= t <= high_t for t in data['readings'])
    
    # This block runs but doesn't contribute to final number
    if not within_bounds:
        fallback = thresholds.get('fallback_mode', False)
        if fallback:
            temp_sum *= thresholds['critical_multiplier']

    # Core computation (hidden among distractions)
    base_value = temp_sum % 7  # 79 % 7 = 2
    
    # Additional transformation: count set bits in 42 (which is 3: 101010)
    bit_count = bin(42).count('1')  # 3
    
    # Final deterministic result: 2 XOR 3 = 1
    final_diagnostic = base_value ^ bit_count
    
    # Return includes many fields, but only one matters
    return {
        'diagnostic': final_diagnostic,
        'raw_sum': temp_sum,
        'base': base_value,
        'bits': bit_count,
        'version': data['version'],
        'timestamp': 1712345678
    }['diagnostic']

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")