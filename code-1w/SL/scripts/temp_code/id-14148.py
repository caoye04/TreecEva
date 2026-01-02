import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 27.3, 20.2, 22.0, 26.8, 28.1, 18.7]
humidity_readings = [45, 52, 61, 48, 55, 70, 65, 50, 40, 72]
pressure_readings = [1013, 1015, 1010, 1008, 1018, 1020, 1005, 1012, 1016, 1009]

# Irrelevant calibration coefficients (distractor)
calibration_coefficients = [0.98, 1.02, 0.99, 1.01, 1.00, 0.97, 1.03, 0.96, 1.04, 0.95]
scaled_coeffs = [c * 1.05 for c in calibration_coefficients if c < 1.0]

# Misleading preprocessing: outlier detection with unused result
outliers = []
for i, temp in enumerate(temperature_readings):
    if abs(temp - sum(temperature_readings) / len(temperature_readings)) > 5:
        outliers.append((i, temp))

# Destructuring assignment (tuple unpacking) - relevant
primary_sensor, secondary_sensor = temperature_readings[0], humidity_readings[0]

# Composite calculation with bitwise manipulation (red herring)
composite_index = 0
for t, h in zip(temperature_readings, humidity_readings):
    composite_index ^= int(t) & int(h)
composite_index = composite_index % 100  # Unused in final logic

# Real processing begins: conditional filtering based on dynamic criteria
def apply_dynamic_filter(data, ref_value):
    return [x for x in data if x > ref_value - 2 and x < ref_value + 3]

ref_temp = sum(temperature_readings) / len(temperature_readings)
filtered_data = apply_dynamic_filter(temperature_readings, ref_temp)

# Create threshold map using dictionary comprehension and string operations (mixed paradigm)
device_ids = ['DEV001', 'DEV002', 'DEV003', 'DEV004']
threshold_map = {dev_id: {'temp': 25 + (i % 3), 'humidity': 60 - (i % 5)} 
                  for i, dev_id in enumerate(device_ids)}

# Simulate device status parsing from logs (irrelevant but complex)
log_entries = ['OK@DEV001', 'ERR@DEV002', 'OK@DEV003', 'PND@DEV004']
status_map = {entry.split('@')[1]: entry.split('@')[0] for entry in log_entries}

# Critical function with multiple concepts: list ops, conditionals, arithmetic
# Uses itertools to generate combinations (unused path as distractor)
def generate_combinations(lst):
    combos = []
    for r in range(2, 4):
        combos.extend(itertools.combinations(lst, r))
    return [(sum(combo), len(combo)) for combo in combos if sum(combo) > 50]  # Dead end

# Another decoy function that looks important but isn't called
def compute_rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(round(avg, 2))
    return sorted(averages, reverse=True)

# Real processing function with conditional expressions and destructuring
def process_readings(data, thresholds):
    # Use string method to simulate config lookup (meaningful use)
    mode_flag = 'high_precision'.replace('_', ' ').title().split()[0].lower()
    
    # Conditional expression based on mode
    base_ref = 25 if 'h' in mode_flag else 20
    
    # Multiple assignments and arithmetic transformations
    adjusted = [round(x * 1.02 - 0.5, 1) for x in data]
    deviations = [abs(x - base_ref) for x in adjusted]
    
    # Logical evaluation with short-circuiting
    high_deviation_count = sum(1 for d in deviations if d > 3.0)
    adjustment_factor = 0.9 if high_deviation_count > 2 else 1.0
    
    # Final computation with integer division and rounding
    total_score = sum(int(d * adjustment_factor) for d in deviations)
    
    # Key intermediate result (looks important but not final)
    diagnostic_proxy = total_score // len(deviations) if deviations else 0
    
    # Actual final result built from core logic
    final_sum = sum(adjusted) + diagnostic_proxy
    normalized_result = round(final_sum / 1.75, 6)  # Precise decimal output
    
    return int(normalized_result)  # Deterministic integer answer

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")