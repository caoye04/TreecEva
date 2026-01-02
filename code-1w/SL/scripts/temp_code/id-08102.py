def compute_integrity_score(input_sequence):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x ** 2 for x in input_sequence if x < 0]  # Never used
    temp_buffer = sorted(temp_buffer, reverse=True)  # Distractor sort

    # Initialization of multiple decoy variables
    accumulator = 0
    running_avg = 0.0
    outlier_count = 0
    mode_flag = len(input_sequence) % 4  # Used later, but disguised

    # Decoy statistical analysis (not affecting final result)
    mean_val = sum(input_sequence) / len(input_sequence) if input_sequence else 0
    deviation_sq = [(x - mean_val) ** 2 for x in input_sequence]
    variance = sum(deviation_sq) / len(deviation_sq) if deviation_sq else 0

    # Real data transformation: filter and scale positive values
    scaled_data = []
    for val in input_sequence:
        if val > 0:
            scaled_val = val * (val % 7)  # Nonlinear scaling
            scaled_data.append(scaled_val)

    # Decoy dictionary operations (red herring)
    stats_map = {}
    for i, v in enumerate(scaled_data):
        stats_map[f'item_{i}'] = {
            'value': v,
            'flagged': v > 50,
            'meta': (v * 3) % 17
        }
    # Another distraction: unused recursive function
    def _unused_dfs(path_total, depth):
        if depth == 0:
            return path_total
        return _unused_dfs(path_total + depth, depth - 1)

    # Real computation begins here
    data_sum = sum(scaled_data)  # Core component

    # Multiple prime checks as distraction
    primes_evaluated = []
    for n in range(2, 15):
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
        if is_prime:
            primes_evaluated.append(n)

    prime_base = primes_evaluated[5] if len(primes_evaluated) > 5 else 13  # Fixed to 13

    # Core logic embedded in distractions
    checksum = 0
    if len(input_sequence) > 0:
        checksum = (data_sum + mode_flag) % prime_base  # Critical assignment point

    # Final red herring: unused complex structure
    report_summary = {
        'final_checksum': checksum,
        'debug_trace': [
            {'phase': 'init', 'status': 1},
            {'phase': 'transform', 'status': 2},
            {'phase': 'verify', 'status': checksum ^ 255}
        ],
        'archive_flag': False
    }

    # Only this line matters for output
    return checksum

# Main execution with fixed input
sequence = [4, -2, 7, 1, 8, -5, 3, 9]
result = compute_integrity_score(sequence)
print(f"Result: {result}")