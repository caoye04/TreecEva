import math

# Irrelevant helper function (dead code path)
def compute_noise_floor(signal, band):
    return sum([(s ** 2) % 7 for s in signal]) * 0.3

# Misleading intermediate calculation
temporal_offset = 127
phase_shift = (temporal_offset * 2.5) % 6
baseline_drift = int(phase_shift * 8) ^ 42

# Real data structure initialization
energy_nodes = [
    {'id': 'E1', 'input': 13, 'state': 'active', 'flags': [1, 0, 1]},
    {'id': 'E2', 'input': 19, 'state': 'idle', 'flags': [0, 1, 1]},
    {'id': 'E3', 'input': 23, 'state': 'active', 'flags': [1, 1, 0]}
]

# Decoy variables with plausible but unused computations
signal_chain = [x['input'] * 1.7 for x in energy_nodes if x['state'] == 'idle']
stress_factor = 0.0
for node in energy_nodes:
    if node['id'] == 'E2':  # This branch does nothing important
        stress_factor += node['input'] / 100
    else:
        stress_factor += 0.1

# Distractor: complex-looking but unused bitwise cascade
status_word = 0
for node in energy_nodes:
    flag_val = sum(node['flags']) << 1
    status_word ^= (flag_val * 3) & 0xF

# Unused lambda (red herring)
analyze_spike = lambda x: math.log(x + 1) * 2.1 if x > 10 else 0.0

# Real logic begins here — deeply nested and interwoven with prior noise
scaling_map = {13: 2, 19: 3, 23: 5}

def evaluate_system_load(nodes, stress):
    total_load = 0
    adjustment = 1.0
    
    # First real computation hidden among distractions
    for entry in nodes:
        raw_input = entry['input']
        state = entry['state']
        
        # Only active nodes contribute to load
        if state != 'active':
            continue
            
        # Apply multiplicative scaling via dictionary lookup
        if raw_input in scaling_map:
            scaled = raw_input * scaling_map[raw_input]
            
            # Conditional bit manipulation based on input parity
            if scaled % 2 == 0:
                scaled = (scaled >> 1) | 7
            else:
                scaled = (scaled << 1) ^ 3
            
            # Accumulate transformed values
            total_load += scaled
    
    # Secondary transformation using stress factor (mostly irrelevant except baseline)
    adjustment *= (1 + stress * 2)
    
    # Critical early return disguised as redundancy
    if total_load > 100:
        return int(total_load * adjustment) + 5
    
    # Fallback (not reached)
    return total_load

# Additional red herring: dictionary operations not used in final result
summary_stats = {
    'count': len(energy_nodes),
    'flags_sum': sum(sum(n['flags']) for n in energy_nodes),
    'peak': max(n['input'] for n in energy_nodes)
}
summary_stats['derived'] = summary_stats['count'] * summary_stats['flags_sum']

# Key execution point
thermal_capacity = evaluate_system_load(energy_nodes, stress_factor)

# Print required result
print(f"Result: {thermal_capacity}")