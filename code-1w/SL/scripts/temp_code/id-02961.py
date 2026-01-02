import itertools

# System diagnostics simulator with red herrings and complex data paths
def analyze_sequence(log_series, threshold):
    if len(log_series) < 5:
        return 0

    # Irrelevant transformation branch (dead path)
    temp_shadow = [x ** 0.5 for x in log_series if x > 0]
    normalization_factor = sum(temp_shadow) / len(temp_shadow) if temp_shadow else 1

    # Distractor: complex but unused calculation chain
    alpha_chain = list(itertools.accumulate(log_series, lambda a, b: (a + b) % 7))
    beta_mirror = [x for x in alpha_chain if x in log_series]
    gamma_shift = [(i * beta_mirror[i]) % 4 for i in range(len(beta_mirror)) if i % 2 == 0]

    # Real processing starts here — heavily masked by prior noise
    filtered = [x for x in log_series if x % 2 == 1]  # only odd values matter
    smoothed = [sum(filtered[i:i+3]) for i in range(0, len(filtered)-2, 3)]  # sliding window sum

    # Conditional mutation based on threshold
    if len(smoothed) >= 3:
        smoothed = [x for x in smoothed if x > threshold]

    # Key intermediate value buried in logic
    base_metric = len(smoothed) * 17

    # Decoy recursive function that's defined but not used
    def decay_sequence(val, depth):
        if depth <= 0 or val < 1:
            return val
        return decay_sequence(val / 2, depth - 1) + decay_sequence(val // 3, depth - 2)

    # Another irrelevant block: character frequency simulation
    status_tag = "diagnostics_active"
    char_count = {c: status_tag.count(c) for c in set(status_tag)}
    case_transform = ''.join([c.upper() if char_count[c] > 1 else c for c in status_tag])

    # Real metric computation — subtle and easy to miss
    adjustment = 0
    for i, val in enumerate(smoothed):
        if val % 4 == 0:
            adjustment += 1
        elif val % 3 == 0:
            adjustment -= 2

    return base_metric + adjustment

# Secondary system: data alignment verification (mostly decoy)
def align_segments(data_chunk):
    size = len(data_chunk)
    if size == 0:
        return 0

    # Bit manipulation red herring
    bit_analysis = [data_chunk[i] ^ data_chunk[-i-1] for i in range(size)]
    parity_check = sum(1 for x in bit_analysis if bin(x).count('1') % 2 == 0)

    # Unused slicing operations
    mid_slice = data_chunk[size//4 : -(size//4)] if size > 4 else []
    reverse_twin = data_chunk[::-1]
    overlap_score = sum(1 for a, b in zip(data_chunk, reverse_twin) if a == b)

    # Actual contribution: count of values > 100
    return sum(1 for x in data_chunk if x > 100)

# Core aggregation function containing the final answer
def aggregate_metrics(buffer, key):
    # Multiple distractions at start
    audit_log = []
    temp_frame = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp_frame[i][j] = (i * key + j * len(audit_log)) % 9

    # Real logic: process buffer using key as filter threshold
    segment_a = buffer[:len(buffer)//2]
    segment_b = buffer[len(buffer)//2:]

    result_a = analyze_sequence(segment_a, key)
    result_b = align_segments(segment_b)

    # Critical operation — combines two independent results
    combined = result_a * result_b

    # Final adjustment via modular arithmetic
    final_shift = (combined + key**2) % 9973

    # This is the true answer variable
    final_diagnostic = (final_shift * 3) - 418

    # More distraction: meaningless string formatting
    report_template = f"Diagnostic run: {final_shift}, Status: OK"
    checksum = sum(ord(c) for c in report_template) % 256

    # Dead code path — never executed due to constant condition
    if False:
        fallback = 0
        for x in itertools.combinations([1,2,3], 2):
            fallback += x[0] * x[1]
        final_diagnostic = fallback

    return final_diagnostic

# Execution entry point
if __name__ == '__main__':
    timing_buffer = [15, 22, 33, 45, 57, 60, 73, 88, 91, 105, 117, 120, 131]
    validation_key = 25

    # These variables are part of distraction framework
    debug_trace = [x & 7 for x in timing_buffer]
    slice_preview = timing_buffer[::3]
    inverted_map = {i: timing_buffer[i] for i in range(len(timing_buffer))}

    # Key execution point
    final_diagnostic = aggregate_metrics(timing_buffer, validation_key)

    print(f"Result: {final_diagnostic}")