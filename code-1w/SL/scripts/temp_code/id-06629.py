def analyze_data_stream(raw_input):
    # Irrelevant transformation: base conversion with decoy output
    decoy_buffer = [x % 7 for x in raw_input if x > 5]
    temp_shadow = [x * 2 + 1 for x in decoy_buffer]

    # Actual processing begins: mask and filter logic
    masked_data = [x ^ 3 for x in raw_input]  # Bit manipulation red herring?

    # Misleading statistical summary (unused)
    mean_val = sum(masked_data) / len(masked_data) if masked_data else 0
    outlier_threshold = mean_val * 1.5  # Looks important, never used

    # Core logic disguised among distractions
    processed = []
    for i, val in enumerate(masked_data):
        if i % 2 == 0:  # Only even indices matter
            shifted = val >> 1
            if shifted > 10:  # Filter condition
                processed.append(shifted)

    # Decoy list comprehension with similar name
    process_log = [f'Item_{i}' for i in range(len(processed) + 5)]  # Unused string log

    # Slicing operation (required feature): reverse every third element
    sliced_core = processed[::-3]  # Real data path

    # Another red herring: recursive checksum (never called)
    def checksum(arr):
        return arr[0] if len(arr) == 1 else arr[-1] + checksum(arr[:-1])

    # Boolean logic chain with short-circuiting distraction
    is_valid = len(sliced_core) > 0 and sliced_core[0] > 5 or False
    flag_override = not is_valid and True or False  # Complex but irrelevant

    # Conditional execution that looks consequential
    if flag_override:
        final_adjustment = max(sliced_core) * -1
    else:
        final_adjustment = 0  # Never applied due to logic above

    # Critical assignment point
    valid_entries = [x + final_adjustment for x in sliced_core]  # Adjustment is 0

    # Key computation
    filtered_sum = sum(valid_entries)

    # Dead code path: simulation of recovery protocol
    if filtered_sum < 0:
        backup_repair = [x + abs(filtered_sum) for x in valid_entries]
        filtered_sum = sum(backup_repair) // 2

    return filtered_sum

# Simulate input
input_sequence = [12, 8, 14, 6, 18, 4, 22, 2, 25, 1, 28]
result = analyze_data_stream(input_sequence)
print(f"Result: {result}")