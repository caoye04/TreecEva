import itertools

def preprocess_readings(sensor_stream, baseline):
    processed = []
    for idx, reading in enumerate(sensor_stream):
        adjusted = (reading - baseline) * 1.05
        if idx % 4 == 0:
            adjusted += 0.2
        processed.append(round(adjusted, 3))
    return processed

def generate_phase_shift(pattern):
    shifted = [0] * len(pattern)
    for i in range(len(pattern)):
        shifted[i] = pattern[(i + 3) % len(pattern)] ^ (i & 3)
    return shifted

def validate_coherence(sequence):
    score = 0
    for a, b in zip(sequence, sequence[1:]):
        if (a + b) % 2 == 0:
            score += 1
        else:
            score -= 2
    return score > -5

def compute_harmonic(chain):
    total = 0.0
    for i, val in enumerate(chain, 1):
        if i % 3 == 0:
            total += val / i
        else:
            total += val * 0.1
    return round(total, 4)

def filter_anomalies(dataset):
    clean_set = []
    threshold = sum(dataset) / len(dataset)
    for item in dataset:
        if abs(item - threshold) < 15:
            clean_set.append(item)
    return clean_set  # Dead code path — not used in final result

def decode_signature(signal):
    temp = 0
    for x in signal[:5]:
        temp ^= int(x * 2) & 7
    return temp

def aggregate_metrics(data_blocks, key):
    accumulator = 0
    for i, block in enumerate(data_blocks):
        block_val = 0
        if i % 2 == 0:
            block_val = sum(b & 3 for b in block) * key[i % len(key)]
        else:
            block_val = sum(b >> 1 for b in block) + key[(i+1) % len(key)]
        accumulator += block_val * (i + 1)
    
    # Irrelevant transformation
    dummy_seq = [x | 4 for x in key]
    dummy_sum = sum(dummy_seq) % 17
    
    # Critical red herring
    intermediate_fuse = 0
    for j in range(3):
        intermediate_fuse += dummy_sum * (j + 2)
    
    # Actual relevant logic continues
    phase_core = generate_phase_shift(key)
    coherence_flag = validate_coherence(phase_core)
    
    if coherence_flag:
        harmonic_input = [x * 2 for x in phase_core]
        adjustment_factor = compute_harmonic(harmonic_input)
        accumulator = int(accumulator * (adjustment_factor / 10)) + 53
    
    # Misleading checksum
    decoy_check = decode_signature([float(x) for x in phase_core])
    accumulator += decoy_check  # Minor but valid contribution
    
    # Final irrelevant block
    temp_grid = list(itertools.product([1, 2], ['a', 'b']))
    metadata_index = 0
    for idx, (num, char) in enumerate(temp_grid):
        metadata_index += num ^ ord(char)
    
    final_diagnostic = accumulator + metadata_index  # Answer influenced only by real dependencies
    return final_diagnostic

# Main execution
baseline_offset = 23.1
sensor_input = [89, 95, 76, 88, 92, 84, 77, 81]
reference_pattern = [5, 3, 8, 1, 6]

turbine_data = []
for raw_block in [sensor_input[i:i+4] for i in range(0, len(sensor_input), 4)]:
    proc_block = preprocess_readings(raw_block, 75)
    int_block = [int(sum(proc_block[j:j+2])) for j in range(0, len(proc_block), 2)]
    turbine_data.append(int_block)

calibration_sequence = [x ^ 5 for x in reference_pattern]
calibration_sequence = [x + 2 for x in calibration_sequence]  # Overwritten next

calibration_sequence = [7, 2, 9, 4, 8]  # Final calibration vector

# Execute critical statement
final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
print(f"Result: {final_diagnostic}")