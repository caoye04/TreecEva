import math

# Simulated telemetry data from a distributed sensor array
telemetry_stream = [142, 89, 205, 76, 133]
baseline_offset = 98
calibration_factor = 1.07

# Irrelevant audio processing stubs (dead code path)
def analyze_tone(frequency):
    return int(frequency * 0.84) if frequency > 50 else 0

# Unused signal smoothing function
def smooth_signal(data, weight=0.3):
    smoothed = []
    for i in range(len(data)):
        prev = smoothed[i-1] if i > 0 else data[i]
        smoothed.append(weight * data[i] + (1 - weight) * prev)
    return smoothed

# Auxiliary transformation map for non-critical diagnostics
diagnostic_map = {
    'voltage': lambda x: x * 1.02,
    'current': lambda x: x * 0.93,
    'thermal': lambda x: math.log(x + 1) * 1.1
}

# System state flags (some are decoys)
system_state = {
    'active_nodes': 7,
    'power_cycle_count': 14,
    'last_reset_flag': False,
    'overclock_mode': True,
    'legacy_compatibility': 'disabled',
    'cache_integrity': 'valid'
}

# Complex logic flow with red herrings and conditional branching
logic_flow = []
accumulator = 0
shift_register = 0b1010

for idx, reading in enumerate(telemetry_stream):
    # Apply baseline correction and conditional scaling
    adjusted = (reading - baseline_offset) * calibration_factor
    
    # Bit manipulation decoy: simulate checksum update (not used later)
    shift_register ^= (reading << 1) & 0b1111
    shift_register = (shift_register >> 1) | ((shift_register & 1) << 3)
    
    # Conditional expression with misleading intermediate
    status_flag = 'nominal' if adjusted > 40 else 'caution'
    diagnostic_score = math.sqrt(adjusted ** 2 + 10) if status_flag == 'nominal' else adjusted / 2
    
    # Accumulate only every odd-indexed result (critical logic)
    if idx % 2 == 1:
        accumulator += int(diagnostic_score)
    
    # Update logic flow with irrelevant metadata
    logic_flow.append({
        'index': idx,
        'raw': reading,
        'adjusted': round(adjusted, 3),
        'diagnostic': diagnostic_score,
        'flag': status_flag,
        'checksum': hex(shift_register),
        'derived_key': idx * 17 + 23  # unused obfuscation
    })

# Secondary loop with dead computation (no impact on final result)
summary_stats = []
for entry in logic_flow:
    z_score = (entry['adjusted'] - 50) / 15
    category = 'high' if z_score > 1 else 'low'
    summary_stats.append({'z': round(z_score, 2), 'cat': category})

# Decoy aggregation using dictionary operations (irrelevant)
aggregated_diagnostics = {}
for key in diagnostic_map.keys():
    aggregated_diagnostics[key] = sum(diagnostic_map[key](i) for i in range(5, 10))

# Critical conditional branch with tuple unpacking distraction
aux_data = [(3, 7), (11, 13), (17, 19)]
total_aux = 0
for a, b in aux_data:
    total_aux += a * b  # Dead computation

# Core calculation buried in distractions
primary_accumulation = 0
for item in logic_flow[1::2]:  # Every second item starting at index 1
    primary_accumulation += int(item['diagnostic'])

# Final processing with conditional expression and dict lookup red herring
def process_metrics(flow, state):
    # Extract relevant indices
    relevant_indices = [i for i, x in enumerate(flow) if x['flag'] == 'nominal']
    
    # Distractor: use dictionary get() with default (unused result)
    node_multiplier = state.get('node_scale', 1.0) if state['active_nodes'] > 5 else 0.8
    
    # Real logic: sum diagnostic values at even positions in filtered set
    filtered_sum = sum(
        int(flow[i]['diagnostic']) for i in relevant_indices if i % 2 == 0
    )
    
    # Secondary real component: use accumulator from earlier odd-index sum
    base_value = primary_accumulation
    
    # Final deterministic computation (answer is base_value + filtered_sum)
    temp_result = base_value + filtered_sum
    
    # Conditional override that never triggers (decoy)
    if state['legacy_compatibility'] == 'enabled' and not state['last_reset_flag']:
        return temp_result * 0.75
    else:
        return temp_result

# Execute critical statement
final_diagnostic = process_metrics(logic_flow, system_state)

# Print result as required
print(f"Result: {final_diagnostic}")