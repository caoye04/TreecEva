from itertools import groupby, chain
import math

# Simulated sensor readings from thermal array (irrelevant data)
sensor_data = [23.4, 24.1, 25.0, 24.8, 26.2, 25.9, 27.1, 26.8, 25.3, 24.7]

# Irrelevant transformation: normalize to z-score (dead path)
def z_score_normalize(data):
    mean = sum(data) / len(data)
    stddev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [(x - mean) / stddev for x in data]

normalized_readings = z_score_normalize(sensor_data)  # unused later

# Decoy function: appears relevant but not used
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Core system parameters (mixed with decoys)
system_flags = [True, False, True, True]
baseline_offset = 0.87
reference_nodes = ['A', 'B', 'C', 'D', 'E']

# Efficiency trace log – this is the actual input
efficiency_log = [0.92, 0.88, 0.95, 0.83, 0.91, 0.85, 0.93]

# Red herring: complex grouping that computes nothing useful
def analyze_pattern(seq):
    grouped = [list(g) for k, g in groupby(seq, key=lambda x: round(x, 1))]
    flat = list(chain.from_iterable(grouped))
    return len([g for g in grouped if len(g) > 1])

pattern_score = analyze_pattern(efficiency_log)  # computed but unused

# Actual critical computation path
def calculate_thermal_properties(log):
    # Step 1: filter only high-efficiency cycles
    filtered = [x for x in log if x > 0.89]
    
    # Step 2: apply non-linear correction factor
    corrected = [math.log(x) * 100 for x in filtered]
    
    # Step 3: map to hypothetical thermal units via lambda
    mapper = lambda val: val ** 1.1
    mapped = list(map(mapper, corrected))
    
    # Step 4: aggregate using weighted contribution
    weights = [1.0, 1.2, 1.1, 1.3, 1.05, 1.15, 0.95][:len(mapped)]
    weighted = [mapped[i] * weights[i] for i in range(len(mapped))]
    
    # Step 5: apply diminishing returns
    processed = [w / (1 + i*0.05) for i, w in enumerate(weighted)]
    
    # Step 6: cumulative capacity calculation
    cumulative = 0
    for val in processed:
        cumulative += val
        if cumulative > 1000:  # artificial cap (never reached)
            cumulative *= 0.95
    
    # Step 7: adjust with baseline offset (unused in red herring above)
    final = cumulative + (baseline_offset * 100)
    
    return final

# Unused alternative algorithm (dead code path)
if False:
    def alt_calc(seq):
        rev = seq[::-1]
        return sum(rev[i] * (i+1) for i in range(len(rev)))

# Critical execution point
target_node = reference_nodes[2]  # irrelevant
status_flag = system_flags[0] and not system_flags[1]  # misleading intermediate

# Key assignment – the answer depends on this
temperature_snapshot = sensor_data[2]
efficiency_peak = max(efficiency_log)
thermal_capacity = calculate_thermal_properties(efficiency_log)

# Output the target variable
print(f"Result: {thermal_capacity}")