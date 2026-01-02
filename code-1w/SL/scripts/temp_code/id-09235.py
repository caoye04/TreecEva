import math

# Simulated sensor data with noise and redundant metrics
data_stream = [18, 23, 15, 47, 29, 33, 41, 12, 8, 55, 62, 5, 38, 44]
noise_floor = 7
amplification_factor = 2.5

# Irrelevant transformation - red herring
transformed = [math.sin(x / 10) * amplification_factor for x in data_stream]
smoothed = [sum(data_stream[i:i+3]) // 3 for i in range(len(data_stream) - 2)]

# Real preprocessing: filter valid readings above noise floor
effective_readings = [x for x in data_stream if x > noise_floor]

# Decoy statistical analysis (dead code path)
mean_val = sum(effective_readings) / len(effective_readings)
median_val = sorted(effective_readings)[len(effective_readings)//2]
variance = sum((x - mean_val)**2 for x in effective_readings) / len(effective_readings)

# Hash map of thresholds (some irrelevant)
thresholds = {
    'critical': 50,
    'warning': 30,
    'info': 20,
    'debug': 10,
    'trace': 5  # Unused
}

# Misleading multi-step calculation chain
baseline_offset = 10
weighting_curve = []
for i, val in enumerate(effective_readings):
    if val >= thresholds['critical']:
        weight = 3.0
    elif val >= thresholds['warning']:
        weight = 1.8 + (i % 3) * 0.1  # Introduce subtle variation
    elif val >= thresholds['info']:
        weight = 1.2
    else:
        weight = 0.5
    weighting_curve.append(weight)

# Distractor: complex bit manipulation with no impact
bitmask = 0b101010
masked_values = [x ^ bitmask & 0b111 for x in data_stream]
shifted_sum = sum((x << 2) >> 1 for x in masked_values) % 1000

# Unused recursive function - decoy abstraction layer
def analyze_recursively(arr, depth=0):
    if depth >= 3 or len(arr) < 2:
        return depth
    return analyze_recursively(arr[::2], depth + 1)

# Spurious dictionary accumulation
stats_summary = {}
for key in thresholds:
    count = sum(1 for x in effective_readings if x > thresholds[key])
    stats_summary[key] = count

# Conditional slicing based on dynamic index
start_idx = len(effective_readings) // 4
end_idx = len(effective_readings) - (len(effective_readings) // 5)
working_slice = effective_readings[start_idx:end_idx]

# Secondary processing: compute weighted contributions
weighted_contributions = []
for i, val in enumerate(working_slice):
    normalized = (val - baseline_offset) / 10.0
    exponentiated = normalized ** weighting_curve[start_idx + i]
    weighted_contributions.append(exponentiated)

# Tertiary transformation: logarithmic scaling only on positive values
scaled_inputs = []
for wc in weighted_contributions:
    if wc > 0:
        scaled_inputs.append(math.log(wc + 1) * 100)
    else:
        scaled_inputs.append(0)

# Final aggregation through multiple stages
aggregation_chain = scaled_inputs.copy()
while len(aggregation_chain) > 1:
    new_chain = []
    for i in range(len(aggregation_chain) - 1):
        combined = (aggregation_chain[i] + aggregation_chain[i+1]) / 2.0
        if i % 3 == 0:
            combined = math.sqrt(combined) if combined > 0 else 0
        new_chain.append(combined)
    aggregation_chain = new_chain

# Core evaluation logic hidden among distractions
def evaluate_performance(raw_metrics):
    # Extract only necessary part
    primary_signal = [x for x in raw_metrics if x > thresholds['warning']]
    if not primary_signal:
        return 0.0
    
    # Real computation buried in noise
    base_score = sum(primary_signal)
    penalty = len([x for x in raw_metrics if x < thresholds['info']]) * 3
    bonus = int(any(x > thresholds['critical'] for x in raw_metrics)) * 50
    
    # Final adjustment using slice length from earlier
    adjustment = len(working_slice) * 2.5
    
    # Actual answer computation
    return base_score - penalty + bonus + adjustment

# Execution point of interest
final_score = evaluate_performance(metric_data=data_stream)

# Output requirement
print(f"Result: {final_score}")