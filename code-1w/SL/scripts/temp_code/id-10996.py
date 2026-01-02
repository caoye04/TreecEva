from collections import defaultdict

# Simulate a chemical process flow with intermediate checks
def analyze_purity_levels(readings):
    purity_count = defaultdict(int)
    for r in readings:
        if r > 90:
            purity_count['high'] += 1
        elif r > 70:
            purity_count['medium'] += 1
        else:
            purity_count['low'] += 1
    # Distractor: this computation is unused later
    total_weighted_score = sum(r**0.5 for r in readings if r > 80)
    return purity_count

# Main flow calculator
def calculate_net_flow(sequence):
    base_flow = 100
    multiplier = 1.0
    temp_adjustment = 0
    
    for step in sequence:
        if step['type'] == 'reaction':
            base_flow += step['delta']
            temp_adjustment += step['temp_delta']
        elif step['type'] == 'condensation':
            base_flow *= 0.9
        elif step['type'] == 'evaporation':
            base_flow *= 1.1
    
    # Complex conditional expression affecting flow
    multiplier = 1.05 if temp_adjustment > 0 else 0.95
    final_flow = base_flow * multiplier
    
    # Dead code path (distractor)
    if False:
        correction_factor = 0
        for i in range(len(sequence)):
            correction_factor += i  # Never executed
    
    return int(final_flow)

# Sensor data (unused in final result but plausible)
sensor_logs = [92, 85, 73, 94, 67, 88]
analyze_purity_levels(sensor_logs)

# Process configuration
process_sequence = [
    {'type': 'reaction', 'delta': 15, 'temp_delta': 5},
    {'type': 'condensation', 'delta': 0, 'temp_delta': 0},
    {'type': 'reaction', 'delta': -10, 'temp_delta': 3},
    {'type': 'evaporation', 'delta': 0, 'temp_delta': 0},
    {'type': 'reaction', 'delta': 20, 'temp_delta': -10}
]

# Extra irrelevant variables (distractors)
total_steps = len(process_sequence)
invalid_flag = None
aux_data = [x['delta'] for x in process_sequence if x['type'] == 'reaction']
sum_aux = sum(aux_data)  # Computed but not used

# Key execution point
net_flow = calculate_net_flow(process_sequence)

# Output result as required
print(f"Result: {net_flow}")