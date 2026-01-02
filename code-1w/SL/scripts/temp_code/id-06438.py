import math

# Simulated telemetry data from distributed sensors
telemetry_stream = [14, 28, 42, 56, 70, 84, 98, 112]
offset_correction = 3
scaling_factor = 1.75
decoy_buffer = [x ** 2 for x in range(15)]  # Unused computation (red herring)

# Data structure initialization
log_entries = {}
for i, val in enumerate(telemetry_stream):
    key = f'sensor_{(i * 7) % 11}'  # Non-sequential key mapping
    corrected = (val + offset_correction) * scaling_factor
    log_entries[key] = int(corrected) if i % 2 == 0 else round(corrected, 2)

# Extraneous dictionary transformation (distractor)
power_map = {k: v ** 2 for k, v in log_entries.items() if isinstance(v, int)}

# System state with health flags and thresholds
system_state = {
    'nodes_active': 7,
    'thresholds': [12.5, 25.0, 37.5],
    'health_flag': True,
    'debug_mode': False,
    'cache_snapshot': {'a': 1, 'b': 2, 'c': 3}  # Dead data (unused)
}

# Irrelevant recursive function (decoy)
def calculate_entropy(n):
    if n <= 1:
        return 1
    return n * math.log(n) + calculate_entropy(n - 1)

entropy_value = calculate_entropy(5)  # Computed but not used

# Real processing begins here — core logic mixed with distractions
rolling_window = [telemetry_stream[i:i+3] for i in range(len(telemetry_stream)-2)]
filtered_sets = [window for window in rolling_window if sum(window) % 7 == 0]

# Bit manipulation for checksum simulation
checksum = 0
for val in telemetry_stream[::2]:
    checksum ^= (val << 2) | (val >> 1)

# Core diagnostic processor
status_codes = []
for key, value in log_entries.items():
    if isinstance(value, int):
        status_codes.append(value % 13)
    else:
        status_codes.append(int(value // 2.5))

# Conditional override based on system health
if system_state['health_flag'] and system_state['nodes_active'] > 5:
    adjusted = [code * 2 for code in status_codes if code > 3]
    processed = sum(adjusted) // len(adjusted) if adjusted else 0
else:
    processed = sum(status_codes)

# Secondary validation using slicing and set operations
validation_slice = sorted(set(status_codes[1::2]))  # Every second element, unique only
quorum_check = len(validation_slice) >= 3 and validation_slice[2] > 5

# Final aggregation with modular arithmetic
aggregation_key = (processed + len(validation_slice)) % 17

# Misleading intermediate that looks important
consensus_score = (aggregation_key * 37) % 1000  # Looks critical, isn't

# Actual final computation path
def process_metrics(entries, state):
    base = sum(v if isinstance(v, int) else int(v) for v in entries.values())
    modifier = state['nodes_active'] * 0.6
    temp_result = base * modifier

    # Apply bit-shift derived factor
    shift_factor = (checksum & 0xFF)  # Use lower byte of checksum
    extended = temp_result * (shift_factor / 100)

    # Final adjustment via modular constraint
    if quorum_check:
        final = int(extended % 98765)
    else:
        final = int(extended % 54321)
    
    return final

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Result: {final_diagnostic}")