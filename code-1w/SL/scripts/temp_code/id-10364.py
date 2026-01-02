import itertools

# Simulated sensor data with metadata tags
data_stream = [
    (12, 'temp', True), (15, 'humid', False), (8, 'temp', True),
    (20, 'pressure', True), (14, 'temp', False), (17, 'temp', True)
]

# Irrelevant auxiliary mapping (distractor)
status_map = {'active': 1, 'standby': 0, 'error': -1}

# Noise filter threshold (unused in final logic)
noise_threshold = 9

# Extract only temperature readings where valid flag is True
temp_readings = [val for val, sensor, valid in data_stream if sensor == 'temp' and valid]

# Misleading transformation chain (dead path)
shifted_values = [(x >> 1) + 3 for x in temp_readings if x > 10]
buffer_cache = {i: v * 2 for i, v in enumerate(shifted_values)}  # Unused

# Augment with dummy indices using enumerate
indexed_data = list(enumerate(temp_readings, start=1))

# Pair forward-backward values via zip (has side-use in real logic)
reversed_indices = list(range(len(indexed_data), 0, -1))
paired_flow = list(zip(indexed_data, reversed_indices))

# Apply exponential scaling on original values (relevant)
scaled_temps = [round(x ** 1.5, 6) for x in temp_readings]

# Create sliding window of size 2 using itertools (core relevant)
windowed = list(itertools.pairwise(scaled_temps))

# Compute differential growth rate across windows
growth_rates = []
for a, b in windowed:
    if a != 0:
        growth_rates.append(round((b - a) / a, 6))
    else:
        growth_rates.append(0.0)

# Fallback smoothing factor (never triggered due to data)
smoothing_factor = 0.85 if len(growth_rates) > 10 else 0.95  # Distractor

# Simulate data enrichment with tuple expansion
enriched_records = []
for idx, rate in enumerate(growth_rates):
    key = f"T{idx+1}"
    phase = "peak" if rate > 0.3 else "stable"
    enriched_records.append((key, rate, phase, (idx, round(rate * 100, 4))))

# Dummy aggregation (red herring)
total_phases = {phase: 0 for phase in ['peak', 'stable', 'decline']}
for _, _, phase, _ in enriched_records:
    if phase in total_phases:
        total_phases[phase] += 1

# Real processing function with nested logic
def process_transformed_data(records):
    accumulator = 0.0
    for entry in records:
        identifier, value, tag, meta = entry
        index_pos = meta[0]
        
        # Conditional bit manipulation on index (obscure but valid)
        transformed_index = index_pos ^ 3  # XOR with fixed
        if transformed_index & 1:  # Check oddness after XOR
            adjusted = value * 1.1
        else:
            adjusted = value * 0.9
        
        # Nested conditional with short-circuit (relevant)
        penalty = 5 if tag == 'peak' and adjusted > 0.5 and len(identifier) > 0 else 0
        bonus = 2 if 'T' in identifier and not (adjusted < 0.1 or tag == 'decline') else 0
        
        # Accumulate net effect
        net_impact = adjusted * 100 + bonus - penalty
        accumulator += net_impact
    
    return int(round(accumulator))

# Execute main computation
final_output = process_transformed_data(enriched_records)

# Print result as required
print(f"Result: {final_output}")