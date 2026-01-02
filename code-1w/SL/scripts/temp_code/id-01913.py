def analyze_data(records):
    # Irrelevant preprocessing (distractor)
    clean_records = [r.strip().lower() for r in records if r]
    valid_count = len([r for r in clean_records if 'error' not in r])

    # Core logic disguised among noise
    raw_values = [len(r) for r in clean_records]
    offset = sum(raw_values) % 7

    # Decoy transformation chain
    transformed = []
    for v in raw_values:
        temp = v ^ 5
        temp = (temp + offset) % 256
        transformed.append(temp | 3)  # Bit manipulation red herring

    # Unused but plausible dead path
    if offset > 10:
        backup = [t << 1 for t in transformed]
        return None  # Never reached

    # Actual relevant computation begins
    summation = 0
    threshold = 100
    for i, record in enumerate(records):
        if i % 2 == 0 and len(record) > 3:
            # Multi-step arithmetic with conditional inclusion
            val = (len(record) ** 2) - (i * 4)
            if val > 0:
                summation += val & 15  # Use only lower 4 bits

    # Secondary filtering with string method distraction
    flags = list(map(lambda x: x.startswith('A'), records))
    flag_sum = sum(1 for f in flags if f)

    # Dummy checksum variant (misleading)
    dummy_checksum = (sum(transformed) + flag_sum) % 97

    # Real finalization function (hidden in lambda)
    finalize = lambda x, limit: (x * 3) ^ 456 if x < limit else (x + 78) & 2047

    # Critical statement
    checksum = finalize(summation, threshold)

    # More noise: unused data structure with cross-reference
    log_entry = {
        'raw': records,
        'meta': {'offset': offset, 'valid': valid_count},
        'debug': transformed[:5]
    }

    # Output required result
    print(f"Result: {checksum}")
    return checksum

# Input data with mixed patterns
input_records = ['Alpha', 'Beta!', 'Aardvark', 'Gamma', 'Delta2', 'Abyss', 'Chi']
analyze_data(input_records)