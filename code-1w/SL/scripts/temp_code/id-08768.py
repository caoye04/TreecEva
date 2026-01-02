from collections import defaultdict, Counter

# System parameters for thermal regulation stages
target_temperatures = [23.5, 47.0, 68.3, 91.2, 105.8]
cooling_efficiency = [0.88, 0.76, 0.91, 0.64, 0.79]
activation_cost = {i: val * 1.75 for i, val in enumerate(target_temperatures)}

# Historical data used for baseline comparison (distractor)
historical_loads = [18.2, 22.1, 45.0, 67.8, 90.1, 104.5]
baseline_coverage = set(historical_loads)
outlier_count = len([x for x in historical_loads if x < 20 or x > 100])

# Simulated sensor readings across multiple zones (partially relevant)
sensor_data = [
    [23.4, 23.6, 23.5],
    [46.8, 47.2, 47.0],
    [68.0, 68.5, 68.3],
    [90.9, 91.4, 91.2],
    [105.5, 106.0, 105.8]
]

# Aggregating sensor consistency per stage (semi-relevant preprocessing)
sensor_variance = []
for readings in sensor_data:
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    sensor_variance.append(round(variance, 4))

# Determine operational confidence based on variance threshold (distractor)
operational_flags = []
for var in sensor_variance:
    if var < 0.05:
        operational_flags.append(True)
    else:
        operational_flags.append(False)

# Define process stages with redundancy checks (core logic setup)
process_stages = []
for i in range(len(target_temperatures)):
    stage = {
        'id': i,
        'target': target_temperatures[i],
        'efficiency': cooling_efficiency[i],
        'activation_cost': activation_cost[i],
        'sensor_consistent': operational_flags[i],
        'variance': sensor_variance[i]
    }
    process_stages.append(stage)

# Auxiliary function to compute weighted output (used later)
def calculate_thermal_output(stages):
    total_weighted_output = 0.0
    efficiency_counter = Counter()
    total_adjustment = 0.0
    
    # Track efficiency categories (set operation as distraction)
    high_efficiency_set = set()
    low_efficiency_set = set()
    
    for stage in stages:
        eff_cat = 'high' if stage['efficiency'] >= 0.8 else 'low'
        efficiency_counter[eff_cat] += 1
        
        if stage['efficiency'] >= 0.8:
            high_efficiency_set.add(stage['id'])
        else:
            low_efficiency_set.add(stage['id'])
    
    # Useless aggregation over historical data (distractor block)
    coverage_overlap = baseline_coverage.intersection(set(target_temperatures))
    overlap_sum = sum(coverage_overlap)
    adjustment_factor = 1.0
    if overlap_sum > 0:
        adjustment_factor = 1 + (overlap_sum / 1000)
    
    # Real calculation path
    valid_stages = [s for s in stages if s['sensor_consistent']]
    for stage in valid_stages:
        raw_output = stage['target'] * stage['efficiency']
        cost_penalty = stage['activation_cost'] * 0.1
        total_weighted_output += raw_output - cost_penalty
    
    # Additional meaningless smoothing step (distraction)
    smoothing_buffer = defaultdict(float)
    for i, stage in enumerate(valid_stages):
        smoothing_buffer[i] = total_weighted_output * 0.01
    
    total_weighted_output -= sum(smoothing_buffer.values())
    
    return round(total_weighted_output, 4)

# Secondary auxiliary function (never called - dead code)
def validate_stage_integrity(stages):
    checksum = 0
    for s in stages:
        checksum ^= int(s['target'])
    return checksum % 13 == 0

# Compute final thermal capacity
temperature_audit = [t for t in target_temperatures if t > 50]
reference_baseline = sum(target_temperatures) / len(target_temperatures)

# Key statement
thermal_capacity = calculate_thermal_output(process_stages)

Result: {thermal_capacity}