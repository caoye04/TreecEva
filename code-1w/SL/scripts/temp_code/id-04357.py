from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor data processing with red herrings
def analyze_readings(raw_stream, threshold=75):
    raw_stats = defaultdict(int)
    filtered_peaks = []
    temp_buffer = []

    for val in raw_stream:
        if val > threshold:
            raw_stats['high_count'] += 1
            if val % 2 == 1:
                filtered_peaks.append(val)
        else:
            raw_stats['low_count'] += 1
            temp_buffer.append(val)

    # Irrelevant transformation: character frequency (decoy)
    decoy_text = "sensor_overflow_error"
    char_freq = Counter(decoy_text)
    vowel_count = sum(char_freq[c] for c in 'aeiou')  # Misleading calculation

    # Real logic branch disguised among distractors
    peak_sum = sum(filtered_peaks)
    peak_count = len(filtered_peaks)
    average_peak = peak_sum / peak_count if peak_count else 0

    # Dead code path (never executed due to fixed input)
    if False and raw_stats['high_count'] > 100:
        fallback_mode = True
        recovery_state = [x * 0.9 for x in temp_buffer]
    else:
        fallback_mode = False
        recovery_state = None

    # Bit manipulation red herring (no effect on final result)
    masked_value = peak_sum ^ 0xFFFF
    shifted_mask = masked_value >> 4

    # Conditional early return that doesn't trigger
    if len(temp_buffer) == 0:
        return -999  

    # Core signal extraction (obscured)
    signal_pattern = [x for x in raw_stream if 50 < x < 90]
    pattern_cycle = cycle(signal_pattern)
    cycle_sum = sum(next(pattern_cycle) for _ in range(len(signal_pattern)))

    # Decoy statistical measures
    variance_proxy = sum((x - average_peak) ** 2 for x in filtered_peaks) / len(filtered_peaks) if filtered_peaks else 0
    entropy_approx = -(vowel_count / len(decoy_text)) * 0.5 if vowel_count else 0

    # Critical intermediate values
    base_metric = average_peak * raw_stats['high_count']
    adjustment = (cycle_sum // 10) % 17

    # Distractor: unused recursive function
    def recursive_noise(n):
        if n <= 1:
            return 1
        return recursive_noise(n-1) + recursive_noise(n-2)
    
    # Unused call (dead code)
    _ = recursive_noise(5) if False else 0

    # Final computation chain
    aggregate_score = base_metric - adjustment
    
    # Secondary correction from bit analysis (subtle but valid)
    binary_ones = bin(shifted_mask).count('1')
    correction_factor = binary_ones * 3 - 5  # Depends on earlier XOR/shift (actually used)

    # Key statement
    final_diagnostic = aggregate_score + correction_factor

    # Multiple print statements (only last matters)
    print(f"Diagnostics: {final_diagnostic}")
    return final_diagnostic

# Input data crafted to produce deterministic output
data_stream = [68, 82, 76, 91, 85, 73, 88, 94, 79, 81, 77, 89, 95, 69, 83]

# Entry point
result = analyze_readings(data_stream)
Target result: {result}