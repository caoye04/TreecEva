import math

# Simulated sensor data and diagnostic framework for a spacecraft subsystem
vital_readings = [144, 25, 67, 89, 101, 33, 78, 92]
temp_buffer = [x ** 0.5 for x in vital_readings if x > 50]

# Irrelevant transformation: frequency harmonics (dead-end analysis)
frequency_harmonics = list(map(lambda x: round(math.sin(x) * 100, 2), temp_buffer))
harmonic_sum = sum(frequency_harmonics)  # Misleading aggregate

# Core signal extraction via slicing and filtering
signal_slice = vital_readings[1:6:2]  # Extracts indices 1, 3, 5: [25, 89, 33]
filtered_signal = [x for x in signal_slice if x % 2 == 1]  # All are odd, so unchanged

# Secondary noise correction using modular arithmetic (distractor)
correction_key = 7
noise_pattern = [(x % correction_key) * 2 for x in filtered_signal]
dummy_correction = sum(noise_pattern) / len(noise_pattern) if noise_pattern else 0

# Construct health signature using bit manipulation and logical ops
bit_encoded = 0
for val in filtered_signal:
    bit_encoded ^= (val << 1) | (val & 1)

health_signature = bit_encoded + (len(filtered_signal) << 4)

# System log generation with red herring checksums
system_log = []
for i, val in enumerate(signal_slice):
    entry = {
        'id': i,
        'raw': val,
        'squared': val ** 2,
        'checksum': (val * 3 + 5) % 97
    }
    system_log.append(entry)

# Decoy function: never used but looks important
def analyze_redundancy(log):
    total = 0
    for e in log:
        total += e['squared'] // (e['id'] + 1)
    return total >> 2

# Another decoy: complex lambda chain with no invocation
anomaly_detector = lambda data: \
    list(map(lambda x: x > 50 and (x & 1) == 0, \
           [item['raw'] * 2 for item in data if item['checksum'] < 50]))

# Critical processing function
def process_metrics(signature, log):
    base_score = signature & 0xFF  # Lower byte
    shift_factor = signature >> 8
    
    # Extract specific log-derived values (only some entries matter)
    relevant_ids = [e['id'] for e in log if e['raw'] > 30]
    id_sum = sum(relevant_ids)
    
    # Dummy calculation that seems important but isn't used in final result
    fake_metric = (base_score + id_sum) // 2
    fake_metric = math.ceil(fake_metric * 1.5)
    
    # Real computation path
    raw_values = [e['raw'] for e in log]
    avg_val = sum(raw_values) / len(raw_values)
    
    # Conditional adjustment based on logical combination
    adjustment = 0
    if all(v > 20 for v in raw_values) and any(v > 80 for v in raw_values):
        adjustment = 17
    
    # Final integration using integer division and rounding
    intermediate = int(avg_val // 1.5) + (shift_factor * 2)
    final_value = intermediate ^ adjustment  # Bitwise finalize
    
    # Additional distractor: floating point decay simulation (unused)
    decay_chain = 100.0
    for i in range(5):
        decay_chain *= 0.87
        decay_chain -= 2.1
    
    return final_value

# Execute critical statement
final_diagnostic = process_metrics(health_signature, system_log)
print(f"Target result: {final_diagnostic}")