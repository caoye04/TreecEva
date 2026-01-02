from collections import defaultdict
import math

def analyze_pattern_sequence(sequence):
    stats = defaultdict(int)
    for item in sequence:
        if item % 3 == 0:
            stats['divisible_by_3'] += 1
        elif item % 5 == 0:
            stats['divisible_by_5'] += 1
        if item > 10:
            stats['greater_than_10'] += 1
    return stats

def generate_wave_interference(peaks):
    interference_map = {}
    total_peaks = len(peaks)
    for i in range(total_peaks):
        for j in range(i + 1, total_peaks):
            delta = abs(peaks[i] - peaks[j])
            if delta not in interference_map:
                interference_map[delta] = 0
            interference_map[delta] += 1
    sorted_deltas = sorted(interference_map.keys())
    median_delta = sorted_deltas[len(sorted_deltas) // 2] if sorted_deltas else 0
    return interference_map, median_delta

def calculate_frequency_envelope(signal):
    envelope = 0
    for i, s in enumerate(signal):
        envelope += s * math.sin(i * math.pi / 4)
    return round(envelope, 6)

def calculate_interference(seq1, seq2):
    # Core logic starts here
    combined = [a ^ b for a, b in zip(seq1, seq2)]
    
    # Irrelevant transformation (distractor)
    temp_transform = [x * 2 + 1 for x in seq1 if x < 5]
    temp_sum = sum(temp_transform)  # Dead-end variable
    
    # Another red herring: unused frequency analysis
    freq_env = calculate_frequency_envelope(seq2)
    dummy_metric = math.log(freq_env + 10) if freq_env > 0 else 0
    
    # Actual relevant computation branch
    xor_sum = sum(combined)
    shift_count = 0
    for val in combined:
        if val > 0:
            shift_count += (val & 3)  # Bitwise mask on XOR result
    direction_factor = -1 if len(seq1) % 2 == 0 else 1
    
    # Secondary relevant path: counting specific patterns
    pattern_match = 0
    for i in range(1, len(combined)):
        if combined[i] > combined[i-1]:
            pattern_match += 1
    
    # Combine multiple derived values into final result
    base_shift = xor_sum * direction_factor
    adjustment = (shift_count - pattern_match) * 2
    net_phase_shift = base_shift + adjustment
    
    # Decoy print and unused assignment
    debug_info = {'base': base_shift, 'adjust': adjustment, 'final': net_phase_shift}
    unused_cleanup = [x for x in range(8) if x not in seq1]
    
    return net_phase_shift

# Main execution
pattern_a = [1, 4, 2, 8, 5, 7]
pattern_b = [3, 4, 1, 8, 6, 6]

# Distractor: irrelevant data structure buildup
data_log = []
for idx, (a, b) in enumerate(zip(pattern_a, pattern_b)):
    entry = {
        'index': idx,
        'sum': a + b,
        'product': a * b,
        'diff': abs(a - b)
    }
    data_log.append(entry)

# Another red herring: unused statistical analysis
stats_a = analyze_pattern_sequence(pattern_a)
stats_b = analyze_pattern_sequence(pattern_b)

# Real computational flow begins here
interference_details, median_gap = generate_wave_interference(pattern_a + pattern_b)

# Key statement
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Final output
print(f"Result: {net_phase_shift}")