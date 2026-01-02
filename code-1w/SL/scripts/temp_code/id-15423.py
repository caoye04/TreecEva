import math

# Material science simulation: stress-strain analysis with noise filtering

def preprocess_readings(raw_data):
    filtered = []
    for val in raw_data:
        if val < 0:  # Ignore invalid negative readings
            continue
        if val > 1000:  # Sensor overflow, cap value
            val = 1000
        normalized = round(val / 10.0, 2)
        if str(normalized).endswith('5'):
            normalized += 0.01  # Minor calibration adjustment
        filtered.append(normalized)
    return sorted(filtered, reverse=True)

# Irrelevant helper - simulates temperature drift (unused in final path)
def estimate_thermal_drift(samples):
    base = sum(samples) / len(samples)
    drift = 0
    for i, s in enumerate(samples):
        drift += (s - base) * math.sin(i)
    return drift * 0.01

# Signal integrity check - never actually called
def validate_signal_integrity(data_str):
    if not isinstance(data_str, str):
        data_str = ','.join(map(str, data_str))
    checksum = sum(ord(c) for c in data_str if c.isdigit()) % 7
    return checksum == 3

# Core transformation: applies polynomial correction to stress levels
def apply_polynomial_correction(levels):
    corrected = []
    for x in levels:
        # Third-degree response curve
        y = 0.001 * x**3 - 0.05 * x**2 + 2.3 * x + 10
        corrected.append(round(y, 3))
    return corrected

# Secondary filter: removes outliers based on moving median (not used)
def remove_outliers_mad(data):
    if len(data) < 3:
        return data[:]
    med = sorted(data)[len(data)//2]
    devs = [abs(x - med) for x in data]
    mad = sorted(devs)[len(devs)//2]
    return [x for x in data if abs(x - med) <= 3 * mad]

# Main calculation engine
def calculate_strain_response(stress_input, settings):
    # Step 1: Preprocess raw stress levels
    processed = preprocess_readings(stress_input)
    
    # Distractor variables
    temp_buffer = [x * 1.05 for x in processed if x % 2 == 0]
    scaling_factor = settings.get('scale', 1.0)
    offset_adjustment = settings.get('offset', 0)
    
    # Unused diagnostic trace
    diagnostics = []
    for idx, val in enumerate(processed):
        diag_val = {
            'index': idx,
            'raw': val,
            'flagged': 'CALIB' if val > 80 else 'OK'
        }
        diagnostics.append(diag_val)
    
    # Step 2: Apply physics-based polynomial correction
    response_curve = apply_polynomial_correction(processed)
    
    # Step 3: Aggregate using weighted harmonic mean (material yield model)
    weights = settings.get('weights', [1]*len(response_curve))
    weighted_inv_sum = 0
    weight_sum = 0
    
    for i, val in enumerate(response_curve):
        safe_val = abs(val) + 0.001  # Avoid division by zero
        weight = weights[i] if i < len(weights) else 1
        weighted_inv_sum += weight / safe_val
        weight_sum += weight
    
    if weight_sum == 0:
        harmonic_mean = 0
    else:
        harmonic_mean = weight_sum / weighted_inv_sum
    
    # Step 4: Apply configuration-based scaling and offset
    adjusted_yield = (harmonic_mean * scaling_factor) + offset_adjustment
    
    # Step 5: Round based on precision setting
    precision = settings.get('precision', 3)
    final = round(adjusted_yield, precision)
    
    # Dead code branch: simulation recovery (never triggered in this input)
    recovery_mode = settings.get('recovery', False)
    if recovery_mode and final < 0:
        fallback_data = settings.get('fallback', [])
        if fallback_data:
            final = sum(fallback_data) / len(fallback_data)
    
    return final

# Misleading initialization block
initial_readings = [123, -5, 456, 789, 1005, 234, 567]
sensor_log = "SR-789|VAL:456|STATUS:NOMINAL"

# Extract numeric parts as distraction
digits_only = ''.join([c for c in sensor_log if c.isdigit()])
token_groups = digits_only.split('789')

# Unused derived values
median_hint = len(token_groups) * 50
checksum_seed = sum(int(d) for d in digits_only[:4])

# Configuration with red herring entries
config = {
    'scale': 1.15,
    'offset': -12.5,
    'precision': 4,
    'weights': [1, 2, 1, 3],  # Last weight will be ignored due to length mismatch
    'calibration_mode': False,
    'debug_trace': [],
    'units': 'MPa',
    'version': '2.1a'
}

# Actual execution begins here
stress_levels = [80, 90, 75, 85, 95]

# Critical statement
final_yield = calculate_strain_response(stress_levels, config)

print(f"Result: {final_yield}")