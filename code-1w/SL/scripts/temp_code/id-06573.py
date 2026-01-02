def analyze_data_stream(raw_samples, threshold=73):
    # Simulate preprocessing pipeline with red herrings
    processed = [x for x in raw_samples if x > 0]  # Ignore non-positive values
    outliers = [x for x in processed if x > threshold]  # Distractor: not used later
    filtered = [x for x in processed if x % 2 == 1]  # Keep only odd values

    # Initialize various variables - many are decoys
    base_shift = 17
    prime_offset = 97
    temp_cache = []
    running_sum = 0
    snapshot_log = []
    modulus = 10007
    iteration_count = 0

    # Complex transformation with nested logic and distractions
    for index, value in enumerate(filtered):
        if index % 3 == 0:
            transformed = (value ^ base_shift) + index
        elif index % 4 == 0:
            transformed = (value + 13) * 2  # Dead branch due to prior condition
        else:
            transformed = value * 3 % 1000

        # Conditional insertion with misleading logging
        if transformed > 50:
            temp_cache.append(transformed)
            running_sum += transformed
            if len(temp_cache) % 2 == 0:
                snapshot_log.append(running_sum)  # Unused log

        iteration_count += 1
        if iteration_count > 100:  # Never triggers
            break

    # Core computation path (non-obvious due to noise)
    valid_sequence = [x for x in temp_cache if x < 500]
    if len(valid_sequence) < 5:
        filler = [i * 19 % 499 for i in range(5 - len(valid_sequence))]
        valid_sequence.extend(filler)

    # Critical statement embedded in distracting environment
    checksum = (valid_sequence[-1] * prime_offset) % modulus

    # Irrelevant final transformations
    final_weight = sum([i*i for i in range(len(snapshot_log))])  # Unused
    debug_flag = False
    if debug_flag:  # Dead code
        print('Debug:', checksum)

    print(f"Result: {checksum}")

# Generate deterministic input
import math
raw_input = [int(100 * math.sin(i) + 128) for i in range(64)]
analyze_data_stream(raw_input)