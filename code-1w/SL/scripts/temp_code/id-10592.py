import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, count):
    """Generate synthetic sensor signals with noise (irrelevant for final result)"""
    return [baseline + math.sin(i) * 0.1 for i in range(count)]


def parse_timestamps(log_entries):
    """Extract and format timestamps (distractor function - not used in main path)"""
    parsed = []
    for entry in log_entries:
        parts = entry.split(' | ')
        time_str = parts[0].split(': ')[1]
        parsed.append(time_str.replace('-', '').replace(':', ''))
    return parsed

# Irrelevant global constants
data_buffer_limit = 512
max_retries = 3
voltage_cap = 3.3
calibration_factor = 0.987

# Core data used in computation
raw_readings = [18, 24, 36, 42, 54, 72, 84, 96]
scaling_factors = {'A': 1.5, 'B': 2.0, 'C': 0.75}

# Misleading preprocessing chain
temp_cache = {}
for idx, val in enumerate(raw_readings):
    temp_cache[f'idx_{idx}'] = val ** 2 + 1 if val % 2 == 0 else val * 3

# Real processing begins here
processed_data = [x for x in raw_readings if x > 30]  # Filter relevant readings

# Decoy statistical calculations
mean_val = sum(raw_readings) / len(raw_readings)
variance_proxy = sum((x - mean_val) ** 2 for x in raw_readings)
entropy_approx = math.log(len(raw_readings))

# Another red herring: unused transformation matrix
diag_matrix = [
    [1, 0, 0],
    [0, scaling_factors['A'], 0],
    [0, 0, scaling_factors['C']]
]

# Threshold map actually used in final computation
def build_threshold_map(data_list):
    base_t = sum(data_list) / len(data_list)
    return {
        'low': base_t * 0.6,
        'optimal': base_t * 0.85,
        'high': base_t * 1.2
    }

threshold_map = build_threshold_map(processed_data)

# Auxiliary function that looks important but is never called
def validate_calibration(sequence, factor):
    running = 0
    for i, v in enumerate(sequence):
        running += v * factor / (i + 1)
    return running < 100

# Key function contributing to final answer
def analyze_readings(readings, thresholds):
    count_in_range = 0
    penalty = 0
    
    for reading in readings:
        # Complex conditional logic with side tracking
        if thresholds['low'] <= reading <= thresholds['optimal']:
            count_in_range += 1
        elif reading > thresholds['high']:
            # Exponential decay penalty
            excess = reading - thresholds['high']
            penalty += int(math.ceil(excess ** 1.5))
    
    # Final score combines positive and negative factors
    stability_index = len(readings) * 10 + count_in_range * 5 - penalty
    
    # Secondary adjustment based on bit patterns (actual use of bitwise logic)
    adjusted = stability_index
    for r in readings:
        if r & 1:  # odd numbers reduce score via XOR interference
            adjusted ^= 7
        else:
            adjusted += (r & 15)  # add lower nibble of even values

    return adjusted

# Unused legacy function (dead code path)
def legacy_diagnostic(arr):
    total = 0
    for x in arr:
        total += x >> 2
    return total * 2

# Simulated logs to feed into distractor function
system_logs = [
    "Time: 2023-10-05T12:30:45 | Status: OK",
    "Time: 2023-10-05T12:31:10 | Status: WARNING"
]

# Extract timestamps (useless operation)
_ = parse_timestamps(system_logs)

# Generate unused signal data
_ = generate_signals(1.0, 100)

# Final computation - this is the critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")