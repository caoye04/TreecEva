def calculate_performance(data):
    # Preprocessing: extract relevant segments
    processed = []
    for entry in data:
        if 'status' in entry and entry['status'] == 'active':
            raw_value = entry['value']
            normalized = (raw_value - 10) ** 2  # Distraction: not directly used
            processed.append(raw_value)

    # Real computation begins: filter and transform
    filtered = [x for x in processed if x % 2 == 1]  # Only odd values contribute
    shifted = [x >> 1 for x in filtered]  # Bitwise shift as part of transformation

    # Accumulate result using modular arithmetic
    total = 0
    multiplier = 3
    for i, val in enumerate(shifted):
        temp_offset = (i + 1) * 0.5  # Red herring: looks important but unused
        total += (val + i) % 7

    # Secondary distraction: dead code path (never executed due to logic)
    if len(processed) > 100:
        backup_result = sum(processed) / len(processed)
        return int(backup_result)

    # Core logic: average of transformed values, then adjusted
    avg_shifted = sum(shifted) / len(shifted) if shifted else 0
    penalty = len(processed) - len(filtered)  # Count how many were even
    final = int(avg_shifted) - penalty

    # String-based obfuscation: irrelevant but plausible
    metadata = "perf_log_2024.txt"
    extension = metadata.split('.')[-1]
    if extension == "txt":
        log_flag = True  # Unused boolean flag

    # Key assignment point
    final_score = final * 2
    return final_score

# Input data setup
data_set = [
    {'value': 21, 'status': 'active'},
    {'value': 24, 'status': 'inactive'},
    {'value': 27, 'status': 'active'},
    {'value': 30, 'status': 'active'},
    {'value': 33, 'status': 'active'},
    {'value': 36, 'status': 'active'}
]

# Execute calculation
final_score = calculate_performance(data_set)
print(f"Result: {final_score}")