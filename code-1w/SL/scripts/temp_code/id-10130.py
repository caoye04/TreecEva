import math

# Simulated system telemetry data
telemetry_stream = [
    {'time': 0.0, 'value': 100, 'status': 'OK'},
    {'time': 0.5, 'value': 108, 'status': 'OK'},
    {'time': 1.0, 'value': 114, 'status': 'WARNING'},
    {'time': 1.5, 'value': 97, 'status': 'ERROR'},
    {'time': 2.0, 'value': 88, 'status': 'ERROR'}
]

# Irrelevant audio processing stubs (distractor)
def apply_eq(signal, freq):
    return [x * 0.9 for x in signal]

def fft_transform(data):
    return [abs(x) ** 2 for x in data]

# Unused error simulation (dead code path)
class LegacyErrorSimulator:
    def __init__(self, seed=42):
        self.seed = seed
    
    def simulate(self, count):
        return [(i * self.seed) % 13 for i in range(count)]

# Real processing begins here
log_entries = []
for entry in telemetry_stream:
    normalized = entry['value'] / 10.0
    if entry['status'] == 'OK':
        category = 0
    elif entry['status'] == 'WARNING':
        category = 1
    else:
        category = 2
    log_entries.append({'norm': normalized, 'cat': category})

# System flags with red herring values
system_flags = {
    'overclock': True,
    'debug_mode': False,
    'cache_enabled': True,
    'legacy_protocol': True,
    'threshold_violation': False,
    'temp_bypass': True,
    'audit_level': 3
}

# Decoy statistical function that's not used directly
compute_stats = lambda data: {
    'mean': sum(d['norm'] for d in data) / len(data),
    'max_cat': max(d['cat'] for d in data)
}

# Actual core logic hidden among distractors
def analyze_entry(entry):
    norm_val = entry['norm']
    base_score = norm_val * 1.5
    
    # Bit manipulation for checksum simulation (relevant)
    raw_int = int(norm_val)
    checksum = (raw_int ^ 0xCAF) >> 2
    adjusted = base_score + (checksum % 3)
    
    return adjusted

def process_metrics(entries, flags):
    results = []
    temp_buffer = []  # unused in final logic but looks important
    
    for e in entries:
        score = analyze_entry(e)
        if e['cat'] == 2:
            score *= 1.2
        results.append(score)
    
    # Real aggregation
    aggregate = sum(results)
    
    # Distracting control flow
    if flags['debug_mode'] and flags['legacy_protocol']:
        adjustment_factor = 0.85
    elif flags['overclock'] and not flags['threshold_violation']:
        adjustment_factor = 1.1  # This branch is taken
    else:
        adjustment_factor = 1.0
    
    # Spurious sorting (looks important, but only used once)
    sorted_results = sorted(results, reverse=True)
    median_tweak = sorted_results[len(sorted_results)//2] * 0.05
    
    # Final computation chain
    intermediate = aggregate * adjustment_factor
    verification_seed = 256
    
    # Recursive validation wrapper (misleading name, simple function)
    def validate_sum(val, depth=2):
        if depth <= 0:
            return val + 1.0
        return validate_sum(val * 0.99, depth - 1)
    
    validated = validate_sum(intermediate)
    final_raw = validated + median_tweak
    
    # Final threshold filter
    if final_raw < 100:
        final_raw = 100
    
    # Critical output variable
    final_diagnostic = int(final_raw * 1.07)  # Amplification factor
    
    # Dead code - looks like logging but never called
    def generate_report(data):
        return '\n'.join(f"Entry {i}: {x}" for i, x in enumerate(data))
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")