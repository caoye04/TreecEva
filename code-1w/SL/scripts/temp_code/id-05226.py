import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    return sum([x * math.log(x + 1e-10) for x in data])

# Unused transformation matrix (red herring)
transform_matrix = [
    [1.2, 0.8, -0.3],
    [0.5, -1.1, 0.7],
    [-0.2, 0.9, 1.0]
]

# Misleading intermediate values
temp_offset = 42
baseline_correction = 0.003
reference_nodes = {"A": 10, "B": 20, "C": 30}

# Real input data
data_stream = [16, 9, 25, 4]

# Dead code path — never called
def legacy_calibrate(x):
    return (x >> 2) ^ 7

# Bit manipulation with red herring variables
bit_flags = 0b101010
mask_value = bit_flags & 0b1111
shifted_mask = mask_value << 3  # Unused

# Distractor set operations
active_channels = {1, 2, 3, 4, 5}
failed_channels = {6, 7}
diagnostic_log = active_channels - failed_channels  # Irrelevant

# Dictionary used for mode mapping (critical)
mode_map = {
    'A': lambda x: x ** 0.5,
    'B': lambda x: x - 10,
    'C': lambda x: x * 2
}

# Another decoy function that looks important
def validate_checksum(arr):
    total = 0
    for val in arr:
        total = (total + val) ^ 0xFF
    return total % 17 == 0

# Early exit simulation (unused)
emergency_override = False
if emergency_override:
    final_output = -999
    print(f"Result: {final_output}")
    exit()

# Core logic begins
processed = []
for val in data_stream:
    if val > 10:
        # Apply bitwise adjustment (some distraction)
        adjusted = (val ^ 0b1100) + 1
        processed.append(adjusted)
    else:
        processed.append(val)

# Intermediate transformation (partially relevant)
squared_filtered = [x**2 for x in processed if x % 2 == 0]

# Base flux derived from sum of transformed stream
base_flux = sum(squared_filtered) // len(squared_filtered)

# Decoy tuple unpacking
status_tuple = (True, 'nominal', base_flux)
is_active, system_state, _ = status_tuple

# Simulated sensor array (distractor)
sensors = [
    {'id': 'S1', 'reading': 120, 'calibrated': False},
    {'id': 'S2', 'reading': 145, 'calibrated': True}
]

# Real processing function (uses dictionary and conditional logic)
def adjust_flux(flux, modes):
    temp_result = flux
    
    # Loop through map keys in specific order (A, B, C)
    for key in ['A', 'B', 'C']:
        if key == 'A':
            temp_result = modes[key](temp_result)  # sqrt
        elif key == 'B':
            temp_result = modes[key](temp_result)  # subtract 10
        elif key == 'C':
            temp_result = modes[key](temp_result)  # multiply by 2
            break  # Early break - only A, B, C applied
    
    # Extra computation that doesn't affect result
    post_adjust = temp_result * 1.001
    return int(temp_result)  # Final truncation

# Key statement
final_flux = adjust_flux(base_flux, mode_map)

# Output result as required
print(f"Result: {final_flux}")