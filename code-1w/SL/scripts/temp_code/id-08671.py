import itertools

# System health monitoring simulation with diagnostic interference

def analyze_phase_shift(samples, threshold):
    """Irrelevant frequency analysis (distractor)"""
    count = 0
    for s in samples:
        if s > threshold * 1.5:
            count += 1
    return count


def compute_entropy(data):
    """Unused entropy calculation - red herring"""
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for f in freq.values():
        p = f / total
        entropy -= p * log(p)
    return round(entropy, 4)


def validate_sequence(seq):
    """Misleading validation path - never called"""
    return all(x in {0,1} for x in seq) and len(seq) == 8

# Real processing begins here
raw_timings = [234, 567, 89, 445, 12, 901, 333, 678]
dropped_packets = {5, 12, 15, 23, 901}

# Irrelevant transformation chain
shifted = [x ^ 255 for x in raw_timings]
filtered = [x for x in shifted if x < 500]
expanded = list(itertools.chain.from_iterable([(x, x+1) for x in filtered]))
expanded_set = set(expanded)

# Core logic buried in noise
active_windows = []
for i, t in enumerate(raw_timings):
    if t % 2 == 0 and t not in dropped_packets:
        active_windows.append(i * t)

# Decoy state variables
system_state_vector = [0] * 8
for idx in range(len(system_state_vector)):
    if idx % 3 == 0:
        system_state_vector[idx] = idx ** 2 + 100

# Bit manipulation red herring
obfuscation_mask = 0b101010
encoded_timing = 0
for t in raw_timings[:3]:
    encoded_timing ^= (t & 0b1111)

# Critical data preparation
timing_data = [t for t in raw_timings if t not in dropped_packets]
failure_flags = set()
for t in timing_data:
    if t < 100 or t > 800:
        failure_flags.add(t)

# Distractor: unused statistical summary
stat_summary = {
    'mean': sum(raw_timings) / len(raw_timings),
    'peak': max(raw_timings),
    'variance': sum((x - sum(raw_timings)/len(raw_timings))**2 for x in raw_timings) / len(raw_timings)
}

# Another decoy function call (no effect)
corrupted_estimate = analyze_phase_shift(raw_timings, 100)

# Real computation hidden among distractions
def aggregate_metrics(times, errors):
    base_score = 0
    adjustment = 0
    
    # Complex conditional scoring
    for val in times:
        if val in errors:
            if val < 100:
                adjustment -= 3
            else:
                adjustment -= 7
        else:
            if 100 <= val <= 600:
                base_score += val // 10
            else:
                base_score += val // 15
    
    # Set operations used meaningfully but with distraction
    error_set = set(errors)
    high_errors = {x for x in error_set if x > 500}
    low_errors = {x for x in error_set if x <= 500}
    
    # Cross-reference with original data
    valid_high_count = len([x for x in times if x > 500 and x not in errors])
    
    # Final formula combining multiple concepts
    penalty = len(high_errors) * 15 + len(low_errors) * 5
    bonus = valid_high_count * 4
    
    intermediate = base_score + adjustment * 2 - penalty + bonus
    
    # Apply bit trick irrelevant to final result but looks important
    masked = intermediate ^ 0xFF
    final = intermediate  # The real answer ignores masking
    
    return final

# Key execution point
final_diagnostic = aggregate_metrics(timing_data, failure_flags)

# Print required output
print(f"Target result: {final_diagnostic}")