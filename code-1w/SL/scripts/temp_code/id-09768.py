import math

# Simulated sensor fusion system for environmental anomaly detection
def collect_readings(base: float, noise_factor: float) -> set:
    readings = set()
    for i in range(1, 8):
        raw = (base * i) + noise_factor * math.sin(i)
        quantized = int(round(raw))
        readings.add(quantized)
    # Distractor: irrelevant transformation
    temp_data = [x ** 0.5 for x in readings if x > 0]
    temp_data.reverse()
    return readings

def generate_reference() -> set:
    ref_set = set()
    for i in range(2, 20, 3):
        ref_set.add(i * i % 17)
    # Dead code path - never used later
    if len(ref_set) > 10:
        ref_set.discard(0)
    return ref_set

def filter_outliers(data: set, limit: int) -> set:
    cleaned = set()
    outlier_count = 0  # Tracking but not used
    for val in data:
        if abs(val) < limit:
            cleaned.add(val)
        else:
            outlier_count += 1
    # Distractor computation
    magnitude_score = sum([abs(x) for x in cleaned]) / (len(cleaned) + 1)
    normalized_score = round(magnitude_score, 3)
    return cleaned

def merge_diagnostic(primary: set, secondary: set) -> set:
    # Fusion using symmetric difference and intersection mix
    intersect = primary.intersection(secondary)
    diff = primary.symmetric_difference(secondary)
    fused = set()
    for x in intersect:
        fused.add(x * 2)
    for x in diff:
        if x % 3 == 0:
            fused.add(x // 3)
    # Red herring: unused complex structure
    history_log = [{'event': 'merge_step', 'values': list(fused)}, {'event': 'backup', 'values': list(diff)}]
    return fused

def recursive_transform(seq: set, depth: int) -> int:
    if depth <= 0 or len(seq) == 0:
        return sum(seq)
    transformed = set()
    for item in seq:
        if item > 0:
            transformed.add(int(math.sqrt(item) + 1))
        elif item < 0:
            transformed.add(item + 5)
        else:
            transformed.add(7)
    # Decoy operation with no effect
    [x * x for x in transformed if x < 0]  
    return recursive_transform(transformed, depth - 1)

def analyze_signal(pattern: set, criteria: set) -> int:
    # Core logic hidden among distractions
    base_score = 0
    trigger_flags = 0
    for x in pattern:
        if x in criteria:
            base_score += x * 3
        elif x > 10:
            base_score += x // 4
        else:
            base_score -= x
    # Critical red herring: looks important but unused
    compliance_matrix = [[(i + j) % 5 for j in range(5)] for i in range(5)]
    validation_trace = []
    for row in compliance_matrix:
        validation_trace.append(sum(row))
    adjustment_factor = len(validation_trace) % 9
    # Actual answer depends only on this final expression
    final_diagnostic = base_score + adjustment_factor
    return final_diagnostic

# Irrelevant initialization - distractor block
initial_buffer = [0] * 15
for idx in range(len(initial_buffer)):
    initial_buffer[idx] = (idx * 7) % 13

# Sensor input simulation (meaningful input chain)
core_reading = collect_readings(3.7, 1.4)
reference_pool = generate_reference()
cleaned_signal = filter_outliers(core_reading, 25)
composite_pattern = merge_diagnostic(cleaned_signal, reference_pool)

# Threshold definition with misleading expansion
threshold_set = {1, 3, 5, 7, 9, 11}
temp_thresholds = [x * 2 + 1 for x in range(5)]
# Unused expansion
expanded_zones = set(temp_thresholds)
expanded_zones.update({x + 10 for x in expanded_zones})

# Recursive processing decoy - appears significant but not tied to output
recursion_test = recursive_transform(composite_pattern, 2)
recursion_test = recursive_transform(composite_pattern, 1)  # Re-run for confusion

# Key execution point - this determines the actual answer
final_diagnostic = analyze_signal(composite_pattern, threshold_set)

# Output must be printed exactly like this
print(f"Result: {final_diagnostic}")