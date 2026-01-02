import math

# Irrelevant utility function (dead code)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Misleading data structure with decoy entries
decoys = {
    'temp_offset': -7.2,
    'calibration_factor': 0.88,
    'noise_floor': 42,
    'useless_counter': 117
}

# Simulated sensor readings (some relevant, some not)
sensor_data = [
    {'type': 'pressure', 'val': '1013.25', 'active': True},
    {'type': 'humidity', 'val': '68.4', 'active': False},
    {'type': 'temperature', 'val': '22.1', 'active': True},
    {'type': 'vibration', 'val': '0.0031', 'active': True}
]

# Configuration with red herring fields
config = {
    'threshold': 50,
    'mode': 'diagnostic',
    'debug_flag': False,
    'legacy_mode': True,
    'max_iterations': 999,  # unused
    'scale_factor': 2.5
}

# String parsing using string methods
parsed_values = []
for entry in sensor_data:
    if entry['active']:
        try:
            # Extract numeric value via string.strip and convert
            clean_val = float(entry['val'].strip())
            parsed_values.append((entry['type'], clean_val))
        except ValueError:
            continue

# Transform data using lambda and list operations
transform_fn = lambda t: (t[0], round(t[1] * config['scale_factor'], 4)) if 'pressure' not in t[0] else (t[0], round(t[1] / 100, 4))
transformed_data = list(map(transform_fn, parsed_values))

# Decoy computation path (never used)
temporary_accum = 0
for i in range(10):
    temporary_accum += i ** 2
    if temporary_accum > 100:
        break

# Real processing function
def process_metrics(data, cfg):
    result = 0.0
    pressure_val = None
    temperature_offset = cfg.get('threshold') * 0.01

    # Nested logic with multiple conditions
    for typ, val in data:
        if typ == 'pressure':
            pressure_val = val * 10  # scale up for metric
        elif typ == 'temperature':
            # Apply nonlinear correction
            corrected = math.log(val + 273.15)  # Kelvin conversion
            result += corrected * 10
        elif typ == 'vibration':
            # Bit manipulation as part of signal weighting
            magnitude = int(val * 10000)
            weighted = magnitude ^ 0b1101  # XOR mask
            weighted = (weighted << 1) | (weighted >> 3)  # shift mix
            result += weighted / 100

    # Final integration step
    if pressure_val is not None:
        result += pressure_val

    # Integer division and rounding interplay
    result = math.floor(result * 2) // 1  # floor then integer divide

    # Final adjustment based on config mode
    if cfg['mode'] == 'diagnostic':
        result = round(result + temperature_offset, 4)

    return result

# Unused but plausible-looking diagnostic chain
def fake_pipeline(seq):
    acc = 0
    for x in seq:
        if isinstance(x, tuple) and len(x) == 2:
            acc += hash(x[0]) % 7
    return acc

# Key execution point
final_diagnostic = process_metrics(transformed_data, config)

# Print target result
print(f"Target result: {final_diagnostic}")