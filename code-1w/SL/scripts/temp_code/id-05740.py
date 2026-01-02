import math

def simulate_sensor_drift(raw_values):
    # Irrelevant function: simulates sensor noise but not used in final computation
    return [x + 0.1 * math.sin(i) for i, x in enumerate(raw_values)]

def deprecated_calculate_load(x, y):
    # Dead code path: unused legacy function
    return (x ** 2 + y ** 2) ** 0.5

def compute_entropy(data):
    # Distractor function: calculates entropy but result is ignored
    total = sum(data)
    if total == 0:
        return 0
    probs = [d / total for d in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def analyze_system_response(events, factor):
    # Core logic with embedded distractions
    base_score = 0
    adjustment = len(events) % 7
    
    # Red herring: complex-looking but unused transformation
    transformed = [\n        (e['temp'] ** 1.5) / (e['time'] + 1) for e in events if e['temp'] > 30
    ]
    
    # Decoy accumulator
    dummy_accum = 0
    for e in events:
        dummy_accum += e['time'] * 0.01
    
    # Relevant logic chain begins
    valid_events = [e for e in events if e['status'] == 'active']
    if len(valid_events) == 0:
        return 0
    
    # Nested logic with multiple steps
    peak_flux = max(e['flux'] for e in valid_events)
    avg_temp = sum(e['temp'] for e in valid_events) / len(valid_events)
    
    # Conditional branch based on threshold
    if avg_temp > 45:
        base_score += 150
    else:
        base_score += 90
    
    # Bit manipulation red herring
    masked_flux = peak_flux & 0xFFFF
    
    # More relevant computation
    duration = events[-1]['time'] - events[0]['time']
    if duration > 0:
        rate_of_change = (events[-1]['temp'] - events[0]['temp']) / duration
        if rate_of_change > 0.5:
            base_score += 40
    
    # Final calculation with factor
    result = base_score * factor
    
    # Unused but plausible intermediate
    normalized = result / (len(valid_events) + 1)
    
    return int(result)

# Main execution
system_log = [
    {'time': 0, 'temp': 40, 'flux': 250, 'status': 'inactive'},
    {'time': 3, 'temp': 42, 'flux': 260, 'status': 'active'},
    {'time': 6, 'temp': 47, 'flux': 275, 'status': 'active'},
    {'time': 9, 'temp': 55, 'flux': 290, 'status': 'active'},
    {'time': 12, 'temp': 60, 'flux': 305, 'status': 'active'},
    {'time': 15, 'temp': 58, 'flux': 280, 'status': 'active'}
]

# Irrelevant preprocessing
raw_temps = [entry['temp'] for entry in system_log]
simulated_drift = simulate_sensor_drift(raw_temps)

# Unused statistical distraction
entropy_value = compute_entropy([5, 12, 23, 38, 45])
efficiency_factor = 1.8

# Key statement
thermal_capacity = analyze_system_response(system_log, efficiency_factor)

# Print result as required
print(f"Result: {thermal_capacity}")