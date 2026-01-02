import itertools

def generate_checksum(data):
    # Irrelevant function - not used in final computation
    return sum(data) % 256

def decrypt_block(block, key):
    # Decoy decryption logic - never called
    result = 0
    for i, b in enumerate(block):
        result ^= (b + key) << i
    return result & 0xFF

def evaluate_entropy(seq):
    # Distractor: computes entropy but unused
    from math import log2
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def shift_sequence(seq, n):
    # Unused helper - red herring
    n = n % len(seq)
    return seq[n:] + seq[:n]

def build_key_schedule(seed_seq):
    # Complex but partially relevant key derivation
    ks = [seed_seq[i] ^ seed_seq[-i-1] for i in range(len(seed_seq))]
    extended = []
    for a, b in zip(ks, ks[1:] + [ks[0]]):
        extended.append((a + b) * 2)
    # Only first 4 elements are actually used later
    return extended[:4]

def analyze_pattern(seq):
    # Dead code path - looks important but irrelevant
    patterns = {}
    for i in range(len(seq) - 2):
        triplet = tuple(seq[i:i+3])
        patterns[triplet] = patterns.get(triplet, 0) + 1
    return len(patterns)

def filter_outliers(data):
    # Distractor function with misleading statistics
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    threshold = mean_val + 2 * std_dev
    return [x for x in data if x <= threshold]

def process_transmission(signal, schedule):
    # Core logic hidden among distractions
    temp = []
    for idx, val in enumerate(signal):
        if idx % 2 == 0:
            # Apply XOR mask using schedule with wraparound
            masked = val ^ schedule[idx % len(schedule)]
            temp.append(masked)
        else:
            # Alternate path with bit rotation
            rotated = ((val << 1) | (val >> 7)) & 0xFF
            temp.append(rotated)
    
    # Secondary transformation
    transformed = []
    for i, t in enumerate(temp):
        if i < len(schedule):
            t = (t + schedule[i]) % 101  # Mod arithmetic
        if i % 3 == 0:
            t = t ^ (i | 7)  # Bitwise mix
        transformed.append(t)
    
    # Final aggregation
    accumulator = 0
    for a, b in itertools.pairwise(transformed):  # Use of itertools
        if a > b:
            accumulator += a - b
        else:
            accumulator += (b + a) % 97
    
    return accumulator

# Main execution flow
if __name__ == '__main__':
    # Input sequence - appears arbitrary but deterministic
    sequence = [12, 45, 67, 89, 23, 56, 78, 13]
    
    # Irrelevant preprocessing (distractor)
    cleaned = filter_outliers(sequence)
    base_entropy = evaluate_entropy(sequence)
    
    # Key generation (only part is used)
    key_schedule = build_key_schedule(sequence)
    
    # Unused transformations (red herrings)
    shifted_once = shift_sequence(sequence, 3)
    shifted_twice = shift_sequence(shifted_once, 2)
    checksum = generate_checksum(sequence)
    
    # Critical execution point
    final_signal = process_transmission(sequence, key_schedule)
    
    # Irrelevant analysis
    pattern_count = analyze_pattern(sequence)
    
    # Output the target result
    print(f"Result: {final_signal}")