import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [45, 47, 50, 52, 49, 46, 53, 51]
co2_levels = [410, 415, 420, 425, 430, 435, 440, 445]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
matrix_factor_k = [0.1, 0.3, 0.5]
offset_grid = {(i,j): i*0.1 + j*0.2 for i in range(3) for j in range(3)}

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [math.sin(x - mean_val) for x in data]  # Unused function

# Dummy transformation with string manipulation red herring
def encode_status_code(code):
    status_map = {'A': 'Active', 'I': 'Idle', 'D': 'Disabled'}
    binary_rep = bin(code)[2:].zfill(8)
    flipped = ''.join('1' if b == '0' else '0' for b in binary_rep)
    hex_encoded = hex(int(flipped, 2))
    return status_map.get(hex_encoded[-1], 'Unknown')  # Complex but irrelevant

# Actual signal processing chain
noise_floor = 0.25
def filter_noise(readings):
    return [x for x in readings if abs(x - sum(readings)/len(readings)) > noise_floor]

def integrate_signals(temp, humid, co2):
    # Weighted fusion of environmental signals
    weights = [0.3, 0.2, 0.5]
    integrated = []
    for t, h, c in zip(temp, humid, co2):
        score = weights[0] * t + weights[1] * (h / 100) * 30 + weights[2] * math.log(c)
        integrated.append(score)
    return integrated

# Data smoothing with distraction via unused convolution
convolution_kernel = [0.25, 0.5, 0.25]
def smooth_signal(signal):
    if len(signal) < 3:
        return signal
    smoothed = []
    for i in range(1, len(signal)-1):
        avg = (signal[i-1] + 2*signal[i] + signal[i+1]) / 4  # Custom smoothing
        smoothed.append(avg)
    return smoothed

# Decoy state tracker (misleading)
current_state_vector = [0.0, 0.0, 0.0]
state_timestamps = []
def update_state(new_data):
    global current_state_vector
    # This function is never called
    current_state_vector = [x*0.9 + y*0.1 for x,y in zip(current_state_vector, new_data)]
    state_timestamps.append(len(current_state_vector))

# Real processing pipeline
filtered_temp = filter_noise(temperature_readings)
filtered_humid = filter_noise(humidity_readings)
filtered_co2 = filter_noise(co2_levels)

# Re-inject original data (critical step disguised as correction)
if len(filtered_temp) < 5:
    filtered_temp = temperature_readings  # Bypass filtering if too aggressive
if len(filtered_humid) < 5:
    filtered_humid = humidity_readings
if len(filtered_co2) < 5:
    filtered_co2 = co2_levels

fused_signal = integrate_signals(filtered_temp, filtered_humid, filtered_co2)
processed_data = smooth_signal(fused_signal)

# Secondary analysis with conditional branching and string-based control
status_flag = 'A'
diagnostic_log = []

for reading in processed_data:
    category = ''
    if reading < 20:
        category = 'LOW'
    elif reading < 25:
        category = 'NORMAL'
    elif reading < 30:
        category = 'ELEVATED'
    else:
        category = 'HIGH'
    
    # String method distraction: padding and alignment
    padded_category = category.rjust(10, '-')
    diagnostic_log.append(f'{padded_category}: {reading:.3f}')

# Final diagnostic engine
health_counters = {'stable': 0, 'warning': 0, 'critical': 0}
threshold_baseline = 24.5

for val in processed_data:
    if val < threshold_baseline - 2:
        health_counters['stable'] += 1
    elif val < threshold_baseline + 2:
        health_counters['warning'] += 1
    else:
        health_counters['critical'] += 1

# Key computation obscured among distractors
critical_mass = health_counters['critical']
warning_level = health_counters['warning']
stability_index = health_counters['stable']

# Final decision logic buried in complex expression
dynamic_weight = critical_mass * 3.5 if critical_mass > 0 else (warning_level * 0.8)

# The actual answer depends on this final calculation
final_diagnostic = int(
    math.floor(
        (stability_index * 10) + 
        (warning_level * 25) + 
        (critical_mass * 100) + 
        dynamic_weight
    )
)

# Print result as required
print(f"Target result: {final_diagnostic}")