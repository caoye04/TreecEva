def compute_system_diagnostic(data_stream):
    # Simulate multi-layer signal processing with distractions
    raw_samples = [x for x in data_stream if x > 0]  # irrelevant filtering
    shifted_data = [x << 2 for x in raw_samples]  # bit manipulation red herring

    # Core logic setup
    base_threshold = 7
    scaling_factor = 3
    candidate_pairs = []

    # Generate all possible product pairs (nested loops, 3-level deep)
    for i in range(len(raw_samples)):
        for j in range(i + 1, len(raw_samples)):
            product = raw_samples[i] * raw_samples[j]
            if product % 2 == 1:  # only odd products considered
                candidate_pairs.append(product)

    # Distractor: complex but unused transformation chain
    decoy_transform = set()
    for val in shifted_data:
        transformed = (val ^ 5) >> 1
        if transformed < 100:
            decoy_transform.add(transformed)
    decoy_result = sum(decoy_transform) * scaling_factor - 123  # dead end

    # Another distraction: recursive validation (never called)
    def validate_consistency(arr, idx=0):
        if idx >= len(arr):
            return True
        if arr[idx] < 0:
            return False
        return validate_consistency(arr, idx + 1)

    # Real path: filter products greater than threshold^2
    threshold_squared = base_threshold ** 2
    filtered_candidates = [p for p in candidate_pairs if p > threshold_squared]

    # Apply secondary filter: must not be divisible by scaling factor
    refined_filter = [p for p in filtered_candidates if p % scaling_factor != 0]

    # Misleading intermediate aggregation
    pseudo_checksum = 0
    for num in refined_filter:
        pseudo_checksum += (num * 2) % 97
    pseudo_checksum = pseudo_checksum / 2 if pseudo_checksum > 0 else 0  # looks important

    # Key computation point
    filtered_sum = sum(refined_filter)

    # Final output (only this matters)
    print(f"Result: {filtered_sum}")

    # Return nothing relevant — focus on side effect
    return decoy_result

# Input data with mixed properties
input_stream = [2, 3, 5, 4, 7, -1, 0, 8]
system_output = compute_system_diagnostic(input_stream)