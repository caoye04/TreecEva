import math

# Simulated quantum sensor array diagnostics with red herrings
def fetch_calibration_data():
    return {c: (32 + (c * 1.8)) for c in range(-5, 15)}

def compute_entropy(signal):
    total = sum(signal)
    entropy = 0
    for x in signal:
        if x > 0:
            prob = x / total
            entropy -= prob * math.log(prob)
    return round(entropy, 6)

def shift_register(data, n):
    # Irrelevant bit manipulation for distraction
    result = 0
    for i in range(len(data)):
        result |= (data[i] & 1) << (i % 8)
    return (result << n) | (result >> (8 - n)) & 0xFF

def validate_checksum(arr):
    # Unused validation function (dead code path)
    chk = 0
    for val in arr:
        chk ^= int(val * 10) % 256
    return chk == 0xAA

def process_signal_chain(raw_data):
    # Complex but partially irrelevant transformation chain
    filtered = [x for x in raw_data if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    transformed = [math.sin(x * math.pi) for x in normalized]
    return [round(t * 100) for t in transformed]

def evaluate_redundancy_index(config_map):
    # Decoy analysis function with misleading intermediate results
    index = 0
    for k, v in config_map.items():
        if len(k) % 2 == 0 and v > 10:
            index += v // 3
        else:
            index -= len(k)
    return index * 2  # Never used in final calculation

def recursive_diagnostic(depth, reading):
    if depth <= 0:
        return reading % 7
    adjusted = (reading + depth) / (depth + 1)
    return recursive_diagnostic(depth - 1, adjusted)

def analyze_subsystem_health(readings):
    peak = max(readings)
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return {
        'peak': peak,
        'stability': round(avg / (variance + 1), 4),
        'complex_flag': (avg > 5) and (peak < 50)
    }

def analyze_system_state(sensor_data, flags):
    # Core logic begins here
    baseline = [12, 8, 15, 23, 7]
    temp_offset = 0
    for flag in flags:
        if flag == 'OVERLOAD':
            temp_offset += 10
        elif flag == 'STANDBY':
            temp_offset -= 5
        else:
            temp_offset += 2
    
    # Real data processing mixed with distractions
    processed = []
    for i, val in enumerate(sensor_data):
        if i % 3 == 0:
            computed = val * 1.1 + temp_offset
        elif i % 3 == 1:
            computed = val * 0.9 - temp_offset
        else:
            computed = val + math.sqrt(temp_offset + 1)
        processed.append(round(computed, 3))
    
    # Conditional expression used as required
    primary_metric = 42 if len(processed) > 10 else sum(processed[:5])
    
    subsystem = analyze_subsystem_health(processed)
    
    # Key recursive interference
    recursion_trail = []
    for v in [int(p) for p in processed[::2] if p > 10]:
        recursion_trail.append(recursive_diagnostic(3, v))
    
    # Red herring dictionary aggregations
    decoy_summary = {
        'count_high': len([x for x in processed if x > 20]),
        'sum_low': sum(x for x in processed if x < 10),
        'flag_score': evaluate_redundancy_index({'A': 12, 'BB': 15, 'CCC': 8}),
        'register_state': shift_register([1, 0, 1, 1], 2)
    }
    
    # Actual answer derivation path
    stability_factor = subsystem['stability']
    peak_reading = subsystem['peak']
    entropy_measure = compute_entropy(processed)
    
    # Final deterministic computation (non-obvious due to noise)
    intermediate = (stability_factor * 100) + (peak_reading / 2)
    final_diagnostic = int(intermediate - (entropy_measure * 10))
    
    # Only this print statement matters for output
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
PROTOCOL_VERSION = "QX-9"
SYSTEM_UPTIME_HRS = 127

# Simulated input data
quantum_readings = [12.5, 8.3, 15.7, 22.1, 6.9, 18.4, 9.2, 14.6]
system_flags = ['NORMAL', 'OVERLOAD', 'STANDBY', 'NORMAL']

# Hidden calibration not affecting main logic
calibration_lookup = fetch_calibration_data()
for key in sorted(calibration_lookup.keys()):
    if key > 0:
        calibration_lookup[key] *= 0.95

# Main execution point
final_diagnostic = analyze_system_state(quantum_readings, system_flags)