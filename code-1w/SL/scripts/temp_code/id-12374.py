def normalize_input(data_str):
    # Irrelevant string processing function (red herring)
    cleaned = data_str.strip().lower()
    tokens = cleaned.split(',')
    filtered = [t for t in tokens if t.isalpha()]
    return ''.join(filtered)

# Misleading constants and variables
efficiency_map = {'A': 0.95, 'B': 0.87, 'C': 0.72}
dummy_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
scaling_factor = 1.04
offset_correction = -0.02

# Distractor list used in dead code path
event_log = ['start', 'calibrate', 'idle', 'reset']
for event in event_log:
    if len(event) > 6:
        event_log.remove(event)  # Dead logic due to modification during iteration

# Real computation begins here
base_temperature = 273.15
heating_rate = 3.45
cooling_rate = 1.92
mode = 'high'

# Simulated sensor readings (some are decoys)
sensor_a = 120.5
sensor_b = 98.7
sensor_c = 145.2  # Not actually used

raw_average = (sensor_a + sensor_b) / 2
adjusted_avg = raw_average * 1.08  # Minor adjustment

# Initial thermal capacity derived from adjusted average
target_power = int(adjusted_avg)
thermal_capacity = int(base_temperature + target_power)

# Bit manipulation decoy (unused)
flag_register = 0b10101100
mask = 0b11110000
masked_flag = flag_register & mask

# Unused conditional branch (distractor)
if masked_flag > 100:
    scaling_factor *= 1.1
    dummy_weights.append(1.1)

# Linear search in irrelevant dataset (dead code path)
search_space = list(range(50, 150, 7))
found_index = -1
for i in range(len(search_space)):
    if search_space[i] == 80:
        found_index = i
        break

# Main logic: function that actually affects the answer
def adjust_thermal(value, mode):
    if mode == 'high':
        value += int(heating_rate * 2)
    elif mode == 'low':
        value -= int(cooling_rate * 3)
    else:
        value = int(value * 0.9)
    
    # String-based switch using irrelevant method (but syntactically valid)
    mode_tag = 'HIGH_MODE_ACTIVE'
    if mode_tag.lower().startswith('high'):
        value += 5
    return value

# Critical statement
thermal_capacity = adjust_thermal(thermal_capacity, mode)

# Additional distractor: unused recursive function
def calculate_depth(n):
    if n <= 1:
        return 1
    return n * calculate_depth(n - 2)

# Final output
Result: {thermal_capacity}