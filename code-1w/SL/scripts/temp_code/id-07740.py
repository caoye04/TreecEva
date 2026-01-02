def main():
    data_stream = [12, 15, 22, 27, 30, 35, 42, 44, 48, 51]
    
    # Irrelevant transformation: reverse mapping for unused feature
    reversed_map = {v: i for i, v in enumerate(reversed(data_stream))}
    offset_correction = sum([i * 2 for i in range(5)])  # Unused adjustment
    
    # Core processing chain
    scaled = [x * 2 + 1 for x in data_stream]
    adjusted = [x - 10 for x in scaled if x > 30]  # Filtering based on threshold
    
    # Distractor: complex but unused conditional block
    temp_state = 0
    for val in adjusted:
        if val % 4 == 0:
            temp_state += val // 4
        elif val % 5 == 0:
            temp_state -= val // 5
    
    # Simulate sensor noise filtering (only some values are valid)
    processed = []
    for x in adjusted:
        if x < 100:
            processed.append(x)
            if x % 7 == 0:
                processed.append(x // 2)  # Duplicate handling for redundancy

    # Bitwise integrity check (distractor)
    parity_flags = 0
    for p in processed:
        parity_flags ^= (p & 1) << 1

    # Real computation path
    filtered_evens = list(filter(lambda x: x % 2 == 0, processed))
    filtered_multiples_of_3 = filter(lambda x: x % 3 == 0, filtered_evens)
    sum_filtered = sum(filtered_multiples_of_3)
    
    # Finalization with lambda (used)
    finalize = lambda x: x + (x % 11)
    checksum = finalize(sum(filter(lambda x: x % 3 == 0, processed)))
    
    # Dead code: post-check that doesn't affect result
    if checksum < 500:
        checksum *= 2
    else:
        checksum += 10  # Not triggered
        backup = [checksum - i for i in range(3)]

    print(f"Result: {checksum}")

main()