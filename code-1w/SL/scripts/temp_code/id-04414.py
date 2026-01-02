import itertools

# Simulated sensor data stream with noise and metadata
raw_signals = [5, -3, 8, 12, -1, 0, 7, 4]
noise_floor = 0.5
calibration_offset = sum([x for x in raw_signals if x > 0]) // len(raw_signals)

# Irrelevant diagnostic flags (distractors)
system_status = {'temp': 'OK', 'pressure': 'HIGH', 'flow': 'STABLE'}
device_mode = 'CALIBRATION'
heartbeat_interval = 123

# Data normalization (some irrelevant transformations mixed in)
normalized = [x + calibration_offset for x in raw_signals]
filtered = [x for x in normalized if abs(x) > noise_floor]

# Dummy transformation chain (only one path is relevant)
def apply_filter(data, mode='smooth'):
    if mode == 'smooth':
        return [sum(data[i:i+2]) / 2 for i in range(len(data)-1)]
    elif mode == 'edge':
        return [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    else:
        return data  # unreachable default

# Unused recursive function (dead code - red herring)
def compute_depth(value, acc=0):
    if value <= 1:
        return acc
    return compute_depth(value // 2, acc + 1)

# Real processing begins here — slicing and shifting
windowed = filtered[1:-1]  # Remove edges
shifted = [x << 1 for x in windowed]  # Bit shift doubling

# Apply two different filters but only use one later
smooth_path = apply_filter(shifted, 'smooth')
edge_path = apply_filter(shifted, 'edge')  # Computed but unused

# Decoy statistical analysis (irrelevant computations)
mean_value = sum(shifted) / len(shifted)
variance = sum((x - mean_value) ** 2 for x in shifted) / len(shifted)
entropy_approx = len([x for x in shifted if x % 2 == 0])  # Not actually used

# Core logic disguised among distractors: transform using itertools.cycle
reference_cycle = itertools.cycle([1, -1])
oscillated = [a + next(reference_cycle) for a in smooth_path]

# Further transformation via dictionary mapping (only even indices matter)
index_map = {i: oscillated[i] * 2 for i in range(len(oscillated))}
indexed_result = [index_map[i] for i in range(0, len(oscillated), 2)]  # Use only even keys

# Another decoy structure: unused dictionary aggregation
aggregated_stats = {
    'total_peaks': len([x for x in edge_path if x > 5]),
    'baseline_drift': filtered[0] - filtered[-1],
    'pulse_count': heartbeat_interval % 10
}

# Critical function: analyzes transformed pattern
def analyze_pattern(data):
    if not data:
        return -999
    
    # Real answer derived from min and max interaction
    peak = max(data)
    trough = min(data)
    spread = peak - trough
    
    # Secondary effect: count how many crossed midpoint
    midpoint = (peak + trough) / 2
    cross_count = sum(1 for x in data if x >= midpoint)
    
    # Final deterministic computation (others are distractions)
    return int(spread * cross_count // 1.5)

# Transform data through multiple layers before final analysis
temp_correction = [x + (1 if i % 3 == 0 else 0) for i, x in enumerate(indexed_result)]
transformed_data = [x for x in temp_correction if x % 2 == 1]  # Keep only odds

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")