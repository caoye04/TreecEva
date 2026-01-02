import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    timestamps = list(range(100, 200, 3))
    voltages = [round(120 + 10 * math.sin(t / 50), 4) for t in timestamps]
    temperatures = [round(70 + 3 * math.cos(t / 60) + abs(math.sin(t / 30)), 2) for t in timestamps]
    cycle_counts = [t * 2 + (t % 7) for t in timestamps]
    
    # Construct log entries with redacted fields and irrelevant metadata
    logs = []
    for i in range(len(timestamps)):
        log_entry = {
            'ts': timestamps[i],
            'v': voltages[i],
            'temp': temperatures[i],
            'cycles': cycle_counts[i],
            'status': 'OK' if temperatures[i] < 72 else 'WARN',
            'meta': {  # Irrelevant nested metadata
                'version': '2.1.0',
                'node_id': f'N-{i % 10}',
                'debug_flag': False,
                'payload_size': 128 + i % 16
            }
        }
        logs.append(log_entry)
    return logs

# Distractor function: computes unrelated statistical moment (not used in final result)
def compute_fourth_moment(data_list):
    mean_val = sum(data_list) / len(data_list)
    fourth_powers = [(x - mean_val)**4 for x in data_list]
    return sum(fourth_powers) / len(fourth_powers)

# Unused helper: simulates checksum but never called
compute_checksum = lambda data: sum([hash(str(v)) % 1000 for v in data]) * 0.001

# Core processing pipeline
system_flags = {
    'threshold_voltage': 122.5,
    'overclock_penalty': 1.08,
    'decay_factor': 0.93,
    'enable_correction': True
}

# Misleading intermediate calculations
raw_cycles = [i * 3 + (i**2 % 5) for i in range(30)]
decoy_signal = sum([math.tan(i / 10) for i in raw_cycles if i % 4 == 0])
dummy_aggregate = len(raw_cycles) * 1.5 if decoy_signal > 10 else 0  # Dead branch

# Real-time filter mask (only some entries are valid)
valid_mask = lambda entry: entry['v'] > 118 and entry['cycles'] % 2 == 0

# Signal transformation map with multiple red herrings
transform_map = {
    'A': lambda x: x * 1.05,
    'B': lambda x: x * 0.98 + 3.2,
    'C': lambda x: x ** 0.5 * 10,
    'D': lambda x: x  # Identity, unused
}

# Main metric processor
weights = {'v': 0.3, 'temp': -0.15, 'cycles': 0.002}

# High-interference computation block
def process_metrics(entries, config):
    # Irrelevant pre-allocation
    buffer_pool = [{'buf': [0]*8} for _ in range(5)]
    temp_cache = {}  # Never actually used

    # Filter relevant entries
    filtered = [e for e in entries if valid_mask(e)]
    
    # Distractor: build unused frequency table
    voltage_bins = {}
    for e in entries:
        bin_key = int(e['v'])
        voltage_bins[bin_key] = voltage_bins.get(bin_key, 0) + 1
    
    # Critical path begins: extract core values
    voltages = [e['v'] for e in filtered]
    temps = [e['temp'] for e in filtered]
    cycles = [e['cycles'] for e in filtered]
    
    # Apply weighting and correction
    base_score = 0
    for i in range(len(filtered)):
        reading = weights['v'] * voltages[i]
        reading += weights['temp'] * temps[i]
        reading += weights['cycles'] * cycles[i]
        
        if config['enable_correction']:
            if voltages[i] > config['threshold_voltage']:
                reading *= config['overclock_penalty']
            else:
                reading *= config['decay_factor']
        
        base_score += reading
    
    # Secondary adjustment using set operations (irrelevant to outcome but looks important)
    unique_temps = set(temps)
    outlier_temps = {t for t in unique_temps if t > 73}
    penalty_rate = 0.01 * len(outlier_temps) if outlier_temps else 0
    
    # Final computation chain
    adjustment_factor = 1 - penalty_rate
    raw_final = base_score * adjustment_factor
    
    # Normalize using combinatorics-based divisor (key insight)
    n = len(filtered)
    if n > 1:
        combinations = math.factorial(n) // (math.factorial(2) * math.factorial(n-2))  # C(n,2)
        normalized = raw_final / combinations if combinations > 0 else raw_final
    else:
        normalized = raw_final
    
    # Final transformation via lambda (required language feature)
    apply_offset = lambda x: x + 50.0
    final_value = apply_offset(normalized)
    
    # Dead code path: masked by condition that never triggers
    if 'DEBUG_MODE' in os.environ:
        import json
        print(json.dumps(buffer_pool))
    
    return final_value

# Generate inputs
log_entries = generate_telemetry()

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)

# Output result as required
print(f"Result: {final_diagnostic}")