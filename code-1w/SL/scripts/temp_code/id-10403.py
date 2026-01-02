import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_sequences = [
        'ACGTGGCTAGTT', 'TGCAATCGACTG', 'GGATCCGGATCC', 'TTAGGGTTAGGG',
        'ATATATATATAT', 'CGCGCGCGCGCG', 'AAATTTCCCGGG'
    ]
    return raw_sequences

def compute_gc_content(sequence):
    gc_count = sum(1 for base in sequence if base in 'GC')
    return round(gc_count / len(sequence), 6)

def filter_noisy_reads(sequences, min_length=6, max_entropy=0.95):
    filtered = []
    entropy_cache = {}
    decoy_sum = 0

    for seq in sequences:
        if len(seq) < min_length:
            continue

        # Irrelevant entropy calculation (distractor)
        unique_bases = set(seq)
        seq_entropy = 0.0
        for base in unique_bases:
            p = seq.count(base) / len(seq)
            if p > 0:
                seq_entropy -= p * math.log2(p)
        entropy_cache[seq] = round(seq_entropy, 4)

        if seq_entropy <= max_entropy:
            filtered.append(seq)

        # Dead computation path - never used later
        temp_val = sum(ord(b) for b in seq) % 7
        decoy_sum += temp_val  # Red herring accumulator

    # Unused diagnostic output
    debug_info = {"valid_count": len(filtered), "avg_entropy": sum(entropy_cache.values()) / len(entropy_cache)}
    return filtered

def generate_reference_map(keys, offset=100):
    # Creates a dummy mapping not fully utilized
    ref_map = {k[:4]: hash(k) % offset for k in keys}
    ref_map['META'] = 42  # Misleading magic number
    return ref_map

def transform_sequence(seq):
    # Complex transformation with red herrings
    rev_seq = seq[::-1]
    shifted = ''.join(chr((ord(c) - 65 + 3) % 26 + 65) for c in rev_seq)
    score = 0
    for i, c in enumerate(shifted):
        if c in 'GCTA':
            score += (i + 1) * (ord(c) % 7)
    # Only the length matters in the end
    return {'transformed': shifted, 'score': score, 'length': len(seq)}

def analyze_readings(data_list, config_map):
    results = []    
    aggregate_flag = False
    accumulator = 0
    temp_tracker = []

    # Key logic buried in distractions
    critical_values = []
    for item in data_list:
        x = transform_sequence(item)
        y = compute_gc_content(item)
        z = len(item) ** 2

        # Decoy branching
        if y > 0.5 and z < 200:
            temp_tracker.append(z * 0.1)
        elif 'TTT' in item or 'AAA' in item:
            temp_tracker.append(-1 * y)
        else:
            # This branch contributes to final result
            critical_values.append(len(item))

        # Bit manipulation side-channel (irrelevant)
        bit_fingerprint = 0
        for c in item:
            bit_fingerprint ^= ord(c)
        bit_fingerprint &= 0xFF
        if bit_fingerprint % 13 == 0:
            aggregate_flag = not aggregate_flag

    # Real answer derivation hidden here
    base_result = sum(critical_values)
    adjustment = config_map.get('THRESH', 10) - config_map.get('OFFSET', 4)
    final_score = base_result * adjustment

    # Multiple return candidates (misdirection)
    candidate_a = final_score + len(temp_tracker)
    candidate_b = final_score - (bit_fingerprint % 9)
    candidate_c = int(str(final_score)[:3]) if final_score > 100 else final_score

    # The real assignment
    final_diagnostic = final_score  # Critical line: this is the actual answer

    # Excessive logging (dead code)
    logs = []
    logs.append(f'Processed {len(data_list)} items')
    logs.append(f'Critical path triggered {len(critical_values)} times')
    logs.append(f'Temp tracker size: {len(temp_tracker)}')
    logs.append(f'Final diagnostic set to {final_diagnostic}')

    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Initial data collection
    sensor_reads = collect_sensor_data()
    
    # Irrelevant preprocessing chain
    processed_set = set()
    for read in sensor_reads:
        if read.startswith('A') or read.endswith('G'):
            processed_set.add(read)
    processed_list = sorted(list(processed_set), key=lambda x: x.count('G'))

    # Filtering with distractors
    clean_reads = filter_noisy_reads(processed_list)
    
    # Dummy reference structure with misleading entries
    keys_used = ['ACGTGGC', 'TGCAATC', 'GGATCCG']
    threshold_map = generate_reference_map(keys_used)
    threshold_map['THRESH'] = 17
    threshold_map['OFFSET'] = 5
    threshold_map['DEBUG'] = sum(hash(k) for k in keys_used) % 1000  # Unused

    # Core analysis - where the answer is determined
    final_diagnostic = analyze_readings(clean_reads, threshold_map)
    
    # Final output (must be exactly this format)
    print(f"Result: {final_diagnostic}")