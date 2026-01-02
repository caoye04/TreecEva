from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_packets = [
    {'id': 1, 'values': [0.1, 0.3, 0.4, 0.2], 'type': 'A', 'status': 'active'},
    {'id': 2, 'values': [0.5, 0.6, 0.7], 'type': 'B', 'status': 'active'},
    {'id': 3, 'values': [0.8, 0.9, 1.0, 1.1, 1.2], 'type': 'A', 'status': 'inactive'},
    {'id': 4, 'values': [0.2, 0.25], 'type': 'C', 'status': 'active'}
]

# Irrelevant statistical counters (distractors)
stale_counter = defaultdict(int)
drop_counter = Counter()
for packet in data_packets:
    stale_counter[packet['type']] += len(packet['values'])
    if packet['status'] == 'inactive':
        drop_counter[packet['type']] += 1

# Signal processing pipeline
noise_floor = 0.15
def filter_noise(sample_list):
    return [x for x in sample_list if x > noise_floor]

def integrate_signal(samples):
    return sum(x ** 1.5 for x in samples)

# Misleading energy calculation (unused in final path)
def compute_energy(sig):
    return sum(math.sin(x) * math.exp(-x/10) for x in sig)

# Decoy transformation chain
temp_transform = lambda x: x * 2 if x < 0.5 else x * 0.5
legacy_buffer = []
for packet in data_packets:
    transformed = [temp_transform(val) for val in packet['values']]
    legacy_buffer.extend(transformed)

# Core processing function
def preprocess_packet(packet):
    if packet['status'] != 'active':
        return []
    filtered = filter_noise(packet['values'])
    if len(filtered) == 0:
        return []
    # Apply weighting based on type
    weight = 1.0
    if packet['type'] == 'A':
        weight = 1.2
    elif packet['type'] == 'B':
        weight = 0.9
    else:
        weight = 1.1
    return [x * weight for x in filtered]

# Accumulate processed signal chunks
processed_data = []
compression_log = []
for pkt in data_packets:
    result_chunk = preprocess_packet(pkt)
    if result_chunk:
        processed_data.extend(result_chunk)
        compression_log.append(len(result_chunk))

# Dead code path - never executed due to filtering above
redundant_shift = 0
if len(processed_data) > 100:
    redundant_shift = sum(processed_data) % 7

# Actual diagnostic analysis
bit_flag = 0
for val in processed_data:
    shifted = int(val * 10) & 7  # Extract lower 3 bits
    bit_flag ^= shifted  # Accumulate XOR of flags

# Secondary metric (distraction)
entropy_proxy = 0.0
if processed_data:
    mean_val = sum(processed_data) / len(processed_data)
    variance = sum((x - mean_val) ** 2 for x in processed_data) / len(processed_data)
    entropy_proxy = math.log(variance + 1) if variance > 0 else 0.0

# Main recursive integrator (key computation path)
def integrate_recursive(seq, idx=0, acc=0.0, mult=1.0):
    if idx >= len(seq):
        return acc
    current = seq[idx]
    next_mult = mult * 1.05 if current > 0.5 else mult * 0.95
    new_acc = acc + current * mult
    # Early termination red herring (never triggered in this case)
    if new_acc < 0:
        return -1
    return integrate_recursive(seq, idx + 1, new_acc, next_mult)

# Spurious sort operation (no effect on result)
sorted_diagnostics = sorted(processed_data, key=lambda x: abs(x - 0.5))
baseline_score = sum(sorted_diagnostics[::2])  # Another distraction

# Final analysis combining multiple concepts
def analyze_signal(signal_sequence):
    if not signal_sequence:
        return 0.0
    
    # Bit manipulation layer
    control_word = 0
    for i, val in enumerate(signal_sequence):
        if i % 2 == 0:
            control_word += int(val * 100) & 15
        else:
            control_word -= int(val * 50) & 7
    
    # Normalize control word
    control_word = abs(control_word) % 1000
    
    # Primary accumulation
    raw_integral = integrate_recursive(signal_sequence)
    
    # Secondary adjustment using string-based key (obscure but valid)
    key_seed = "signal_{}".format(len(signal_sequence)).__hash__() % 97
    adjustment = (control_word * 0.01) + (key_seed * 0.001)
    
    # Final composition
    result = raw_integral + adjustment
    
    # Red herring: unused conditional override
    if result > 1000 or result < 0:
        result = 999.999  # Never reached
    
    return result

# Execute critical statement
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")