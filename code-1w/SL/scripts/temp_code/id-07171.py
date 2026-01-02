def analyze_pattern(data_stream):
    # Irrelevant signal processing variables
    alpha_filter = 0.85
    beta_threshold = 23.7
    gamma_correction = [i ** 0.5 for i in range(10)]

    # Distractor: unused transformation pipeline
    def transform_signal(x):
        return (x >> 2) ^ 0xAFFE

    # Actual relevant data
    raw_segments = [18, 45, 23, 67, 12, 89, 34, 76]
    temp_buffer = [x for x in raw_segments if x % 2 == 1]  # filter odds

    # Red herring: complex but unused recursive function
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)
    
    lookup_table = {i: (i * i) % 19 for i in range(15)}

    # Real logic begins: slice middle segment
    focus_window = raw_segments[2:6]  # [23, 67, 12, 89]

    # Conditional filtering based on mapped value in lookup
    candidate_pool = []
    for val in focus_window:
        if lookup_table.get(val % 15, 0) > 7:
            candidate_pool.append(val)

    # Now apply bitwise weighting
    weighted_vals = []
    for idx, v in enumerate(candidate_pool):
        shifted = (v << 1) | (idx & 1)
        weighted_vals.append(shifted)

    # Another distraction: unused accumulator
    total_energy = sum((x ** 2 for x in gamma_correction))

    # Critical path: determine validity via length check and parity
    if len(weighted_vals) >= 3 and sum(weighted_vals) % 2 == 0:
        valid_sequence = weighted_vals[::-1]  # reverse order
    else:
        valid_sequence = weighted_vals[::2]  # every other element

    # Decoy computation with plausible naming
    entropy_score = 0
    for i in range(len(valid_sequence)):
        entropy_score += valid_sequence[i] ^ (i * 17)

    # Key constants mixed among distractors
    prime_offset = 1013
    modulus = 9871

    # Unused alternate checksum method
    def crc_calc(arr):
        result = 0
        for a in arr:
            result = (result * 31 + a) % 65535
        return result

    # Critical statement
    checksum = (valid_sequence[0] * prime_offset) % modulus

    # Final red herring: conditional override that never triggers
    if len(raw_segments) == 10:
        checksum = (checksum + 999) % 10000

    print(f"Result: {checksum}")

analyze_pattern(list(range(10, 70, 3)))