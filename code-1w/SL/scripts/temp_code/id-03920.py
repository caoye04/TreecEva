def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]

def validate_sequence(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

process_flow = {
    'stages': [3, 7, 2, 8, 5],
    'modes': {1: 'idle', 2: 'active', 3: 'standby'},
    'threshold': 6,
    'buffer': [1, 4, 6, 9, 2, 3],
    'flags': {True: 'on', False: 'off'}
}

# Irrelevant transformation chain (distractor)
processed_buffer = sorted([x**2 for x in process_flow['buffer'] if x % 2 == 0])
temp_scaling = sum(processed_buffer) / len(processed_buffer)

# Decoy function with unused logic
def analyze_efficiency(data):
    cumulative = 0
    for val in data:
        if val > 4:
            cumulative += val * 0.1
    return cumulative

# Real calculation buried in noise
status_log = set()
for stage in process_flow['stages']:
    if stage > process_flow['threshold']:
        status_log.add('high')
    elif stage == process_flow['threshold']:
        status_log.add('medium')
    else:
        status_log.add('low')

# Unused but plausible-looking aggregation
mode_count = {}
for mode in process_flow['modes']:
    mode_count[mode] = len(process_flow['modes'][mode])

# Core logic disguised among red herrings
def calculate_thermal_output(flow):
    stages = flow['stages']
    base_energy = 0
    adjustment_factor = 1.0
    
    # Real computation starts here
    for s in stages:
        if s % 2 == 0:
            base_energy += s ** 2
        else:
            base_energy -= s
    
    # Secondary adjustment
    threshold = flow['threshold']
    high_stage_count = len([s for s in stages if s > threshold])
    
    # Tertiary influence via set size
    log_size_impact = len(status_log) * 10
    
    # Actual formula
    result = (base_energy + log_size_impact) * (high_stage_count + 1)
    
    # Dead code branch (never executed due to structure)
    if False and 'debug' in flow:
        result *= 0.5
    
    return result

# Unused recursive distraction
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

# Key execution point
thermal_capacity = calculate_thermal_output(process_flow)

# Final output
print(f"Result: {thermal_capacity}")