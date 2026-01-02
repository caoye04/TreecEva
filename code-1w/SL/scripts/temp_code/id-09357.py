import math

def preprocess_input(raw_stream):
    # Irrelevant transformation chain (distractor)
    temp_buffer = [x ** 0.5 for x in raw_stream if x > 10]
    normalized = [round(x / sum(temp_buffer), 4) for x in temp_buffer]
    return [x * 100 for x in normalized]

# Unused function - red herring
def validate_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) % 256
    return checksum == 42

# Decoy data structure
system_states = {
    'idle': {'mode': 7, 'flag': False},
    'active': {'mode': 19, 'flag': True},
    'standby': {'mode': 3, 'flag': False}
}

# Real signal processing components
primary_weights = [1.5, 2.0, -1.0, 0.5]
secondary_mask = [1 if i % 2 == 0 else 0 for i in range(8)]

# Simulated sensor readings with embedded logic
raw_sensor_data = [32, 15, 45, 28, 60, 12, 38, 51]

# Misleading intermediate computation (dead path)
calibration_offset = 0
for val in raw_sensor_data:
    if val < 20:
        calibration_offset += math.log(val)

# Actual relevant preprocessing
filtered_data = [x for x in raw_sensor_data if x % 3 != 0]  # Remove multiples of 3
temp_scaled = [x * 1.1 for x in filtered_data]

# String-based mode selection (required python string method)
operation_mode = 'diagnostics_active'
if operation_mode.startswith('debug'):
    temp_scaled = [x * 0.9 for x in temp_scaled]
elif 'active' in operation_mode.split('_'):
    temp_scaled = [x * 1.05 for x in temp_scaled]  # Apply 5% boost

processed_data = [int(x) for x in temp_scaled]  # Convert to integers

# Core analysis logic
mask_threshold = 18
shift_register = 0

for val in processed_data:
    if val > mask_threshold:
        shift_register += (val & 7)  # Bitwise AND with 7
    else:
        shift_register -= (val % 4)

# Conditional branching with modular arithmetic
cycle_index = len(processed_data) % 6
amplitude_factor = 0
if cycle_index in [0, 2, 4]:
    amptide_factor = 3
elif cycle_index in [1, 3, 5]:
    amplitude_factor = 2
else:
    amplitude_factor = 1

# Final diagnostic calculation
base_metric = shift_register * amplitude_factor

# Secondary influence: count uppercase letters in mode string (string method distractor)
dummy_score = sum(1 for c in operation_mode if c.isupper())

# Real final step
final_diagnostic = base_metric + (cycle_index ** 2)

# Output required result
print(f"Result: {final_diagnostic}")