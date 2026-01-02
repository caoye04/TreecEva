def analyze_fragment(fragment):
    if len(fragment) < 3:
        return 0
    mid_index = len(fragment) // 2
    left_part = fragment[:mid_index]
    right_part = fragment[mid_index:]
    
    # Irrelevant transformation chain (distractor)
    transformed = ''.join(sorted(right_part))
    reversed_clean = left_part[::-1].strip('x')
    noise_value = len(transformed) * 2 - len(reversed_clean)

    # Core logic embedded within distractions
    vowel_count = sum(1 for c in fragment if c.lower() in 'aeiou')
    consonant_count = len(fragment) - vowel_count - fragment.count(' ')
    score = (vowel_count * 2) + (consonant_count * 3)
    return score

# Simulate processing of multiple data segments
segments = ['hello world', 'python', 'ai reasoning test', 'complex logic flow', 'nested execution']

# Tracking variables with mixed relevance
capacity_tracker = []
overflow_log = []
diagnostic_trace = []
baseline_offset = 0

for idx, seg in enumerate(segments):
    # Distractor computations
    segment_length = len(seg)
    temp_analysis = seg.upper().replace(' ', '_') + 'X'
    padding_size = (idx + 1) * 2 % 5
    padded_segment = 'x' * padding_size + seg
    
    # Real contribution to logic
    segment_value = analyze_fragment(seg)
    
    # State tracking with conditional side effects
    if segment_value > 15:
        capacity_tracker.append(segment_value + baseline_offset)
        diagnostic_trace.append(f"High-{idx}")
        if len(diagnostic_trace) % 3 == 0:
            baseline_offset += 2  # Subtle state influence
    elif segment_value > 8:
        capacity_tracker.append(segment_value)
        overflow_log.append(segment_length * 0.5)
    else:
        overflow_log.append(segment_value)

# Secondary distractor loop (dead-end computation)
data_summary = []nonsense_shift = 0
for entry in overflow_log:
    nonsense_shift += int(entry) % 3
    summary_entry = f"Z{nonsense_shift}{int(entry)*2}"
    data_summary.append(summary_entry)

# Core final calculation using primary tracked state
def calculate_remaining(tracker, log):
    base = sum(tracker)
    adjustment = len(log) * 1.5
    penalty = 0
    
    # Additional distraction: analyze string pattern in diagnostics
    trace_string = ''.join(diagnostic_trace)
    high_count_str = str(trace_string.count('High'))
    bonus = len(high_count_str) * 1.25  # Minor red herring
    
    # Real penalty logic
    for val in tracker:
        if val > 25:
            penalty += val * 0.1
    
    # Final formula
    result = base - adjustment - penalty + bonus
    return round(result, 4)

# Execute key statement
capacity_snapshot = list(capacity_tracker)  # checkpoint (irrelevant)
final_capacity = calculate_remaining(capacity_tracker, overflow_log)
print(f"Result: {final_capacity}")