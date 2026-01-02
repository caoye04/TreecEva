import math

# Simulated sensor fusion system for environmental monitoring

def collect_readings():
    raw_values = [127, 255, 192, 64, 32, 160, 80]
    scale_factor = 0.75
    adjusted = [val * scale_factor for val in raw_values]
    return adjusted

# Irrelevant calibration function (dead code path)
def calibrate_sensors(offsets):
    base_ref = 42
    for i in range(len(offsets)):
        offsets[i] += base_ref % 7
    return sorted(offsets, reverse=True)

# Signal processing pipeline
def filter_noise(data, limit=100):
    filtered = []
    noise_floor = 50 * 0.8
    for x in data:
        if x > noise_floor and x < limit:
            filtered.append(int(x))
    return filtered

# Data transformation using set operations
def create_signature(profile):
    even_components = {x for x in profile if x % 2 == 0}
    multiples_of_16 = {x for x in profile if x % 16 == 0}
    signature = even_components.intersection(multiples_of_16)
    return signature

# Recursive frequency analysis (actual usage)
def count_frequency(values, index=0, acc=None):
    if acc is None:
        acc = {}
    if index >= len(values):
        return acc
    key = values[index]
    acc[key] = acc.get(key, 0) + 1
    return count_frequency(values, index + 1, acc)

# Main analysis engine
def analyze_signal(dataset, constraints):
    freq_map = count_frequency(dataset)
    temp_result = []
    for k, v in freq_map.items():
        if k in constraints:
            temp_result.append(k * v)
    aggregate = sum(temp_result)
    adjustment = len(constraints) // 2
    return aggregate - adjustment

# Decoy diagnostic function (misleading intermediate result)
def compute_health_score(trace):
    score = 0
    for item in trace:
        if item > 90:
            score += 10
        elif item > 50:
            score += 5
    return score * 1.5  # Not used in final computation

# Secondary irrelevant transformation
intermediate_buffer = ['A', 'B', 'C']
debug_mode = False
if debug_mode:
    print('Debug: Buffer initialized')

# Core execution flow
readings = collect_readings()
processed_data = filter_noise(readings, limit=150)

# Create constraint set via set operations
baseline = [16, 32, 64, 128]
system_bounds = {x * 2 for x in baseline}
threshold_set = create_signature(processed_data).union({32, 64})  # Key constraint set

# Phantom operation with no downstream effect
temporary_analysis = compute_health_score(processed_data)
dropped_segment = processed_data[::2]

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_set)
print(f"Result: {final_diagnostic}")