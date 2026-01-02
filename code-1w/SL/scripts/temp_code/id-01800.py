from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor readings with noise and redundancy
def collect_sensor_data():
    raw_readings = [127, 63, 95, 79, 31, 159]
    filtered = [x for x in raw_readings if x > 50]
    return filtered

# Legacy system compatibility layer (mostly irrelevant)
def legacy_normalization(data):
    normalized = []
    for val in data:
        temp = val >> 2
        temp = temp ^ 15
        temp = (temp + 9) % 256
        normalized.append(temp)
    return normalized  # Never actually used

# Core diagnostic logic
def run_diagnostics():
    sensors = collect_sensor_data()
    
    # Irrelevant transformation chain
    decoy_transform = [(x | 64) & 191 for x in sensors]
    decoy_stats = defaultdict(int)
    for val in decoy_transform:
        decoy_stats[val] += 1
    
    # Actual signal extraction
    amplitudes = [x & 63 for x in sensors]  # Mask to extract lower 6 bits
    frequencies = [x % 11 for x in sensors]
    
    # Red herring: complex but unused combinatorics
    unused_pairs = list(combinations(amplitudes, 2))
    pair_sums = []
    for a, b in unused_pairs:
        pair_sums.append((a + b) * (a ^ b))
    
    # Distractor: frequency analysis with dead end
    freq_count = Counter(frequencies)
    dominant_freq = max(freq_count, key=freq_count.get)
    harmonic_check = [f for f in frequencies if f % dominant_freq == 0] if dominant_freq != 0 else []
    
    # Meaningless cyclic padding
    pad_cycle = cycle([2, 4, 8])
    extended_amplitudes = amplitudes.copy()
    for _ in range(5):
        extended_amplitudes.append(next(pad_cycle))
    
    # Real computation begins here
    base_energy = 0
    for i, amp in enumerate(amplitudes):
        if i % 2 == 0:
            base_energy += amp * frequencies[i]
        else:
            base_energy += amp // (frequencies[i] if frequencies[i] != 0 else 1)
    
    # Secondary processing with conditional masking
    masked_values = []
    for val in amplitudes:
        if val > 30:
            masked_values.append(val & ~8)  # Clear bit 3 if val > 30
        else:
            masked_values.append(val | 4)
    
    # Aggregation through weighted sum
    weight_sequence = [1, -1, 2, -2, 3, -3]
    weighted_sum = sum(w * v for w, v in zip(weight_sequence, masked_values))
    
    # Correction based on parity and overflow tracking
    overflow_count = 0
    for val in sensors:
        if (val & (val - 1)) == 0:  # power of two check
            overflow_count += 1
    
    # Decoy checksum (looks important, never used)
    checksum = 0
    for i, val in enumerate(sensors):
        checksum ^= (val + i) * 3
    checksum = (checksum + 512) % 1024
    
    # Critical path: final aggregation
    aggregate_score = base_energy + abs(weighted_sum)
    
    # Correction factor based on structural properties
    bit_pattern_count = sum(1 for val in sensors if (val & 16) and not (val & 32))
    correction_factor = (bit_pattern_count * 7) - (overflow_count * 3)
    
    # Final result assignment — KEY STATEMENT
    final_diagnostic = aggregate_score + correction_factor
    
    # Output required format
    print(f"Result: {final_diagnostic}")
    
    # Dead code path: looks like post-processing
    if final_diagnostic > 100:
        adjusted = final_diagnostic >> 1
        for _ in range(3):
            adjusted = (adjusted ^ 42) % 800
        # This doesn't affect anything
    
    return final_diagnostic

# Execute main logic
result = run_diagnostics()