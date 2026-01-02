import math

# Simulated sensor array diagnostics with interference logic
def collect_readings(samples):
    readings = []
    for s in samples:
        if s % 3 == 0 and s > 0:
            readings.append(s ** 0.5)
    return readings

# Irrelevant signal smoothing (dead-end function)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed  # Never used

# Auxiliary checksum (misleading intermediate)
def compute_legacy_checksum(arr):
    checksum = 0
    for val in arr:
        checksum += (val * 7) % 13
    return checksum * 2  # Computed but not part of final result

# Core pattern analyzer
def generate_logic_mask(size):
    mask = []
    for i in range(size):
        if i % 4 == 0:
            mask.append(1)
        elif i % 3 == 0:
            mask.append(-1)
        else:
            mask.append(0)
    return mask

def evaluate_thresholds(values, threshold=5.0):
    return [1 if v > threshold else 0 for v in values]

# Unused recursive variant (red herring)
def recursive_scan(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_scan(arr, idx + 2)  # Not invoked

# Main analysis engine
def analyze_pattern(grid, flags):
    aggregate = 0
    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            # Only specific flagged positions contribute
            if flags[row_idx][col_idx]:
                transformed = val * (row_idx + 1) - (col_idx * 0.5)
                if transformed > 0:
                    aggregate += int(math.floor(transformed))
    return aggregate

# --- Simulation Setup ---
raw_samples = [9, -3, 12, 6, 15, 21, 8, 18]
diagnostic_readings = collect_readings(raw_samples)  # [3.0, 3.464..., 2.449..., 3.872..., 4.582..., 4.242...]

# Misleading preprocessing chain
legacy_checksum = compute_legacy_checksum(raw_samples)  # Distractor: 142
filtered_readings = evaluate_thresholds(diagnostic_readings, 3.5)  # [False, False, False, True, True, True]

# Construct logic grid (core data structure)
logic_grid = []
for i in range(4):
    row = []
    for j in range(4):
        base = (i * 4) + j + 1
        noise = math.sin(base) if base % 2 else math.cos(base)
        clean_val = base * diagnostic_readings[i % len(diagnostic_readings)] if i < len(diagnostic_readings) else 0
        final_val = abs(clean_val + 10 * noise)
        row.append(round(final_val, 2))
    logic_grid.append(row)

# Trigger map generation (conditional expression usage)
mask_sequence = generate_logic_mask(4)
triggers = []
for i in range(4):
    trigger_row = [
        (i == j and mask_sequence[i] != 0) or (j == 3 and diagnostic_readings[i % len(diagnostic_readings)] > 4.0) 
        for j in range(4)
    ]
    triggers.append(trigger_row)

# Critical execution point
final_diagnostic = analyze_pattern(logic_grid, triggers)

print(f"Result: {final_diagnostic}")