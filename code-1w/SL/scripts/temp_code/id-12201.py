def main():
    # System configuration parameters (irrelevant)
    buffer_size = 4096
    timeout_limit = 30
    max_retries = 5
    debug_mode = False

    # Core data sequence (relevant)
    signal_data = [18, 27, 9, 45, 63, 12, 81, 72]
    
    # Noise injection for simulation (distractor)
    noise_profile = [x % 7 for x in range(len(signal_data))]
    filtered_noise = list(filter(lambda x: x > 3, noise_profile))
    adjusted_signal = [s + n for s, n in zip(signal_data, noise_profile)]  # Not actually used

    # Data transformation pipeline
    processed = []
    for i, val in enumerate(signal_data):
        if i % 2 == 0:
            transformed = val ^ 0b1101  # XOR with binary pattern
        else:
            transformed = val | 0b1010      # OR with binary pattern
        processed.append(transformed)
    
    # Red herring: unused frequency analysis
    def compute_entropy(seq):
        from math import log2
        freq = {}
        for item in seq:
            freq[item] = freq.get(item, 0) + 1
        entropy = -sum((count / len(seq)) * log2(count / len(seq)) for count in freq.values())
        return round(entropy, 4)
    entropy_value = compute_entropy(signal_data)  # Computed but not used

    # Actual summation path
    temp_storage = {i: v for i, v in enumerate(processed)}  # dict storage (redundant)
    summation = 0
    for idx in range(len(processed)):
        if idx in temp_storage:
            summation += temp_storage[idx] * (idx + 1)  # weighted sum by index+1

    # Encoding key derived from dummy conditions
    flags = [True, False, True]
    mode_flag = any(flags) and not all(flags)
    encoding_key = 17 if mode_flag else 23
    backup_key = 19

    # Decoy cryptographic function (never called)
    def encrypt_chunk(data, key):
        return [(d * key) % 257 for d in data]

    # Finalization logic (critical)
    def finalize(total, key):
        intermediate = total ^ key
        intermediate = (intermediate + (intermediate >> 4)) & 0xFFFF
        return abs(intermediate - 500)  # deterministic scalar adjustment

    checksum = finalize(summation, encoding_key)

    # Dead code branch (misleading)
    if debug_mode:
        validation_hash = sum(checksum % (i+1) for i in range(10))
        print(f"Validation: {validation_hash}")

    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()