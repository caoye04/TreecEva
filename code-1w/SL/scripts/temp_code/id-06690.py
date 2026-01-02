from itertools import combinations, cycle

# Simulated sensor data with noise and redundant readings
data_stream = [189, 23, 45, 76, 12, 99, 101, 21, 44, 77, 13, 98, 102, 22, 46]
noise_floor = 20
signal_threshold = 75

decoy_results = []
for i in range(len(data_stream)):
    if data_stream[i] > noise_floor:
        decoy_results.append(data_stream[i] ** 2)

# Extract high-confidence signals
signals = [x for x in data_stream if x > signal_threshold]

# Irrelevant transformation: frequency simulation (dead-end path)
frequency_map = {}
for s in set(signals):
    freq = sum(1 for x in data_stream if x == s)
    frequency_map[s] = freq * 1.5

# Generate all possible 3-element increasing subsequences
subsequences = list(combinations(signals, 3))
filtered_chains = []
for seq in subsequences:
    if seq[0] < seq[1] < seq[2] and (seq[2] - seq[1]) != (seq[1] - seq[0]):
        filtered_chains.append(seq)

# Compute entropy proxy (unused distractor)
import math
total_energy = sum(s**2 for s in signals)
entropy_proxy = sum(s / total_energy * math.log(s) for s in signals if s > 0)

# Real computation begins: find valid chain with maximal spread
best_chain = None
max_spread = -1
for chain in filtered_chains:
    spread = chain[2] - chain[0]
    if spread > max_spread:
        max_spread = spread
        best_chain = chain

# Destructuring assignment (relevant)
first_val, mid_val, last_val = best_chain

# Decoy function that's defined but not used
def analyze_pattern(seq):
    return sum(seq) * len(seq)

# Tuple-based modular arithmetic chain
chain_tuple = (first_val % 17, mid_val % 11, last_val % 13)
modulus = 10007
prime_offset = 103

# Secondary filter: only chains where tuple elements are distinct
if len(set(chain_tuple)) == 3:
    # Compute base sum from original values
    valid_sequence_sum = sum(best_chain)

    # Red herring: unused weighted sum
    weights = cycle([0.5, 1.0, 1.5])
    weighted = sum(w * v for w, v in zip(weights, best_chain))

    # Key statement
    checksum = (valid_sequence_sum * prime_offset) % modulus

    # More irrelevant operations
    parity_check = sum(1 for x in chain_tuple if x % 2 == 0)
    if parity_check > 1:
        checksum += 500  # misleading branch never taken

# Final output
print(f"Result: {checksum}")