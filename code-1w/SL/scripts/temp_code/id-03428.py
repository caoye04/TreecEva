def analyze_data_stream(data_string):
    # Irrelevant preprocessing: character frequency analysis (distraction)
    char_freq = {c: data_string.count(c) for c in set(data_string)}
    unique_chars = len(char_freq)
    total_length = len(data_string)

    # Decoy transformation: base64-like but unused (dead path)
    reversed_chunks = ''.join([data_string[i:i+2][::-1] for i in range(0, len(data_string), 2)])
    encoded_garbage = ''.join(chr((ord(c) + 3) % 256) for c in data_string)

    # Real processing begins: extract digits and filter valid ones
    raw_digits = [int(c) for c in data_string if c.isdigit()]
    threshold_filter = [d for d in raw_digits if d > 2]  # Only digits > 2 are valid
    valid_count = len(threshold_filter)

    # Bitwise manipulation with red herring variables
    magic_seed = 17
    temp_checksum = 0
    for i, digit in enumerate(threshold_filter):
        temp_checksum ^= (digit << (i % 4))  # Shift-based XOR accumulation
    
    # Distractor: unused recursive function (misleading complexity)
    def calc_recursive(n):
        if n <= 1:
            return 1
        return calc_recursive(n-1) + calc_recursive(n-2)
    
    # Another decoy: complex string splitting with no effect
    fragments = data_string.split('a')
    fragment_lengths = [len(f) for f in fragments if f != '']
    average_frag = sum(fragment_lengths) / len(fragment_lengths) if fragment_lengths else 0

    # Core logic hidden among noise: prime offset based on valid count
    prime_offset = 0
    candidate = valid_count + 10
    while prime_offset == 0:
        is_prime = True
        for j in range(2, int(candidate ** 0.5) + 1):
            if candidate % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_offset = candidate
        candidate += 1

    # Coordination key derived from XOR of even-positioned valid digits
    coordination_key = 0
    for idx, val in enumerate(threshold_filter):
        if idx % 2 == 0:
            coordination_key ^= val

    # Critical statement: what is the value of 'checksum' here?
    checksum = (valid_count * prime_offset) ^ coordination_key

    # Final red herring: unrelated floating point calculation
    entropy_score = sum(d * 0.1 for d in raw_digits) / (valid_count or 1)
    normalized_entropy = round(entropy_score * 100, 4)

    # Output only the target result
    print(f"Result: {checksum}")

# Execute with realistic input
input_stream = "x9a2m4k8p5z1q7r3s6t9"
analyze_data_stream(input_stream)