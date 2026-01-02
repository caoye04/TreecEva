import itertools

def analyze_sensor_array(raw_readings, threshold, mode='aggregate'):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 0.98 + 3 for x in raw_readings]
    outliers = [i for i, v in enumerate(normalized) if v > 95]
    masked_data = [v for i, v in enumerate(normalized) if i not in outliers]

    # Core logic disguised among red herrings
    shifted = [(v * 2) % 87 for v in masked_data]
    paired = list(zip(shifted[:-1], shifted[1:]))
    diffs = [abs(a - b) for a, b in paired]

    # Decoy transformation (unused later)
    transformed = [round((x ** 0.5) * 1.2, 2) for x in diffs]

    # Actual relevant path begins here
    filtered_data = [x for x in diffs if x > threshold]
    cumulative = 0
    for idx, val in enumerate(filtered_data):
        if idx % 2 == 0:
            cumulative += val * (idx + 1)
        else:
            cumulative -= val // 2

    return cumulative


def validate_checksum(sequence):
    # Unused function - red herring
    return sum(x ^ (x << 1) for x in sequence) % 100


def process_readings(data, factor):
    # Real processing with modular arithmetic and bit manipulation
    base_value = sum(data) % 10000
    temp = 0
    for i, x in enumerate(data):
        temp ^= (x * factor + i) % 127  # Bitwise mix with index
    
    # Complex but deterministic transformation
    extended = list(itertools.accumulate(data, lambda a, b: (a + b * 2) % 500))
    mid_stage = sum(extended[i] for i in range(len(extended)) if i % 3 == 1)

    # Final composition
    result = (base_value + temp * 3) ^ mid_stage
    adjustment = len(data) ** 2
    if result < 0:
        result -= adjustment
    else:
        result += adjustment

    return result

# Simulated sensor input (real data source)
raw_input = [42, 78, 88, 91, 65, 72, 83, 76, 69, 81, 94, 77, 85]

# Irrelevant transformations (dead paths)
calibration_map = {k: v**2 for k, v in enumerate([2, 3, 1, 4])}
dummy_sequence = [x | (x >> 2) for x in raw_input]

# Key computation chain
initial_diagnostic = analyze_sensor_array(raw_input, threshold=15, mode='aggregate')

# Secondary irrelevant check
status_flags = ['OK' if x > 50 else 'LOW' for x in raw_input]

# Core assignment with distractors around
baseline = 412
reference_log = [f"Entry_{i}: {v}" for i, v in enumerate(raw_input)]
calibration_factor = 7

# Critical execution point
final_diagnostic = process_readings(filtered_data=[initial_diagnostic % 50 + i for i in range(8)], calibration_factor=calibration_factor)

# Dead code path - misleading
if final_diagnostic > 1000:
    final_diagnostic = final_diagnostic & 0xFFFF
else:
    final_diagnostic = final_diagnostic | 0xFF

# Output required result
print(f"Target result: {final_diagnostic}")