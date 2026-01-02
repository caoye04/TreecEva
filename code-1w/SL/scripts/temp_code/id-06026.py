from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and metadata
timestamps = [1001, 1002, 1005, 1010, 1011, 1016, 1020]
raw_readings = [3, 5, 7, 11, 13, 17, 19]
noise_flags = [False, True, False, True, False, False, True]

# Irrelevant auxiliary processing: checksum validation (dead path)
def validate_checksum(data):
    return sum(data) % 7 == 0

def generate_metadata_index(timestamps, readings):
    index = {}
    for t, r in zip(timestamps, readings):
        index[t] = {'value': r, 'group': r % 4}
    return index

# Unused transformation: exponential smoothing (distractor)
def smooth_data(readings, alpha=0.3):
    smoothed = [readings[0]]
    for i in range(1, len(readings)):
        smoothed.append(alpha * readings[i] + (1 - alpha) * smoothed[i-1])
    return smoothed

# Decoy function that looks important but isn't used in critical path
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Auxiliary logic: detect arithmetic sequences (used indirectly)
def is_arithmetic(seq):
    if len(seq) < 3:
        return False
    diff = seq[1] - seq[0]
    return all(seq[i] - seq[i-1] == diff for i in range(2, len(seq)))

# Complex pattern analyzer with red herrings
# Combines multiple concepts: sequence analysis, frequency counting, bit manipulation
def analyze_pattern(seq, freq_map):
    n = len(seq)
    
    # Irrelevant intermediate: prime detection side calculation
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_count = sum(1 for x in seq if is_prime(x))
    
    # Distractor: bitmask analysis of position parity
    position_mask = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            position_mask |= (1 << (val % 8))
    
    # Real logic begins: find longest increasing subsequence (LIS)
    if n == 0:
        return 0
    
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
    
    max_lis = max(lis)
    
    # Frequency-based weight from input map
    freq_weight = 0
    for val in seq:
        if val in freq_map:
            freq_weight += freq_map[val]
    
    # Conditional branching based on sequence properties
    adjustment = 1
    if is_arithmetic(seq):
        adjustment = 1.5
    elif seq == sorted(seq, reverse=True):
        adjustment = 0.5
    else:
        adjustment = 1.2
    
    # Bit manipulation distractor: XOR folding
    xor_fingerprint = 0
    for val in seq:
        xor_fingerprint ^= (val * 17) >> 1
    
    # Final score computation - only some components are relevant
    base_score = max_lis * freq_weight * adjustment
    
    # Red herring normalization (unused)
    max_possible = n * n  # theoretical maximum
    normalized = base_score / max_possible if max_possible > 0 else 0
    
    # ACTUAL answer contribution: only base_score matters
    return int(round(base_score))

# Main execution flow
if __name__ == "__main__":
    # Build frequency map using defaultdict (required feature)
    frequency_map = defaultdict(int)
    for val in raw_readings:
        frequency_map[val] += 1
    frequency_map[7] += 2  # Artificial boost for 7
    frequency_map[13] -= 1 # Adjustment
    
    # Add irrelevant extra keys (distractor)
    frequency_map[99] = 5
    frequency_map[101] = -3
    
    # Filter out noisy readings (only even indices without flag)
    filtered_sequence = []
    for i, flag in enumerate(noise_flags):
        if not flag:
            filtered_sequence.append(raw_readings[i])
    
    # This sequence becomes [3, 7, 13, 17]
    sequence = filtered_sequence
    
    # Dead code: unused transformation branch
    if len(sequence) > 10:
        processed = smooth_data(sequence)
    else:
        temp_result = compute_entropy(sequence)  # Computed but not used
        metadata_index = generate_metadata_index(timestamps[:len(filtered_sequence)], filtered_sequence)
    
    # Critical statement
    final_score = analyze_pattern(sequence, frequency_map)
    
    # Print result as required
    print(f"Result: {final_score}")