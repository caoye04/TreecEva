def analyze_signal_pattern(raw_data, threshold=0.75):
    # Irrelevant signal preprocessing (distractor)
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = [x for x in normalized if x > 0.1]
    entropy = 0.0
    for val in filtered:
        if val > 0:
            entropy -= val * (val).log()

    # Real computation begins: pattern analysis using bitwise and logic
    binary_map = [int(x >= threshold) for x in raw_data]
    transitions = 0
    for i in range(1, len(binary_map)):
        if binary_map[i] != binary_map[i-1]:
            transitions += 1

    # Tuple unpacking and multiple assignments (relevant)
    (primary_count, secondary_count) = (sum(binary_map), len(binary_map) - sum(binary_map))

    # Decoy function that's defined but not used
    def deprecated_analysis(seq):
        return sum([seq[i] ^ seq[i+1] for i in range(len(seq)-1)])

    # String-based flag encoding (red herring)
    status_flags = 'OK WARNING CRITICAL'.split()
    system_status = status_flags[transitions % 3] if transitions < 6 else status_flags[2]
    status_code = ''.join([bin(ord(c))[2:] for c in system_status])[:8]

    # Dictionary operations for diagnostic mapping (partially relevant)
    diagnostics = {
        'baseline': 127,
        'offset': transitions << 2,
        'weight': primary_count >> 1
    }
    
    # Complex data transformation with distractors
    history_log = [
        {'epoch': 2020+i, 'value': (i*17) % 255} for i in range(5)
    ]
    legacy_correction = sum([log['value'] for log in history_log]) // 100

    # Dead code path (never executed)
    if False:
        fallback_metric = 0
        for k, v in diagnostics.items():
            fallback_metric ^= hash(k) % 100

    # Actual core logic buried in noise
    trigger_events = 0
    for i in range(len(raw_data) - 2):
        a, b, c = raw_data[i:i+3]
        if a < b > c and (b - a) > (c - b):  # Local maxima detection
            trigger_events += 1

    # Bit manipulation and integer division
    packed_value = (trigger_events << 3) | (transitions & 7)
    aggregate_score = diagnostics['baseline'] + diagnostics['offset'] - diagnostics['weight']

    # Misleading floating point calculation
    pseudo_entropy = (len(raw_data) * transitions) / (entropy + 1e-8)
    fake_confidence = round(pseudo_entropy / 100, 4)

    # Character counting distraction
    flag_chars = {c: system_status.lower().count(c) for c in 'abcdefghijklmnopqrstuvwxyz'}
    rare_char_bonus = sum([v for k, v in flag_chars.items() if k in 'jkmqwx'])*10

    # Final computation chain (critical)
    temp_result = packed_value ^ diagnostics['baseline']
    correction_factor = (legacy_correction + rare_char_bonus) - 5
    final_diagnostic = aggregate_score + correction_factor

    # Output required result
    print(f"Result: {final_diagnostic}")

# Input data with meaningful structure
input_stream = [0.1, 0.8, 0.3, 0.9, 0.2, 0.7, 0.6, 0.4]
analyze_signal_pattern(input_stream)